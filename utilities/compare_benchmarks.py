import matplotlib.pyplot as plt
import textwrap

def compare_benchmarks(*benchmarks):
    """
    Plots the performance results of multiple benchmarks.

    Parameters
    ----------
    *benchmarks : list of dict
        A list of dictionaries, where each dictionary represents a benchmark.
        The required keys for each dictionary are "name" (the name of the benchmark)
        and "times" (a list of times for each iteration of the benchmark).

    Returns
    -------
    None

    """
    for benchmark in benchmarks:
        plt.plot(benchmark["times"], label=benchmark["name"])

    plt.xlabel("Iteration")
    plt.ylabel("Time (seconds)")
    plt.legend()

    names = ", ".join([benchmark["name"] for benchmark in benchmarks])

    plt.title(f"Performance Results for {names}")
    plt.show()


def compare_statistics_benchmarks(*benchmarks):
    """
    Compares the statistical metrics of multiple benchmarks.

    Parameters
    ----------
    *benchmarks : list of dict
        A list of dictionaries, where each dictionary represents a benchmark.
        The required keys for each dictionary are "name" (the name of the benchmark)
        and the statistical metrics of interest (e.g., "mean", "median", etc.).

    Returns
    -------
    None

    """
    metrics = ["mean", "median", "minimum", "maximum"]
    num_metrics = len(metrics)
    num_benchmarks = len(benchmarks)

    fig, axs = plt.subplots(num_metrics // 2, 2, figsize=(12, 12))
    fig.suptitle(f"Statistical comparison for {num_benchmarks} benchmarks")

    for i, metric in enumerate(metrics):
        row = i // 2
        col = i % 2

        names = [benchmark["name"] for benchmark in benchmarks]
        values = [benchmark[metric] for benchmark in benchmarks]

        for j, benchmark in enumerate(benchmarks):
            color = plt.cm.get_cmap("tab10")(j)  # Use different colors for each benchmark
            axs[row, col].bar(names[j], values[j], label=benchmark["name"], color=color)

        # Wrap long labels onto multiple lines with a width of 10 characters
        axs[row, col].set_xticklabels([textwrap.fill(label, width=10) for label in names])

        axs[row, col].set_ylabel(metric.capitalize() + " time (seconds)")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout for the suptitle
    plt.show()