from pprint import pprint

# part 1
with open("inputs/everybody_codes_e2025_q03_p1.txt", "r") as f:
    file = [int(i) for i in f.read().split(",")]

pprint(sum(set(file)))

# part 2
with open("inputs/everybody_codes_e2025_q03_p2.txt", "r") as f:
    file = sorted(list(set([int(i) for i in f.read().split(",")])))

pprint(sum(file[:20]))

# part 3

from collections import Counter

with open("inputs/everybody_codes_e2025_q03_p3.txt", "r") as f:
    file = sorted(list([int(i) for i in f.read().split(",")]))

print(max(Counter(file).values()))
