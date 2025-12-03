from itertools import pairwise

with open("inputs/input_2.txt", "r") as f:
    file = f.read().strip().split(",")
    ranges = [i.strip().split("-") for i in file]


# Part 1
def check_invalid_conditions(range_start: str, range_end: str) -> list[int]:
    invalid_ids = []

    for prod_id in range(int(range_start), int(range_end) + 1):
        str_id = str(prod_id)
        length_of_id = len(str_id)
        halfpoint_id = length_of_id // 2
        if length_of_id % 2 == 1:
            continue
        if str_id[0:halfpoint_id] == str_id[halfpoint_id:]:
            invalid_ids.append(prod_id)
    return invalid_ids


invalid_ids = []
for start, end in ranges:
    invalid_ids_for_range = check_invalid_conditions(start, end)
    invalid_ids.extend(invalid_ids_for_range)

print(sum(invalid_ids))


# Part 2
import re

regex_pattern = re.compile(r"^(\d+?)\1+$")


def test_regex(
    range_start: str, range_end: str, regex_pattern=regex_pattern
) -> list[int]:
    invalid_ids = []

    for prod_id in range(int(range_start), int(range_end) + 1):
        str_id = str(prod_id)
        capture_id = regex_pattern.match(str_id)

        if capture_id:
            invalid_ids.append(int(str_id))

    return invalid_ids


invalid_ids = []
for start, end in ranges:
    invalid_ids_for_range = test_regex(start, end, regex_pattern)
    invalid_ids.extend(invalid_ids_for_range)

print(sum(invalid_ids))


# Initially tried to brute force, got the wrong number by setting ids with a length of 1 as invalid
def check_invalid_conditions_extended(range_start: str, range_end: str) -> list[int]:
    invalid_ids = []

    for prod_id in range(int(range_start), int(range_end) + 1):
        str_id = str(prod_id)

        if len(str_id) == 1:
            continue

        if len(set(str_id)) == 1:
            invalid_ids.append(prod_id)
            continue

        length_of_id = len(str_id)

        factors_of_length = [
            n for n in range(2, length_of_id + 1) if length_of_id % n == 0
        ]
        if not factors_of_length:
            continue

        n_in_each_factor = [length_of_id // v for v in factors_of_length]

        for factor in n_in_each_factor:
            steps = [i for i in range(0, length_of_id + 1, factor)]
            paired_steps = [i for i in pairwise(steps)]

            if all(
                str_id[paired_steps[index][0] : paired_steps[index][1]]
                == str_id[paired_steps[index + 1][0] : paired_steps[index + 1][1]]
                for index in range(0, len(paired_steps) - 1)
            ):
                invalid_ids.append(int(str_id))
                break

    return invalid_ids
