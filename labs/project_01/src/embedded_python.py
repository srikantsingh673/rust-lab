import project_01
import timeit
import csv


csv_path = "output/result.csv"
results = []
number = 1

math_time = timeit.timeit(lambda: project_01.arithmetic_operations(10**8), number=number)
print(f"Math test done in: {math_time} seconds")
results.append(["Rust", "arithmetic_operations", math_time])

string_time = timeit.timeit(lambda: project_01.string_processing(10**6), number=number)
print(f"String processing done in: {string_time} seconds")
results.append(["Rust", "string_processing", string_time])

list_time = timeit.timeit(lambda: project_01.list_manipulation(10**6), number=number)
print(f"List manipulation done in: {list_time} seconds")
results.append(["Rust", "list_manipulation", list_time])


fileio_time = timeit.timeit(lambda: project_01.file_io(10**6, "output/rs_output.txt"), number=number)
print(f"File I/O done in: {fileio_time} seconds")
results.append(["Rust", "file_io", fileio_time])

# Conditional if-else speed test
cond_time = timeit.timeit(lambda: [project_01.number_to_name(i % 101) for i in range(10**7)], number=number)
print(f"Conditional if-else test done in: {cond_time} seconds")
results.append(["Rust", "number_to_name", cond_time])

# Write results to CSV
with open(csv_path, mode="a", newline="") as csvfile:
		writer = csv.writer(csvfile)
		# Write header if file is empty
		csvfile.seek(0, 2)
		if csvfile.tell() == 0:
			writer.writerow(["Implementation", "Function", "Time (seconds)"])
		for row in results:
			writer.writerow(row)