from collections import Counter
from itertools import batched


with open("inputs/day_1_1.txt") as f:
    file = f.read()

sum_of_potions = 0
for monster_type, number_of_monster in Counter(file).items():
    if monster_type == "B":
        sum_of_potions += number_of_monster
    if monster_type == "C":
        sum_of_potions += number_of_monster * 3
    else:
        continue
print(sum_of_potions)


with open("inputs/day_1_2.txt") as f:
    file = f.read()


battles: dict[tuple[str, ...], int] = {}

for monsters in batched(file, 2):
    monster_combination: tuple[str, ...] = tuple(sorted(monsters))

    if monster_combination not in battles:
        battles[monster_combination] = 1
    else:
        battles[monster_combination] += 1


def monster_strength(monster: str) -> int:
    match monster:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 3
        case "D":
            return 5
        case _:
            return 0


def group_battle(monster_group: tuple[str, str]) -> int:
    potions_needed = 0

    if monster_group == ("A", "x"):
        return potions_needed

    if "x" not in monster_group:
        potions_needed += 2

    for monster in monster_group:
        potions_needed += monster_strength(monster)

    return potions_needed


potions_for_group_fight = [
    group_battle(monster_group) * battles[monster_group] for monster_group in battles
]

with open("inputs/day_1_3.txt") as f:
    file = f.read()


battles_tripple: dict[tuple[str, ...], int] = {}

for monsters in batched(file, 3):
    monster_combination: tuple[str, ...] = tuple(sorted(monsters))

    if monster_combination not in battles_tripple:
        battles_tripple[monster_combination] = 1
    else:
        battles_tripple[monster_combination] += 1


def group_battle(monster_group: tuple[str, str]) -> int:
    potions_needed = 0

    if monster_group == ("A", "x", "x"):
        return potions_needed

    if "x" not in monster_group:
        potions_needed += 6

    if len([i for i in monster_group if i == "x"]) == 1:
        potions_needed += 2

    for monster in monster_group:
        potions_needed += monster_strength(monster)

    return potions_needed


potions_for_group_fight_triplets = [
    group_battle(monster_group) * battles_tripple[monster_group]
    for monster_group in battles_tripple
]

print(sum(potions_for_group_fight_triplets))
