import matplotlib.pyplot as plt


def compare_benchmarks(*benchmarks):
    for benchmark in benchmarks:
        plt.plot(benchmark["times"], label=benchmark["name"])

    plt.xlabel("Iteration")
    plt.ylabel("Time (seconds)")
    plt.legend()

    names = ", ".join([benchmark["name"] for benchmark in benchmarks])

    plt.title(f"Performance Results for {names}")
    plt.show()


def compare_statistics_benchmarks(*benchmarks):
    metrics = ["mean", "median", "minimum", "maximum"]
    num_metrics = len(metrics)
    num_benchmarks = len(benchmarks)

    _, axs = plt.subplots(num_metrics // 2, 2, figsize=(10, 10))
    plt.title(f"Statistical comparison for {num_benchmarks} benchmarks")

    for i, metric in enumerate(metrics):

        for benchmark in benchmarks:
            row = i // 2
            col = i % 2

            values = [benchmark[metric]]
            names = [benchmark["name"]]

            axs[row, col].bar(names, values)
            axs[row, col].set_ylabel(metric.capitalize() + " time (seconds)")

    plt.show()
