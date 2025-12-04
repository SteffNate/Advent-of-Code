with open("inputs/input_4.txt", "r") as f:
    file = [i.strip() for i in f.read().split()]

paper_map = {}
for y, line_of_rolls in enumerate(file):
    for x, roll in enumerate(line_of_rolls):
        paper_map[x, y] = roll

room_bounds = [max(paper_map), min(paper_map)]

moves = [(-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (1, 0), (0, 1)]


# Part 1
def check_surrounding_floor_for_paper_rolls(position: tuple[int, int]) -> bool:
    surrounding_paper = 0

    for move in moves:
        check_pos = position[0] + move[0], position[1] + move[1]

        # Check if within room_bounds
        if not (
            (room_bounds[0][0] >= check_pos[0] >= room_bounds[1][0])
            and (room_bounds[0][1] >= check_pos[1] >= room_bounds[1][1])
        ):
            continue

        if paper_map[check_pos] == "@":
            surrounding_paper += 1

    if surrounding_paper < 4:
        return True

    return False


accessible_rolls = sum(
    check_surrounding_floor_for_paper_rolls(position)
    for position in paper_map
    if paper_map[position] == "@"
)
print(accessible_rolls)

# Part 2
rolls_of_paper_moved = 0

while True:
    rolls_moved_before = rolls_of_paper_moved
    paper_rolls = [position for position in paper_map if paper_map[position] == "@"]
    for paper_roll_pos in paper_rolls:
        move_roll = check_surrounding_floor_for_paper_rolls(paper_roll_pos)
        if move_roll:
            paper_map[paper_roll_pos] = "."
            rolls_of_paper_moved += 1

    if rolls_of_paper_moved == rolls_moved_before:
        break

print(rolls_of_paper_moved)
