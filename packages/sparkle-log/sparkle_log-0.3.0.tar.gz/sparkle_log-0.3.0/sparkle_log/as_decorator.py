"""
This module contains the decorator to monitor the metrics of the system while the function is being executed.
"""

import logging
from functools import wraps
from threading import Event, Thread

from sparkle_log.graphs import GLOBAL_LOGGER
from sparkle_log.scheduler import run_scheduler
from sparkle_log.ui import GraphStyle

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

        return wrapper

    return decorator
