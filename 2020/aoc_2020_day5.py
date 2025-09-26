with open("inputs/input_5.txt") as f:
    file = f.readlines()

rows = 128
columns = 8


def process_seats(seat_partition: str, rows=rows, columns=columns) -> int:
    current_possible_rows = [i for i in range(0, rows)]
    current_possible_columns = [i for i in range(0, columns)]

    for instruction in seat_partition:
        middle_row = len(current_possible_rows) // 2
        middle_column = len(current_possible_columns) // 2
        match instruction:
            case "F":
                current_possible_rows = current_possible_rows[:middle_row]
            case "B":
                current_possible_rows = current_possible_rows[middle_row:]
            case "R":
                current_possible_columns = current_possible_columns[middle_column:]
            case "L":
                current_possible_columns = current_possible_columns[:middle_column]

    row = current_possible_rows[0]
    column = current_possible_columns[0]

    return (row * 8) + column


# Solution 1
print(
    max(
        [
            process_seats(
                seat_partition,
                rows,
            )
            for seat_partition in file
        ]
    )
)

# Solution 2

seat_ids = sorted(
    [process_seats(seat_partition, rows, columns) for seat_partition in file]
)

missing_seat_id = list(set(range(seat_ids[0], seat_ids[-1])) - set(seat_ids))[0]
print(missing_seat_id)

# Loop version
# for seat_idx in range(0, len(seat_ids) - 1):
#    if seat_ids[seat_idx + 1] != seat_ids[seat_idx] + 1:
#        print(seat_ids[seat_idx] + 1)
#        break
#    else:
#        continue
#
