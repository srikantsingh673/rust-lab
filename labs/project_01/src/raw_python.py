import random
import string
import time

# --------------------------
# 1. Heavy mathematical computation
# --------------------------
def heavy_computation(x: int) -> int:
    """
    Sum of squares from 0 to x.
    """
    return sum(n * n for n in range(x + 1))


# --------------------------
# 2. Heavy string processing
# --------------------------
def heavy_string_processing(n: int) -> str:
    """
    Concatenate and reverse random strings n times.
    """
    result = ""
    letters = string.ascii_letters
    for _ in range(n):
        rand_str = ''.join(random.choices(letters, k=100))
        result += rand_str[::-1]  # reverse string
    return result


# --------------------------
# 3. Large list manipulation
# --------------------------
def heavy_list_manipulation(n: int) -> list:
    """
    Generate list of n random numbers, sort and filter even numbers.
    """
    numbers = [random.randint(0, 1000) for _ in range(n)]
    numbers.sort()
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


# --------------------------
# 4. File I/O heavy test
# --------------------------
def heavy_file_io(n: int, filename: str = "py_output.txt") -> None:
    """
    Write and read large file n times.
    """
    with open(filename, "w") as f:
        for _ in range(n):
            line = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
            f.write(line + "\n")
    # Read back
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


# --------------------------
# Example usage with timing
# --------------------------
if __name__ == "__main__":
    start = time.time()
    heavy_computation(10**7)
    print("Math test done in:", time.time() - start, "seconds")

    start = time.time()
    heavy_string_processing(10**5)
    print("String processing done in:", time.time() - start, "seconds")

    start = time.time()
    heavy_list_manipulation(10**5)
    print("List manipulation done in:", time.time() - start, "seconds")

    start = time.time()
    heavy_file_io(10**5)
    print("File I/O done in:", time.time() - start, "seconds")
