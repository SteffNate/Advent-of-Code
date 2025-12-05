with open("inputs/input_5.txt", "r") as f:
    all_ranges, all_ingredients = f.read().split("\n\n")

ingredients = [ingredient for ingredient in all_ingredients.split()]

ranges = sorted(
    [
        tuple(sorted(map(int, single_range.split("-"))))
        for single_range in all_ranges.split()
    ],
    key=lambda x: (x[0], x[1]),
)

# Part 1
fresh_ingredients = []
for ingredient in ingredients:
    for single_range in ranges:
        if int(single_range[0]) <= int(ingredient) <= int(single_range[1]):
            fresh_ingredients.append(ingredient)
            break

print(len(fresh_ingredients))
# Part 2


def condense_id_ranges(list_of_id_ranges: list[list[int]]) -> list[list[int]]:
    condensed_id_range = []
    cur_start, cur_end = list_of_id_ranges[0]

    for comparison_start, comparison_end in list_of_id_ranges[1:]:
        if comparison_start <= cur_end:
            if comparison_end > cur_end:
                cur_end = comparison_end
        else:
            condensed_id_range.append([cur_start, cur_end])
            cur_start, cur_end = comparison_start, comparison_end

    condensed_id_range.append([cur_start, cur_end])
    return condensed_id_range


print(sum(abs(x - y) + 1 for x, y in condense_id_ranges(ranges)))
