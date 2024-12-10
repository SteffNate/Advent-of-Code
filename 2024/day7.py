from itertools import product
document = parse(7)
target = [int(i.split(":")[0]) for i in document]

numbers = [ints(i.split(":")[1]) for i in document] 

most_tuples = max([len(i) for i in numbers])

def generate_combinations(length):
    combinations = list(product("+*", repeat=length))
    combinations = ["".join(comb) for comb in combinations]
    return combinations

combinations_of_pluss_and_multiplication = {it: generate_combinations(it) for it in range(most_tuples)}

def pluss_or_multiplicate(number_1, number_2, operator):
    match operator:
        case "+":
            return number_1 + number_2
        case "*":
            return number_1 * number_2
        case "|":
            return int(str(number_1) + str(number_2))

def test_case(target, numbers, operator_combination):
    result = pluss_or_multiplicate(numbers[0], numbers[1], operator_combination[0])
    if len(numbers) != 2:
        for value, op in zip(numbers[2:], operator_combination[1:]):
            result = pluss_or_multiplicate(result, value,op)
    return target == result

possible_targets = set()

for target_value, inputs in zip(target, numbers):
    operator_combinations = combinations_of_pluss_and_multiplication[len(inputs)-1]
    for combination in operator_combinations:
        if test_case(target_value, inputs, combination):
            possible_targets.add(target_value)
        else:
            continue

# answer 7_1
sum(possible_targets)

def generate_combinations_with_concat(length):
    combinations = list(product("+*|", repeat=length))
    combinations = ["".join(comb) for comb in combinations]
    return combinations

combinations_of_pluss_and_multiplication_concat = {it: generate_combinations_with_concat(it) for it in range(most_tuples)}

possible_targets = set()

for target_value_concat, inputs in zip(target, numbers):
    operator_combinations = combinations_of_pluss_and_multiplication_concat[len(inputs)-1]
    for combination in operator_combinations:
        if test_case(target_value_concat, inputs, combination):
            possible_targets.add(target_value_concat)
        else:
            continue

# answer 7_1
sum(possible_targets)
