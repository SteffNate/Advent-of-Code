from pprint import pprint


necessary_conditions = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]


def check_if_all_present(passport):
    return all(cond in passport for cond in necessary_conditions)


def controlls(field: str, value: str) -> bool:
    if field == "cid":
        return True
    if field == "hgt":
        if "in" in value:
            field = "hgtin"
            value = "".join(c for c in value if c.isdigit())
        elif "cm" in value:
            field = "hgtcm"
            value = "".join(c for c in value if c.isdigit())
        else:
            return False

    string_fields = ["hcl", "ecl", "pid"]

    number_fields = {
        "byr": range(1920, 2003),
        "iyr": range(2010, 2021),
        "eyr": range(2020, 2031),
        "hgtin": range(59, 77),
        "hgtcm": range(150, 194),
    }
    if field in number_fields:
        try:
            int_value = int(value)
        except ValueError:
            return False
        return int_value in number_fields[field]

    if field in string_fields:
        if field == string_fields[0]:
            return (
                (value[0] == "#")
                and (all([letter in "0123456789abcdef" for letter in value[1:]]))
                and (len(value[1:]) == 6)
            )
        if field == string_fields[1]:
            return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        if field == string_fields[2]:
            return len(value) == 9 and (all(i.isdigit() for i in value))

    return False


def check_values(passport):
    separated_passport = passport.split()
    values = {}
    for i in separated_passport:
        key, value = i.split(":")
        values[key] = value

    condition_checks = []
    for field, value in values.items():
        condition_checks.append(controlls(field, value))
    return all(condition_checks)


with open("inputs/input_4.txt") as f:
    file = f.readlines()

    passports = []
    passport = ""
    for line in file:
        if len(line) > 2:
            passport += line

        else:
            if check_if_all_present(passport):
                passports.append(check_values(passport))
            passport = ""
    passports.append(check_values(passport))


pprint(sum(passports))
