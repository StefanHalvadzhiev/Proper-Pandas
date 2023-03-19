from typing import Callable, Any
import time
import statistics

from config import ITERATION_COUNT


def benchmark(func: Callable[..., Any], *args: Any, **kwargs: Any):
    performance_result = {
        "name": func.__name__,
        "times": [],
        "iterations": ITERATION_COUNT,
        "mean": 0,
        "maximum": 0,
        "minimum": 0,
        "median": 0,
    }

    for i in range(0, ITERATION_COUNT):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        performance_result["times"].append(end_time - start_time)

    performance_result = _calculate_statistics(performance_result)

    return performance_result


def _calculate_statistics(performance_statistics):
    performance_statistics["mean"] = statistics.mean(
        performance_statistics["times"]
    )

    performance_statistics["maximum"] = max(performance_statistics["times"])

    performance_statistics["minimum"] = min(performance_statistics["times"])

    performance_statistics["median"] = statistics.median(
        performance_statistics["times"]
    )

    return performance_statistics
