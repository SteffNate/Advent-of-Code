# part 1
with open("inputs/everybody_codes_e2025_q01_p1.txt", "r") as f:
    f = f.read()
    names, instructions = f.split()
    names = names.split(",")
    instructions = [
        (instruction[0], int(instruction[1:]))
        for instruction in instructions.split(",")
    ]

current_pos: int = 0
n_instructions = len(instructions) - 1
for i in instructions:
    direction, distance = i
    if direction == "L":
        current_pos = current_pos - distance
    else:
        current_pos = current_pos + distance

    if current_pos > n_instructions:
        current_pos = n_instructions
    if current_pos < 0:
        current_pos = 0

print(names[current_pos])

# part 2
with open("inputs/everybody_codes_e2025_q01_p2.txt", "r") as f:
    f = f.read()
    names, instructions = f.split()
    names = names.split(",")
    instructions = [
        (instruction[0], int(instruction[1:]))
        for instruction in instructions.split(",")
    ]


n_left = sum([n for dir, n in instructions if dir == "L"])
n_right = sum([n for dir, n in instructions if dir == "R"])
position = n_right - n_left
if position < 0:
    names.reverse()
    position = abs(position)

location = position % len(names)
print(names[location])

# part 3
with open("inputs/everybody_codes_e2025_q01_p3.txt", "r") as f:
    f = f.read()
    names, instructions = f.split()
    names = names.split(",")
    instructions = [
        (instruction[0], int(instruction[1:]))
        for instruction in instructions.split(",")
    ]

n_positions = len(names)

for i in instructions:
    direction, distance = i
    relative_pos = distance if distance < n_positions else distance % n_positions
    if direction == "L":
        names[0], names[-relative_pos] = names[-relative_pos], names[0]
    else:
        names[0], names[relative_pos] = names[relative_pos], names[0]

print(names[0])
