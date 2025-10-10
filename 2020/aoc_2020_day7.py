with open("inputs/input_7.txt") as f:
    file = f.readlines()


bags = {}
for line in file:
    bag_types, contains_bags = (
        line.replace("bags", "")
        .replace(".", "")
        .replace("\n", "")
        .replace("other", "")
        .split("contain")
    )
    bag_type = bag_types.strip()

    bags_in_bag = []
    for bag in contains_bags.strip().split(","):
        bag = bag.strip().replace("bag", "").strip()
        if not bag or bag.startswith("no"):
            continue
        parts = bag.split(" ", 1)
        if len(parts) < 2:
            continue
        count, color = parts
        bags_in_bag.append((count, color.strip()))
    bags[bag_type] = bags_in_bag


can_contain_golden_bag = set(["shiny gold"])
# Solution 1
while True:
    previous_size = len(can_contain_golden_bag)
    for key in bags:
        colors = [i[1] for i in bags[key]]
        if any(color in can_contain_golden_bag for color in colors):
            can_contain_golden_bag.add(key)
    if len(can_contain_golden_bag) == previous_size:
        break

print(len(can_contain_golden_bag) - 1)
# Solution 2
stack_of_bags = bags["shiny gold"].copy()
all_bags = []

while stack_of_bags:
    count, color = stack_of_bags.pop()
    for inner_count, inner_color in bags[color]:
        total_count = int(count) * int(inner_count)
        all_bags.append((total_count, inner_color))
        stack_of_bags.append((total_count, inner_color))

print(sum(count for count, color in all_bags))
