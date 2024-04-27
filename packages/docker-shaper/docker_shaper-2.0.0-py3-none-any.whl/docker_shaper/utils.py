#!/usr/bin/env python3

"""Common stuff shared among modules"""

import asyncio
import logging
import os

# import re
import signal
import sys
import time
import traceback

# from datetime import datetime
from functools import wraps
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType

# from dateutil import tz
from rich.logging import RichHandler
from rich.markup import escape as markup_escape

from docker_shaper.dynamic import Container, short_id

# LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")


def log() -> logging.Logger:
    """Logger for this module"""
    return logging.getLogger("docker-shaper")


# def stack_str(depth: int = 0):
# def stack_fns():
# stack = list(
# reversed(
# traceback.extract_stack(sys._getframe(depth))  # pylint: disable=protected-access
# )
# )

# for site in stack:
# if site.filename != stack[0].filename or site.name == "<module>":
# break
# yield site.name

# return ">".join(reversed(list(stack_fns())))


# def setup_logging(level: str = "INFO") -> None:
# """Make logging fun"""

# class CustomLogger(logging.getLoggerClass()):
# """Logger with stack information"""

# def makeRecord(  # pylint: disable=too-many-arguments
# self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None
# ):
# if extra is None:
# extra = {}
# extra["stack"] = stack_str(5)
# return super().makeRecord(name, level, fn, lno, msg, args, exc_info, func, extra, sinfo)

# logging.setLoggerClass(CustomLogger)

# logging.getLogger().setLevel(logging.WARNING)
# log().setLevel(getattr(logging, level.split("_")[-1]))
## logging.getLogger("urllib3.connectionpool")
# ch = RichHandler(show_path=False, markup=True, show_time=False)
# ch.setLevel(getattr(logging, level.split("_")[-1]))
# ch.setFormatter(
# logging.Formatter(
# "│ %(asctime)s │ [grey]%(stack)-55s[/] │ [bold white]%(message)s[/]",
# datefmt="%Y-%m-%d %H:%M:%S",
# )
# )
# log().handlers = [ch]
# logging.getLogger("urllib3.connectionpool").setLevel(logging.INFO)

# def markup_escaper(record: logging.LogRecord) -> bool:
# record.args = record.args and tuple(
# markup_escape(arg) if isinstance(arg, str) else arg for arg in record.args
# )
# record.msg = markup_escape(record.msg)
# return True

# ch.addFilter(markup_escaper)

## https://stackoverflow.com/questions/76788727/how-can-i-change-the-debug-level-and-format-for-the-quart-i-e-hypercorn-logge
## https://pgjones.gitlab.io/hypercorn/how_to_guides/logging.html#how-to-log
## https://www.phind.com/agent?cache=clkqhh48y001smg0832tvq1rl

## from quart.logging import default_handler
## logging.getLogger('quart.app').removeHandler(default_handler)
## logger = logging.getLogger("hypercorn.error")
## logger.removeHandler(default_handler)
## logger.addHandler(ch)
## logger.setLevel(logging.WARNING)
## logger.propagate = False


def impatient(func):
    """Tells us, when a function takes suspiciously long"""

    @wraps(func)
    def run(*args: object, **kwargs: object) -> object:
        t1 = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            if (duration := time.time() - t1) > 0.2:
                log().warning("%s took %.2fs!", func.__name__, duration)

    return run


def aimpatient(func):
    """Tells us, when a function takes suspiciously long"""

    @wraps(func)
    async def run(*args: object, **kwargs: object) -> object:
        t1 = time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            if (duration := time.time() - t1) > 0.1:
                log().warning("%s took %.2fs!", func.__name__, duration)

    return run


def increase_loglevel(*_):
    """Become one level more verbose.
    If level is already DEBUG we go back to WARNING.
    """
    try:
        new_level = {
            logging.WARNING: logging.INFO,
            logging.INFO: logging.DEBUG,
            logging.DEBUG: logging.WARNING,
        }.get(log().level) or logging.INFO

        log().setLevel(new_level)
        logging.getLogger("docker-shaper.server").setLevel(new_level)
        level = {
            logging.CRITICAL: "CRITICAL",
            logging.ERROR: "ERROR",
            logging.WARNING: "WARNING",
            logging.INFO: "INFO",
            logging.DEBUG: "DEBUG",
        }[new_level]
        print(f"increase_loglevel to {level}", file=sys.stderr)
    except Exception:  # pylint: disable=broad-except
        log().exception("Could not fully write application stack trace")


def print_stacktrace_on_signal(sig, frame):
    """interrupt running process, and provide a python prompt for
    interactive debugging.
    see http://stackoverflow.com/questions/132058
       "showing-the-stack-trace-from-a-running-python-application"
    """
    try:
        print(f"signal {sig} received - print stack trace", file=sys.stderr)

        def print_stack_frame(stack_frame, file):
            for _f in traceback.format_stack(stack_frame):
                for _l in _f.splitlines():
                    print(_l, file=file)

        def print_stack_frames(file):
            print("++++++ MAIN ++++++++", file=file)
            print_stack_frame(frame, file)
            for task in asyncio.all_tasks():
                print(f"++++++ {task.get_coro().__name__} ++++++++", file=file)
                for stack in task.get_stack(limit=1000):
                    print_stack_frame(stack, file)

        print_stack_frames(sys.stderr)
        with open(
            Path("~/.docker_shaper/traceback.log").expanduser(), "w", encoding="utf-8"
        ) as trace_file:
            print_stack_frames(trace_file)
            print(f"traceback also written to {trace_file}", file=sys.stderr)
    except Exception:  # pylint: disable=broad-except
        log().exception("Could not fully write application stack trace")


def setup_introspection_on_signal():
    """Install signal handlers for some debug stuff"""

    def setup_signal(sig, func, msg):
        signal.signal(sig, func)
        signal.siginterrupt(sig, False)
        sig_str = {signal.SIGUSR1: "USR1", signal.SIGUSR2: "USR2"}.get(sig, sig)
        print(f"Run `kill -{sig_str} {os.getpid()}` to {msg}", file=sys.stderr)

    setup_signal(signal.SIGUSR1, increase_loglevel, "increase log level")
    setup_signal(signal.SIGUSR2, print_stacktrace_on_signal, "print stacktrace")


def load_module(path: Path) -> ModuleType:
    """Loads a module from a file path"""
    spec = spec_from_file_location("dynamic_config", path)
    if not (spec and spec.loader):
        raise RuntimeError("Could not load")
    module = module_from_spec(spec)
    assert module
    # assert isinstance(spec.loader, SourceFileLoader)
    loader: SourceFileLoader = spec.loader
    loader.exec_module(module)
    return module


def get_hostname() -> str:
    """Returns local hostname read from /etc/hostname"""
    with open("/etc/hostname", encoding="utf-8") as hostname_file:
        return hostname_file.read().strip()


def container_markup(container: Container) -> str:
    status_markups = {"running": "cyan bold"}
    image_str, status_str = (
        ("", "")
        if not container.show
        else (
            f" image:[bold]{short_id(container.show.Image)}[/]",
            f" - [{status_markups.get(container.show.State.Status, 'grey53')}]"
            f"{container.show.State.Status:7s}[/]",
        )
    )
    return (
        f"[bold]{container.short_id}[/] / {container.name:<26s}{image_str}{status_str}"
        f" - {container.cpu_usage() * 100:7.2f}%"
        f" - {container.mem_usage() >> 20:6d}MiB"
    )
