from typing import Callable, Any
import time
import statistics

from config import ITERATION_COUNT


ITERATIONS = ITERATION_COUNT


def benchmark(func: Callable[..., Any], *args: Any, **kwargs: Any) -> dict:
    """
    Runs the given function a specified number of times and returns a dictionary containing the performance statistics.

    Args:
        func (Callable[..., Any]): The function to be benchmarked.
        *args: Positional arguments to be passed to the function.
        **kwargs: Keyword arguments to be passed to the function.

    Returns:
        dict: A dictionary containing the performance statistics, including the function name, number of iterations, mean, maximum, minimum, and median execution times.
    """
    performance_result = {
        "name": func.__name__,
        "times": [],
        "iterations": ITERATIONS,
        "mean": 0,
        "maximum": 0,
        "minimum": 0,
        "median": 0,
    }

    for i in range(0, ITERATIONS):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        performance_result["times"].append(end_time - start_time)

    performance_result = _calculate_statistics(performance_result)

    return performance_result


def _calculate_statistics(performance_statistics: dict) -> dict:
    """
    Calculates the mean, maximum, minimum, and median of a list of times.

    Args:
        performance_statistics (dict): A dictionary containing the times and other performance statistics.

    Returns:
        dict: A dictionary containing the mean, maximum, minimum, and median of the times.
    """
    performance_statistics["mean"] = statistics.mean(
        performance_statistics["times"]
    )

    performance_statistics["maximum"] = max(performance_statistics["times"])

    performance_statistics["minimum"] = min(performance_statistics["times"])

    performance_statistics["median"] = statistics.median(
        performance_statistics["times"]
    )

    return performance_statistics
