"""
This module contains the decorator to monitor the metrics of the system while the function is being executed.
"""

import logging
from asyncio import iscoroutinefunction
from functools import wraps
from threading import Event, Thread

from sparkle_log.custom_types import GraphStyle
from sparkle_log.graphs import GLOBAL_LOGGER
from sparkle_log.scheduler import run_scheduler

INITIALIZED = False


def monitor_metrics_on_call(metrics=("cpu", "memory"), interval=10, style: GraphStyle = "bar"):
    """
    Decorator to monitor the system metrics while the function is being executed.
    """

    def decorator(func):
        """Wrapper function"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            """Wrapper function"""
            if not GLOBAL_LOGGER.isEnabledFor(logging.INFO):
                return func(*args, **kwargs)
            stop_event = Event()
            scheduler_thread = Thread(target=run_scheduler, args=(stop_event, metrics, interval, style))
            scheduler_thread.start()

            try:
                return func(*args, **kwargs)
            finally:
                # Stop the scheduler and wait for thread to finish
                stop_event.set()

                scheduler_thread.join()

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            """Wrapper function"""
            if not GLOBAL_LOGGER.isEnabledFor(logging.INFO):
                return func(*args, **kwargs)
            stop_event = Event()
            scheduler_thread = Thread(target=run_scheduler, args=(stop_event, metrics, interval, style))
            scheduler_thread.start()

            try:
                return await func(*args, **kwargs)
            finally:
                # Stop the scheduler and wait for thread to finish
                stop_event.set()

                scheduler_thread.join()

        return async_wrapper if iscoroutinefunction(func) else wrapper

    return decorator
