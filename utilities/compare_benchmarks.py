import matplotlib.pyplot as plt


def compare_benchmarks(benchmark1, benchmark2):
    plt.plot(benchmark1["times"], label=benchmark1["name"])
    plt.plot(benchmark2["times"], label=benchmark2["name"])
    plt.xlabel("Iteration")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.title(f"Performance Results for {benchmark1['name']} and {benchmark2['name']}")
    plt.show()


def compare_statistics_benchmarks(benchmark1, benchmark2):
    metrics = ["mean", "maximum", "minimum", "median"]
    _, axs = plt.subplots(2, 2, figsize=(10, 10))

    for i, metric in enumerate(metrics):
        value1 = benchmark1[metric]
        value2 = benchmark2[metric]
        row = i // 2
        col = i % 2

        axs[row, col].bar([benchmark1["name"], benchmark2["name"]], [value1, value2])
        axs[row, col].set_ylabel(metric.capitalize() + ' time (seconds)')

    plt.title(f"Statistical comparison for for {benchmark1['name']} and {benchmark2['name']}")
    plt.show()
