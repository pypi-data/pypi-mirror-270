#!/usr/bin/env python3

"""Runs the DockerShaper TUI in an auto-reloading and asynchronous way"""
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
# _pylint: disable=fixme

import asyncio
import importlib
import logging
import sys
import time
from collections.abc import MutableMapping
from pathlib import Path
from types import ModuleType
from typing import cast

import psutil
from datetime import datetime
from apparat import fs_changes
from rich.text import Text
from rich.markup import escape as markup_escape
from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.widgets import Button, Label, Static, Tree
from textual.widgets.tree import TreeNode
from trickkiste.base_tui_app import TuiBaseApp
from trickkiste.misc import date_str, dur_str, process_output, age_str

from docker_shaper import dynamic
from docker_shaper.dynamic import Container, ImageIdent, Network, Volume, short_id
from docker_shaper.utils import container_markup, get_hostname, load_module

CONFIG_FILE = dynamic.BASE_DIR / "config.py"

__version__ = "2.0.0"  # It MUST match the version in pyproject.toml file


def log() -> logging.Logger:
    """Returns the logger instance to use here"""
    return logging.getLogger("docker-shaper")


async def schedule_cleanup(global_state: dynamic.GlobalState):
    """Async infinitve loop wrapper for cleanup"""
    while True:
        try:
            while True:
                if (
                    interval := global_state.intervals.get("cleanup", 3600)
                ) and global_state.cleanup_fuse > interval:
                    global_state.cleanup_fuse = 0
                    break
                if (interval - global_state.cleanup_fuse) % 60 == 0:
                    log().debug(
                        "cleanup: %s seconds to go..", (interval - global_state.cleanup_fuse)
                    )
                await asyncio.sleep(1)
                global_state.cleanup_fuse += 1
            await asyncio.ensure_future(dynamic.cleanup(global_state))
        except Exception:  # pylint: disable=broad-except
            dynamic.report(global_state)
            await asyncio.sleep(5)


def load_config(path: Path, global_state: dynamic.GlobalState) -> ModuleType:
    """Load the config module and invoke `reconfigure`"""
    module = load_module(path)
    try:
        module.modify(global_state)
        dynamic.reconfigure(global_state)
    except AttributeError:
        log().warning("File %s does not provide a `modify(global_state)` function")
    return module


async def watch_fs_changes(global_state: dynamic.GlobalState):
    """Watch for changes on imported files and reload them on demand"""
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)

    async for changes in (
        relevant_changes
        async for chunk in fs_changes(
            Path(dynamic.__file__).parent, CONFIG_FILE.parent, min_interval=4, postpone=False
        )
        if (changed_files := set(chunk))
        for loaded_modules in (
            {
                Path(mod.__file__): mod
                for mod in sys.modules.values()
                if hasattr(mod, "__file__") and mod.__file__
                if not any(infix in mod.__file__ for infix in (".pyenv", ".venv", "wingpro"))
            },
        )
        if (
            relevant_changes := [
                (path, loaded_modules.get(path))
                for path in changed_files
                if path == CONFIG_FILE or path in loaded_modules
            ]
        )
    ):
        for changed_file, module in changes:
            if "flask_table" in changed_file.as_posix():
                continue
            try:
                if changed_file == CONFIG_FILE:
                    log().info("config file %s changed - apply changes", changed_file)
                    load_config(CONFIG_FILE, global_state)
                else:
                    log().info("file %s changed - reload module", changed_file)
                    assert module
                    importlib.reload(module)
            except Exception:  # pylint: disable=broad-except
                dynamic.report(global_state)
                await asyncio.sleep(5)
        try:
            dynamic.setup_introspection()
        except Exception:  # pylint: disable=broad-except
            dynamic.report(global_state)
            await asyncio.sleep(5)


