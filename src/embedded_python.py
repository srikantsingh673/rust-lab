import rust_lab
import timeit
import random
import time
import csv
import os

random.seed(42)

def benchmark_func(func, *args, repeats=20):
    func(*args)  # warm-up
    times = timeit.repeat(lambda: func(*args), repeat=repeats, number=1)
    mean_time = sum(times) / len(times)
    stddev = (sum((t - mean_time) ** 2 for t in times) / len(times)) ** 0.5
    return mean_time, stddev

def unique_filename(prefix="output", suffix=".txt"):
    return f"{prefix}_{int(time.time() * 1000)}{suffix}"

if __name__ == "__main__":
    csv_path = "output/result_rust.csv"

    if os.path.exists(csv_path):
        os.remove(csv_path)

    results = []

    mean_time, stddev = benchmark_func(rust_lab.arithmetic_operations, 10**7)
    print(f"Math test done in: {mean_time:.4f} s (stddev {stddev:.4f})")
    results.append(["Rust", "arithmetic_operations", mean_time, stddev])

    mean_time, stddev = benchmark_func(rust_lab.string_processing, 10**5)
    print(f"String processing done in: {mean_time:.4f} s (stddev {stddev:.4f})")
    results.append(["Rust", "string_processing", mean_time, stddev])

    mean_time, stddev = benchmark_func(rust_lab.list_manipulation, 10**5)
    print(f"List manipulation done in: {mean_time:.4f} s (stddev {stddev:.4f})")
    results.append(["Rust", "list_manipulation", mean_time, stddev])

    fname = unique_filename("output/rs_output", ".txt")
    mean_time, stddev = benchmark_func(rust_lab.file_io, 10**5, fname)
    print(f"File I/O done in: {mean_time:.4f} s (stddev {stddev:.4f})")
    results.append(["Rust", "file_io", mean_time, stddev])

    mean_time, stddev = benchmark_func(lambda: [rust_lab.number_to_name(i % 101) for i in range(10**7)])
    print(f"Conditional if-else test done in: {mean_time:.4f} s (stddev {stddev:.4f})")
    results.append(["Rust", "number_to_name", mean_time, stddev])

    with open(csv_path, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Implementation", "Function", "Mean Time (seconds)", "Std Dev"])
        for row in results:
            writer.writerow(row)
