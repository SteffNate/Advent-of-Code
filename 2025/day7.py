from pprint import pprint
from collections import deque

with open("inputs/input_7.txt", "r") as f:
    file = f.read().split()

manifold_diagram = {
    (x, y): position for y, line in enumerate(file) for x, position in enumerate(line)
}

manifold_bounds = [max(manifold_diagram), min(manifold_diagram)]


def out_of_bounds(position: tuple[int, int]) -> bool:
    if not (
        (manifold_bounds[0][0] >= position[0] >= manifold_bounds[1][0])
        and (manifold_bounds[0][1] >= position[1] >= manifold_bounds[1][1])
    ):
        return True
    return False


# Copenhagen interpretation
def run_tachyon_splitter(manifold_diagram):
    splits = 0
    current_tachyons = deque(
        [next(i for i in manifold_diagram if manifold_diagram[i] == "S")]
    )

    move, add_left, add_right = (0, 1), (-1, 0), (1, 0)

    tachyon_cache = set()
    splitter_cache = set()
    while current_tachyons:
        x, y = current_tachyons.pop()

        if (x, y) in tachyon_cache:
            continue

        next_x, next_y = x + move[0], y + move[1]

        for _ in range(manifold_bounds[0][1]):
            if out_of_bounds((next_x, next_y)):
                break

            val_in_next_position = manifold_diagram[(next_x, next_y)]

            if val_in_next_position == ".":
                next_x, next_y = next_x + move[0], next_y + move[1]
                continue

            if val_in_next_position == "^":
                if (next_x, next_y) in splitter_cache:
                    continue

                splitter_cache.add((next_x, next_y))
                splits += 1

                tachyon_split_left = next_x + add_left[0], next_y + add_left[1]
                tachyon_split_right = next_x + add_right[0], next_y + add_right[1]

                if not out_of_bounds(tachyon_split_left):
                    current_tachyons.append(tachyon_split_left)
                if not out_of_bounds(tachyon_split_right):
                    current_tachyons.append(tachyon_split_right)

                break

        tachyon_cache.add((x, y))

    return splits


print(run_tachyon_splitter(manifold_diagram))


# Many-worlds
#


def create_many_worlds_graph(manifold_diagram):
    splitter_positions = sorted(
        [(x, y) for x, y in manifold_diagram if manifold_diagram[x, y] == "^"],
        key=lambda x: x[1],
    )
    add_left, add_right = (-1, 0), (1, 0)
    visited = set()
    current_tachyons = deque()
    root = splitter_positions[0]

    current_tachyons.append(root)
    visited.add(root)
    tree = {}

    while current_tachyons:
        x, y = current_tachyons.pop()

        tree.setdefault((x, y), [])

        tachyons = (
            (x + add_left[0], y + add_left[1]),
            (x + add_right[0], y + add_right[1]),
        )
        for tachyon in tachyons:
            hits_splitter = splitter_in_path(tachyon, splitter_positions)
            if hits_splitter is not None:
                tree[x, y].append(hits_splitter)

                if hits_splitter not in visited:
                    visited.add(hits_splitter)
                    current_tachyons.append(hits_splitter)
            else:
                tree[x, y].append(tachyon)
                if tachyon not in visited:
                    visited.add(tachyon)
    return tree, root


def splitter_in_path(initial_position, splitter_positions):
    x, y = initial_position
    for s_x, s_y in splitter_positions:
        if x == s_x and y < s_y:
            return s_x, s_y
    return None


graph, root = create_many_worlds_graph(manifold_diagram)


def count_unique_paths(graph, root):
    world_memory = {}

    def dfs(tachyon):
        if tachyon in world_memory:
            return world_memory[tachyon]

        if tachyon not in graph or not graph[tachyon]:
            world_memory[tachyon] = 1
            return 1

        total = 0
        for split_world in graph[tachyon]:
            total += dfs(split_world)

        world_memory[tachyon] = total
        return total

    return dfs(root)


print(count_unique_paths(graph, root))
