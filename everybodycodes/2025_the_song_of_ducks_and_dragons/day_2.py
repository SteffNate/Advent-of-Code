from pprint import pprint
import ast
import numpy as np
from numpy.typing import NDArray

# part 1
with open("inputs/everybody_codes_e2025_q02_p1.txt", "r") as f:
    file = f.read()
    numbers: list[int] = ast.literal_eval(file.split("=")[1])


def add_instruction(x: list[int], y: list[int]) -> list[int]:
    return [x[0] + y[0], x[1] + y[1]]


def multiply_instruction(x: list[int], y: list[int]) -> list[int]:
    return [x[0] * y[0] - x[1] * y[1], x[0] * y[1] + y[0] * x[1]]


def division_instruction(x: list[int], y: list[int]) -> list[int]:
    if all(n == 0 for n in x):
        return [0, 0]
    return [x[0] // y[0], x[1] // y[1]]


baseline = [0, 0]
A: list[int] = numbers

n_iterations = 3
for i in range(n_iterations):
    # Multiply the result by itself.
    # Divide the result by  [10,10] .
    # Add  A  to the result.
    baseline = multiply_instruction(baseline, baseline)
    baseline = division_instruction(baseline, [10, 10])
    baseline = add_instruction(baseline, A)
print(baseline)

# part 2

with open("inputs/everybody_codes_e2025_q02_p2.txt", "r") as f:
    file = f.read()
    numbers: list[int] = ast.literal_eval(file.split("=")[1])

print(numbers)
a = np.array(numbers)
bottom_corner = np.add(a, [1000, 1000])

number_of_dots = 101 * 101
point_map = np.linspace(a, bottom_corner, num=number_of_dots)
xd = np.linspace(a[0], bottom_corner[0], 101)
yd = np.linspace(a[1], bottom_corner[1], 101)
x_mat, y_mat = np.meshgrid(xd, yd)


def single_cycle(coordinate):
    result = [0, 0]

    for _ in range(100):
        result = [
            result[0] * result[0] - result[1] * result[1],
            result[0] * result[1] + result[1] * result[0],
        ]

        result = division_instruction(result, [100_000, 100_000])

        result = np.add(result, coordinate)

        for i in result:
            if abs(i) > 1_000_000:
                return False

    return True
