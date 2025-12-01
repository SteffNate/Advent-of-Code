from pprint import pprint

with open("inputs/input_1.txt", "r") as f:
    rotation_instructions = f.read().split()
    rotations = [
        int(instruction[1:]) if instruction[0] == "R" else -int(instruction[1:])
        for instruction in rotation_instructions
    ]

# North Pole Secret Entrance training password
dial_position: int = 50
number_of_0_points: int = 0

for rotation in rotations:
    dial_position += rotation
    if abs(dial_position) % 100 == 0:
        number_of_0_points += 1
pprint(number_of_0_points)

# North Pole Secret Entrance method 0x434C49434B

dial_position_second_attempt: int = 50
number_of_0_crossed: int = 0

for rotation in rotations:
    overflow_zero_turns, remainder = divmod(abs(rotation), 100)
    rotation = remainder if rotation >= 0 else -remainder

    start_pos = dial_position_second_attempt
    current_position = start_pos + rotation

    if current_position % 100 == 0:
        number_of_0_crossed += 1
        dial_position_second_attempt = 0
    else:
        if (current_position < 0 or current_position > 99) and start_pos != 0:
            number_of_0_crossed += 1
        dial_position_second_attempt = current_position % 100

    number_of_0_crossed += overflow_zero_turns

pprint(number_of_0_crossed)
