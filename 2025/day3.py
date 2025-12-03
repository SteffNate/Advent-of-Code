with open("inputs/input_3.txt", "r") as f:
    file = f.read().split()

# part 1


def find_max_joltage_for_bank_of_batteries(bank: str) -> int:
    initial_jolt = max(bank[:-1])
    pos_of_initial_jolt = bank.find(initial_jolt)
    second_jolt = max(bank[pos_of_initial_jolt + 1 :])
    return int("".join([initial_jolt, second_jolt]))


max_jolts = [find_max_joltage_for_bank_of_batteries(bank) for bank in file]

print(sum(max_jolts))


# part 2
def find_max_joltage_for_bank_of_batteries_12_in_series(bank: str) -> int:
    bank_jolt_output = []
    bank_length = len(bank)

    first_available_battery = 0
    for remaining_picks in range(12, 0, -1):
        last_available_battery = bank_length - (remaining_picks - 1)
        jolt = max(bank[first_available_battery:last_available_battery])
        index_of_jolt = bank.index(
            jolt, first_available_battery, last_available_battery
        )
        bank_jolt_output.append(jolt)
        first_available_battery = index_of_jolt + 1

    return int("".join(bank_jolt_output))


max_jolts = [find_max_joltage_for_bank_of_batteries_12_in_series(bank) for bank in file]
print(sum(max_jolts))
