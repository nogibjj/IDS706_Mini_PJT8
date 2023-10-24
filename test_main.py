import pandas as pd
import time
import psutil
from main import compute_statistics


def test_compute_statistics():
    start_time = time.time()
    df = pd.read_csv("heightweight.csv", sep=";")
    stats = compute_statistics(df, "Height")

    assert "mean" in stats, "Mean not computed"
    assert "median" in stats, "Median not computed"
    assert "std" in stats, "Standard deviation not computed"
    assert "size" in stats, "Size not computed"
    end_time = time.time()
    # print("All compute_statistics checks passed.")

    end_time = time.time()

    elapsed_time = end_time - start_time
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()

    print(f"Elapsed time: {elapsed_time:.4f} seconds")
    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_info.percent}%")


if __name__ == "__main__":
    test_compute_statistics()
