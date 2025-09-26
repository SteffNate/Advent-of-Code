with open("inputs/input_2.txt", "r") as f:
    file = f.readlines()


def process_input(input_line):
    key, password = input_line.split(":")
    minumum, rest_key = key.split("-")
    maximum, essential_letter = rest_key.split(" ")
    return int(minumum), int(maximum), essential_letter, password


def check_if_valid_password(minimum, maximum, essential_letter, password) -> bool:
    return minimum <= password.count(essential_letter) <= maximum


parsed_input = [process_input(line) for line in file]

print(
    sum(
        [
            check_if_valid_password(minimum, maximum, essential_letter, password)
            for minimum, maximum, essential_letter, password in parsed_input
        ]
    )
)


def check_if_valid_on_comparison(position_1, position_2, essential_letter, password):
    return (
        (password[position_1] == essential_letter)
        | (password[position_2] == essential_letter)
    ) & (password[position_1] != password[position_2])


print(
    sum(
        [
            check_if_valid_on_comparison(minimum, maximum, essential_letter, password)
            for minimum, maximum, essential_letter, password in parsed_input
        ]
    )
)
