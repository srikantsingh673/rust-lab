import project_01
import time

start = time.time()
res_01 = project_01.heavy_computation(10**7)
print("Math test done in:", time.time() - start, "seconds")

start = time.time()
res_02 = project_01.heavy_string_processing(10**5)
print("String processing done in:", time.time() - start, "seconds")

start = time.time()
res_03 = project_01.heavy_list_manipulation(10**5)
print("List manipulation done in:", time.time() - start, "seconds")

start = time.time()
res_04 = project_01.heavy_file_io(10**5, "rs_output.txt")
print("File I/O done in:", time.time() - start, "seconds")