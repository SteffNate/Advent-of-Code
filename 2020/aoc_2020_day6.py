# day 6
from functools import reduce

with open("inputs/input_6.txt") as f:
    file = [i for i in f.read().split("\n\n")]

# Solution one
print(sum([len(set(line.strip().replace("\n", ""))) for line in file]))

# Solution two
n_answer_all_same = []

for group in file:
    n_answer_all_same.append(
        len(set.intersection(*[set(answer) for answer in group.strip().split("\n")]))
    )
print(sum(n_answer_all_same))
