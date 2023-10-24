# import psutil
from mylib.lib import compute_statistics
import pandas as pd

# import time


def main():
    # start_time = time.time()

    # Load the dataset
    df = pd.read_csv("heightweight.csv", sep=",")

    column_name = "Height"

    if column_name in df.columns:
        stats = compute_statistics(df, column_name)

        # Print the computed statistics
        print(f"Statistics for column '{column_name}':")
        print(f"Mean: {stats['mean']:.2f}")
        print(f"Median: {stats['median']:.2f}")
        print(f"Standard Deviation: {stats['std']:.2f}")
        print(f"Size: {stats['size']}")
    else:
        print(f"Column '{column_name}' not found in the dataset.")

    # end_time = time.time()
    # print(f"Execution time: {end_time - start_time:.2f} seconds")
    # process = psutil.Process()
    # memory_usage = process.memory_info().rss / (1024**2)  # Convert bytes to MB
    # print(f"Memory usage: {memory_usage:.2f} MB")


if __name__ == "__main__":
    main()
