import json
from carla.driving_benchmark.results_printer import print_summary

with open('../_benchmarks_results/outputs-27/metrics.json') as json_file:
    metrics_summary = json.load(json_file)

    train_weathers = [1, 3, 6, 8]
    test_weathers = [4, 14]

    print("Printing Data\n")
    print_summary(metrics_summary, test_weathers, None)
    print("\nDone Printing Data")

