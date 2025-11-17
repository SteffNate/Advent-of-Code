from pprint import pprint
from math import prod

# part 1
with open("inputs/everybody_codes_e2025_q04_p1.txt", "r") as f:
    file = [int(i) for i in f.read().split()]

turns = prod([file[i - 1] / file[i] for i in range(1, len(file))])

print(abs(turns * 2025))

# part 2
with open("inputs/everybody_codes_e2025_q04_p2.txt", "r") as f:
    file = [int(i) for i in f.read().split()]

turns = prod([file[i - 1] / file[i] for i in range(1, len(file))])

threshold_turns = 1_000_000_000_000_0
min_turns = 1
max_turns = 1_000_000_000_000_0

while max_turns - min_turns > 1:
    median_turns = (max_turns + min_turns) // 2
    n_turns = median_turns * turns

    if n_turns < threshold_turns:
        min_turns = median_turns
    elif n_turns > threshold_turns:
        max_turns = median_turns
    else:
        print(print("median is threshold", median_turns))

print(f"max_turns: {max_turns}.  min_turns: {min_turns}. median_turns: {median_turns}")

# Part 3
with open("inputs/everybody_codes_e2025_q04_p3.txt", "r") as f:
    file = [x for x in f.read().split()]

input = []
for item in file:
    if "|" in item:
        unpacked = tuple(int(x) for x in item.split("|"))
        input.append(unpacked)
    else:
        input.append(int(item))


testinput = [5, (7, 21), (18, 36), (27, 27), (10, 50), (10, 50), 11]
turns = []
for i in range(1, len(input)):
    if isinstance(input[i], int):
        turns.append(input[i - 1][1] / input[i])
    elif isinstance(input[i - 1], int):
        turns.append(input[i - 1] / input[i][0])
    else:
        turns.append(input[i - 1][1] / input[i][0])


print("Part 3", int(prod(turns) * 100))