class DockerShaper(TuiBaseApp):
    """Tree view for Jenkins upstream vs. JJB generated jobs"""

    CSS = """
        #logo {background: $panel;}
        RichLog {height: 15; border: solid grey;}
        Tree > .tree--guides {
            color: $success-darken-3;
        }
        Tree > .tree--guides-selected {
            text-style: none;
            color: $success-darken-1;
        }
        Button  {
            height: 1;
            width: 30;
            border: none;
            /*
            margin: 1 1;
            */
        }
        #dashboard {
            layout: grid;
            grid-size: 2;
            grid-columns: 1fr 1fr;
            border: solid $accent;
            padding: 1;
            /*
            width: 80%;
            width: 80;
            */
            height: 20;
        }
        #header {
            text-style: bold;
        }
        #footer {
            width: 100%;
            background: $accent;
            text-style: bold;
            color: $text;
            dock: bottom;
            height: 1;
        }
    """

    BINDINGS = [
        # We don't want the user to accidentally quit DockerShaper by pressing CTRL-C instead of
        # detatching a screen or tmux session. So we inform them to press CTRL-Q instead
        Binding("ctrl+q", "quit"),
        Binding("ctrl+c", "inform_ctrlc_deactivated"),
    ]

    def __init__(self) -> None:
        super().__init__(logger_funcname=False)

        self.docker_stats_tree: Tree[None] = Tree("Docker stats")
        self.removal_patterns: MutableMapping[str, int] = {}
        self.pattern_usage_count: MutableMapping[str, int] = {}
        self.global_state = dynamic.GlobalState()
        mod_config = load_config(CONFIG_FILE, self.global_state)
        self.removal_patterns = mod_config.removal_rules(111)
        self.lbl_event_horizon = Label("event horizon")
        self.lbl_sys = Label("sys info")
        self.lbl_switches = Label("switches")
        self.lbl_expiration = Label("expiration ages")
        self.lbl_clean_interval = Label("cleanup interval")
        self.btn_clean = Button("clean", id="clean")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        log().debug(f"Button '{event.button.id}' pressed")
        if event.button.id == "quit":
            self.exit()

    async def action_inform_ctrlc_deactivated(self) -> None:
        """See BINDINGS"""
        log().error("CTRL-C is deactivated to avoid unintentional shutdown. Press CTRL-Q instead.")

    async def initialize(self) -> None:
        """Executed as soon as UI is ready. Called by parent().on_mount()"""
        self.update_dashboard()
        self.run_docker_stats()
        self.run_listen_messages()
        self.maintain_docker_stats_tree()
        asyncio.ensure_future(watch_fs_changes(self.global_state))
        asyncio.ensure_future(schedule_cleanup(self.global_state))
        dynamic.report(self.global_state, "info", "docker-shaper started")

    def cleanup(self):
        """Gets called on shutdown by super()"""
        self.global_state.export_references()

    def compose(self) -> ComposeResult:
        """Set up the UI"""
        with Static(id="dashboard"):

            yield self.btn_clean
            yield Button("quit", id="quit")
            #yield self.lbl_clean_interval
            yield self.lbl_event_horizon
            yield Label(f"{CONFIG_FILE.as_posix()}")
            yield self.lbl_switches
            yield self.lbl_expiration
            # todo: hostname -> link to monitoring
            yield Label(f"{get_hostname()}")
            yield Label(f"{process_output('docker --version')}")
            yield Label(f"docker-shaper v{__version__}")
            yield self.lbl_sys

        yield self.docker_stats_tree
        yield from super().compose()

    @work(exit_on_error=True)
    async def update_dashboard(self) -> None:
        """Continuously write some internal stuff to log"""
        current_process = psutil.Process()
        while True:
            tasks = [
                name
                for t in asyncio.all_tasks()
                if not (name := t.get_name()).startswith("message pump ")
            ]
            self.lbl_sys.update(
                Text.from_markup(
                    f"PID: {current_process.pid} "
                    f" | CPU: {current_process.cpu_percent()}%"
                    f" │ Tasks: {len(tasks)}"
                    f" │ Total CPU: {psutil.cpu_percent()} * {psutil.cpu_count()}%"
                )
            )
            self.lbl_event_horizon.update(
                #Text.plain(
                    f"EH: {date_str(self.global_state.docker_state.event_horizon)}"
                    f" / {age_str(datetime.now(), self.global_state.docker_state.event_horizon)}")
            self.lbl_switches.update(
                #Text.plain(
                    "\n".join(f"{key}: {markup_escape('[x]' if value else '[ ]')}"
                               for key, value in self.global_state.switches.items()))
            self.lbl_expiration.update(
                #Text.from_markup(
                    "\n".join(f"{key}: {dur_str(value)}"
                               for key, value in self.global_state.expiration_ages.items()))
            self.btn_clean.label = (
                f"Cleanup! {dur_str(self.global_state.intervals['cleanup'] - self.global_state.cleanup_fuse)}"
                f" ({dur_str(self.global_state.intervals['cleanup'])})")

            # │ started / frame:   2024.02.09-11:42:29 / 2h:13m:4s / 134
            # │ event horizon:     2024.01.20-08:54:48 / 20d:5h:0m:45s
            # rotate log level (click + kill info) `kill -USR1 2452824`
            # backtrace (click + kill info) `kill -USR2 2452824`
            # toggles: cleanup container / images / volumes / build cache
            # │ containers:        12
            # │ images:            462
            # │ volumes:           4
            # │ networks:          3
            # │ references:        185
            # │ tag_rules:         44
            # │ connections:       1
            # │ tasks:             34, missing / unknown: none /  none
            # │ initially crawled: containers: True images: True volumes: True networks: True

            # Tables:
            # containers
            # images
            # rules
            # unmatched tags

            await asyncio.sleep(3)

    @work(exit_on_error=True)
    async def run_docker_stats(self) -> None:
        """Runs the docker-stats 'daemon' in background"""
        await self.global_state.docker_state.run()

    @work(exit_on_error=True)
    async def run_listen_messages(self) -> None:
        """Async wrapper around dynamic.run_listen_messages"""
        await dynamic.run_listen_messages(self.global_state)

    @work(exit_on_error=True)
    async def maintain_docker_stats_tree(self) -> None:
        """Continuously updates Docker elements tree"""
        container_nodes = {}
        containers_node = self.docker_stats_tree.root.add("Containers", expand=True)

        image_nodes = {}
        images_node = self.docker_stats_tree.root.add("Images", expand=False)

        reference_nodes: dict[ImageIdent, TreeNode] = {}
        references_node = self.docker_stats_tree.root.add("Image-references", expand=True)

        network_nodes = {}
        networks_node = self.docker_stats_tree.root.add("Networks", expand=True)

        volume_nodes = {}
        volumes_node = self.docker_stats_tree.root.add("Volumes", expand=True)

        patterns_node = self.docker_stats_tree.root.add("Image-pattern", expand=False)

        self.docker_stats_tree.root.expand()
        self.docker_stats_tree.root.allow_expand = False

        # wait for all items to be registered
        while not all(
            (
                self.global_state.docker_state.containers_crawled,
                self.global_state.docker_state.images_crawled,
                self.global_state.docker_state.volumes_crawled,
                self.global_state.docker_state.networks_crawled,
            )
        ):
            log().info(
                "wait for initial crawls (C: %s, I: %s, V: %s, N: %s)",
                self.global_state.docker_state.containers_crawled,
                self.global_state.docker_state.images_crawled,
                self.global_state.docker_state.volumes_crawled,
                self.global_state.docker_state.networks_crawled,
            )
            await asyncio.sleep(1)

        # add all containers
        for container in self.global_state.docker_state.containers.values():
            container_nodes[container.id] = containers_node.add(f"{container}")

        # add all images
        pattern_issues = []
        for img in self.global_state.docker_state.images.values():
            img_node = image_nodes[img.id] = images_node.add(f"{img}", expand=True)
            for tag in img.tags:
                dep_age, reason = dynamic.expiration_age_from_image_name(
                    self.removal_patterns, tag, 666
                )
                reason_markup = "bold red"
                if reason in self.removal_patterns:
                    if reason not in self.pattern_usage_count:
                        self.pattern_usage_count[reason] = 0
                    self.pattern_usage_count[reason] += 1
                    reason_markup = "sky_blue2"
                else:
                    pattern_issues.append(f"{tag} # {reason}")
                img_node.add(
                    f"dep_age=[sky_blue2]{dep_age:10d}[/]"
                    f" [bold]{tag}[/] '[{reason_markup}]{reason}[/]'"
                )

        # add all volumes
        for volume in self.global_state.docker_state.volumes.values():
            volume_nodes[volume.Name] = volumes_node.add(f"{volume}")

        # add all networks
        for network in self.global_state.docker_state.networks.values():
            network_nodes[network.Id] = networks_node.add(f"{network}")

        # add all pattern
        for issue in pattern_issues:
            patterns_node.add(f"[bold red]{issue}[/]'")
        for pattern, dep_age in self.removal_patterns.items():
            usage_count = self.pattern_usage_count.get(pattern, 0)
            if usage_count == 0:
                pattern_issues.append(pattern)
            patterns_node.add(f"{usage_count:3d}: r'[sky_blue2]{pattern}[/]'")
            # network_nodes[network.Id] = networks_node.add(f"{network}")

        with (dynamic.BASE_DIR / "pattern-issues.txt").open("w", encoding="utf-8") as issues_file:
            issues_file.write("\n".join(pattern_issues))

        patterns_node.set_label(f"Image-pattern ({len(self.removal_patterns)})")

        async for mtype, mtext, mobj in self.global_state.docker_state.wait_for_change():
            self.docker_stats_tree.root.set_label(
                f"{get_hostname()}"
                f" / horizon={date_str(self.global_state.docker_state.event_horizon)}"
                f" ({dur_str(int(time.time()) - self.global_state.docker_state.event_horizon)})"
            )

            if mtype == "exception":
                log().exception("%s: %s", mtext, mobj)

            elif mtype == "error":
                log().error(mtext)

            elif mtype == "warning":
                log().warning(mtext)

            elif mtype == "info":
                log().info(mtext)

            elif mtype == "client_disconnect":
                raise SystemExit(1)

            elif mtype in {"container_add", "container_del", "container_update"}:
                cnt: Container = cast(Container, mobj)
                log().info(
                    "container info: '%s' / %s (%d total)",
                    cnt.short_id,
                    mtype,
                    len(self.global_state.docker_state.containers),
                )
                if mtype == "container_add" and cnt.id not in container_nodes:
                    container_nodes[cnt.id] = containers_node.add(f"{cnt}")
                if mtype == "container_update":
                    container_nodes[cnt.id].set_label(container_markup(cnt))
                if mtype == "container_del" and cnt.id in container_nodes:
                    container_nodes[cnt.id].remove()
                    del container_nodes[cnt.id]

                total_cpu = sum(
                    map(lambda c: c.cpu_usage(), self.global_state.docker_state.containers.values())
                )
                total_mem = sum(
                    map(lambda c: c.mem_usage(), self.global_state.docker_state.containers.values())
                )
                containers_node.set_label(
                    f"Containers ({len(self.global_state.docker_state.containers):2d})"
                    f" {' ' * 56} [bold]{total_cpu * 100:7.2f}% - {total_mem >> 20:6d}MiB[/]"
                )

            elif mtype in {"image_add", "image_del", "image_update"}:
                image_id = mtext

                log().info(
                    "image info: '%s' / %s (%d total)",
                    short_id(image_id),
                    mtype,
                    len(self.global_state.docker_state.images),
                )
                if mtype == "image_del":
                    if image_id in image_nodes:
                        image_nodes[image_id].remove()
                        del image_nodes[image_id]
                    continue
                image = self.global_state.docker_state.images[image_id]
                if mtype == "image_add" and image.id not in image_nodes:
                    image_nodes[image.id] = images_node.add(f"{image}")
                if mtype == "image_update":
                    image_nodes[image.id].set_label(f"{image} - +")

                images_node.set_label(f"Images ({len(self.global_state.docker_state.images)})")

            elif mtype in {"volume_add", "volume_del"}:
                volume_id = mtext

                log().info(
                    "volume info: '%s' / %s (%d total)",
                    short_id(volume_id),
                    mtype,
                    len(self.global_state.docker_state.volumes),
                )
                if mtype == "volume_add" and volume_id not in volume_nodes:
                    vol: Volume = cast(Volume, mobj)
                    volume_nodes[volume_id] = volumes_node.add(f"{vol}")
                if mtype == "volume_del":
                    if volume_id in volume_nodes:
                        volume_nodes[volume_id].remove()
                        del volume_nodes[volume_id]
                volumes_node.set_label(f"Volumes ({len(self.global_state.docker_state.volumes)})")

            elif mtype in {"network_add", "network_del"}:
                network_id = mtext

                log().info(
                    "network info: '%s' / %s (%d total)",
                    short_id(network_id),
                    mtype,
                    len(self.global_state.docker_state.networks),
                )
                if mtype == "network_add" and network_id not in network_nodes:
                    netw: Network = cast(Network, mobj)
                    network_nodes[network_id] = networks_node.add(f"{netw}")
                if mtype == "network_del":
                    if network_id in network_nodes:
                        network_nodes[network_id].remove()
                        del network_nodes[network_id]
                networks_node.set_label(
                    f"Networks ({len(self.global_state.docker_state.networks)})"
                )

            elif mtype in {"reference_update", "reference_del"}:
                ident = cast(ImageIdent, mobj)
                log().info(
                    "reference updated: %s (%d total)",
                    ident,
                    len(self.global_state.docker_state.last_referenced),
                )
                if mtype == "reference_update":
                    if mtype in reference_nodes:
                        reference_nodes[ident].set_label(
                            f"{ident} - {self.global_state.docker_state.last_referenced[ident]} - +"
                        )
                    else:
                        reference_nodes[ident] = references_node.add(
                            f"{ident} - {self.global_state.docker_state.last_referenced[ident]}"
                        )
                if mtype == "reference_del" and ident in reference_nodes:
                    reference_nodes[ident].remove()
                    del reference_nodes[ident]

            else:
                log().error("don't know message type %s", mtype)


def main() -> None:
    """Main entry point"""
    logging.getLogger().setLevel(logging.WARNING)
    log().setLevel(logging.DEBUG)
    dynamic.setup_introspection()
    DockerShaper().execute()


if __name__ == "__main__":
    main()
