with open("inputs/input_1.txt", "r") as f:
    file = [int(expense) for expense in f.readlines()]


def is_2020(expense_1: int, expense_2: int, expense_3: int) -> bool:
    return (expense_1 + expense_2 + expense_3) == 2020


for index in range(len(file)):
    for i in range(index + 1, len(file)):
        for z in range(index + 2, len(file)):
            if is_2020(file[index], file[i], file[z]):
                print(file[index] * file[i] * file[z])
                break
