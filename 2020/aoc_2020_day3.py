from pprint import pprint
from math import prod

repeat_n = 100

with open("inputs/input_3.txt") as f:
    file = f.read().split()
    map = {
        (x, y): value
        for x, line in enumerate(file)
        for y, value in enumerate(line * repeat_n)
    }


def tobaggen_movement(
    position: tuple[int, int], slope_method: tuple[int, int]
) -> tuple[int, int]:
    new_tobaggen_position = tuple(x + y for x, y in zip(position, slope_method))
    return new_tobaggen_position


slope_methods = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]


def tobaggen_movement_simulator(slope_method: tuple[int, int]) -> int:
    position = (0, 0)
    tree_tracker = 0
    tree = "#"

    while True:
        try:
            tree_tracker += 1 if map[position] == tree else 0
            position = tobaggen_movement(position, slope_method)
        except:
            return tree_tracker


print(
    prod([tobaggen_movement_simulator(slope_method) for slope_method in slope_methods])
)
