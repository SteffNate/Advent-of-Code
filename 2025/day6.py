from pprint import pprint
import numpy as np

# part 1
with open("inputs/input_6.txt", "r") as f:
    file = [i for i in f.read().splitlines()]
    part_array = np.rec.fromarrays(
        [np.array([int(i) if i.isdigit() else i for i in l.split()]) for l in file]
    )
print(
    sum(
        [
            np.prod(np.asarray(values.tolist()[:-1]), dtype=np.int64)
            if values[-1] == "*"
            else np.sum(np.asarray(values.tolist()[:-1]), dtype=np.int64)
            for values in part_array
        ]
    )
)

# part 2
with open("inputs/input_6.txt", "r") as f:
    file = f.read().splitlines()

idxs = []
for i, v in enumerate(zip(file[0], file[1], file[2], file[3], file[4])):
    if all(val == " " for val in v):
        idxs.append(i)

bounds = [-1] + idxs + [len(file[0])]

num_ranges = [
    list(range(right - 1, left, -1)) for left, right in zip(bounds, bounds[1:])
]

sums = []
for idx_values in num_ranges:
    vals = []
    op = None
    for idx in idx_values:
        vals.append(
            int("".join([file[0][idx], file[1][idx], file[2][idx], file[3][idx]]))
        )
        if file[4][idx] != " ":
            op = file[4][idx]
    sums.append(
        np.prod(vals, dtype=np.int64) if op == "*" else np.sum(vals, dtype=np.int64)
    )

print(sum(sums))
