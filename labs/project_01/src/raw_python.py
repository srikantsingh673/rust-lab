import random
import string
import timeit
import csv

# --------------------------
# 1. Heavy mathematical computation
# --------------------------
def heavy_computation(x: int) -> int:
    """
    Sum of squares from 0 to x.
    """
    return sum(n * n for n in range(x + 1))

def arithmetic_operations(x: int) -> float:
    """
    Perform a complex arithmetic calculation using +, -, *, /, % for each n in 1..x.
    """
    result = 0
    for n in range(1, x + 1):
        value = (((n * 3) + 7) - 4) / 2 % 5
        result += value
    return result


# --------------------------
# 2. Heavy string processing
# --------------------------
def string_processing(n: int) -> str:
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

def list_manipulation(n: int) -> list:
    """
    Generate list of n random numbers, sort and filter even numbers.
    """
    numbers = [random.randint(0, 1000) for _ in range(n)]
    numbers.sort()
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# --------------------------
# 5. Conditional if-else speed test
# --------------------------
def number_to_name(n: int) -> str:
    """
    Return the English name of a number from 0 to 100 using if-else chain.
    """
    if n == 0:
        return "zero"
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 10:
        return "ten"
    elif n == 11:
        return "eleven"
    elif n == 12:
        return "twelve"
    elif n == 13:
        return "thirteen"
    elif n == 14:
        return "fourteen"
    elif n == 15:
        return "fifteen"
    elif n == 16:
        return "sixteen"
    elif n == 17:
        return "seventeen"
    elif n == 18:
        return "eighteen"
    elif n == 19:
        return "nineteen"
    elif n == 20:
        return "twenty"
    elif n == 21:
        return "twenty-one"
    elif n == 22:
        return "twenty-two"
    elif n == 23:
        return "twenty-three"
    elif n == 24:
        return "twenty-four"
    elif n == 25:
        return "twenty-five"
    elif n == 26:
        return "twenty-six"
    elif n == 27:
        return "twenty-seven"
    elif n == 28:
        return "twenty-eight"
    elif n == 29:
        return "twenty-nine"
    elif n == 30:
        return "thirty"
    elif n == 31:
        return "thirty-one"
    elif n == 32:
        return "thirty-two"
    elif n == 33:
        return "thirty-three"
    elif n == 34:
        return "thirty-four"
    elif n == 35:
        return "thirty-five"
    elif n == 36:
        return "thirty-six"
    elif n == 37:
        return "thirty-seven"
    elif n == 38:
        return "thirty-eight"
    elif n == 39:
        return "thirty-nine"
    elif n == 40:
        return "forty"
    elif n == 41:
        return "forty-one"
    elif n == 42:
        return "forty-two"
    elif n == 43:
        return "forty-three"
    elif n == 44:
        return "forty-four"
    elif n == 45:
        return "forty-five"
    elif n == 46:
        return "forty-six"
    elif n == 47:
        return "forty-seven"
    elif n == 48:
        return "forty-eight"
    elif n == 49:
        return "forty-nine"
    elif n == 50:
        return "fifty"
    elif n == 51:
        return "fifty-one"
    elif n == 52:
        return "fifty-two"
    elif n == 53:
        return "fifty-three"
    elif n == 54:
        return "fifty-four"
    elif n == 55:
        return "fifty-five"
    elif n == 56:
        return "fifty-six"
    elif n == 57:
        return "fifty-seven"
    elif n == 58:
        return "fifty-eight"
    elif n == 59:
        return "fifty-nine"
    elif n == 60:
        return "sixty"
    elif n == 61:
        return "sixty-one"
    elif n == 62:
        return "sixty-two"
    elif n == 63:
        return "sixty-three"
    elif n == 64:
        return "sixty-four"
    elif n == 65:
        return "sixty-five"
    elif n == 66:
        return "sixty-six"
    elif n == 67:
        return "sixty-seven"
    elif n == 68:
        return "sixty-eight"
    elif n == 69:
        return "sixty-nine"
    elif n == 70:
        return "seventy"
    elif n == 71:
        return "seventy-one"
    elif n == 72:
        return "seventy-two"
    elif n == 73:
        return "seventy-three"
    elif n == 74:
        return "seventy-four"
    elif n == 75:
        return "seventy-five"
    elif n == 76:
        return "seventy-six"
    elif n == 77:
        return "seventy-seven"
    elif n == 78:
        return "seventy-eight"
    elif n == 79:
        return "seventy-nine"
    elif n == 80:
        return "eighty"
    elif n == 81:
        return "eighty-one"
    elif n == 82:
        return "eighty-two"
    elif n == 83:
        return "eighty-three"
    elif n == 84:
        return "eighty-four"
    elif n == 85:
        return "eighty-five"
    elif n == 86:
        return "eighty-six"
    elif n == 87:
        return "eighty-seven"
    elif n == 88:
        return "eighty-eight"
    elif n == 89:
        return "eighty-nine"
    elif n == 90:
        return "ninety"
    elif n == 91:
        return "ninety-one"
    elif n == 92:
        return "ninety-two"
    elif n == 93:
        return "ninety-three"
    elif n == 94:
        return "ninety-four"
    elif n == 95:
        return "ninety-five"
    elif n == 96:
        return "ninety-six"
    elif n == 97:
        return "ninety-seven"
    elif n == 98:
        return "ninety-eight"
    elif n == 99:
        return "ninety-nine"
    elif n == 100:
        return "one hundred"
    else:
        return "out of range"


# --------------------------
# 4. File I/O heavy test
# --------------------------
def file_io(n: int, filename: str = "output/py_output.txt") -> None:
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
    csv_path = "output/result.csv"
    results = []
    number = 1

    math_time = timeit.timeit(lambda: arithmetic_operations(10**8), number=number)
    print(f"Math test done in: {math_time} seconds")
    results.append(["Python", "arithmetic_operations", math_time])

    string_time = timeit.timeit(lambda: string_processing(10**6), number=number)
    print(f"String processing done in: {string_time} seconds")
    results.append(["Python", "string_processing", string_time])

    list_time = timeit.timeit(lambda: list_manipulation(10**6), number=number)
    print(f"List manipulation done in: {list_time} seconds")
    results.append(["Python", "list_manipulation", list_time])


    fileio_time = timeit.timeit(lambda: file_io(10**6), number=number)
    print(f"File I/O done in: {fileio_time} seconds")
    results.append(["Python", "file_io", fileio_time])

    # Conditional if-else speed test
    cond_time = timeit.timeit(lambda: [number_to_name(i % 101) for i in range(10**7)], number=number)
    print(f"Conditional if-else test done in: {cond_time} seconds")
    results.append(["Python", "number_to_name", cond_time])

    # Write results to CSV
    with open(csv_path, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write header if file is empty
        csvfile.seek(0, 2)
        if csvfile.tell() == 0:
            writer.writerow(["Implementation", "Function", "Time (seconds)"])
        for row in results:
            writer.writerow(row)
