# For adding tuples
import operator

# input as str lines
document = parse(6)

# Generate map for lab
lab = {(x, y): position 
                         for y, row in enumerate(document) 
                         for x, position in enumerate(row)
                        }

def guard_position(lab):
    """Get initial position of Guard"""
    return next((position for position, item in lab.items() if item not in ["#", "."]))

def switch_direction_90_degrees(facing_direction):
    """Rotates 90 degrees"""
    match facing_direction:
        case "^":
            return ">"
        case "v":
            return "<"
        case ">":
            return "v"
        case "<":
            return "^"
        
# a single movement in lab dictionary grid
north, south, east, west  = ((0, -1), (0, 1), (1, 0), (-1, 0))

# Get next position key
def next_position(current_position, movement_direction):
    """Returns new position after movement"""
    return tuple(map(operator.add, current_position, movement_direction))

# Get way to move from the direction the guard is facing
def guard_moves_in_direction(current_position, facing_direction):
    """Moves a single step in facing direction"""
    match facing_direction:
        case "^":
            return next_position(current_position, north)
        case "v":
            return next_position(current_position, south)
        case ">":
            return next_position(current_position, east)
        case "<":
            return next_position(current_position, west)
        
# Run task 1
distinct_spots_visited = set()
current_position = guard_position(lab)
facing_direction = lab[current_position]

while True:
    try:
        next_position_in_lab = guard_moves_in_direction(current_position, facing_direction)
        if lab[next_position_in_lab] == "#":
            facing_direction = switch_direction_90_degrees(facing_direction)
        else:
            current_position = next_position_in_lab
            distinct_spots_visited.add(current_position)

    except :
        print("Guard moved out of Lab")
        break

answer_6_1 = len(distinct_spots_visited)
print(answer_6_1)

# part 2
# Brute force obstacle placement maps with modular keys that ended up not being used
def generate_lab_maps_with_one_obstacle(original_schematic):
    map_schematics = {}
    for number, (key, map_point) in enumerate(original_schematic.items()):
        if map_point == ".":
            schematic_name = f"modified_schematic_number{number+1}"
            schematic_name = dict(original_schematic)
            schematic_name[key] = "#"
            map_schematics[key] = schematic_name
    return map_schematics
    
# Generate possible obstruction placings
map_schematics = generate_lab_maps_with_one_obstacle(lab)

# Test a map to see if it is looping, looping is defined as visiting two consecutive obstructions in a row, twice, so that the guard is moving on the same path 
def test_obstruction(lab_map):
    spots_visited = set()
    obstructions_in_twos = []

    current_position = guard_position(lab_map)
    facing_direction = lab_map[current_position]

    while True:
        try:
            next_position_in_lab = guard_moves_in_direction(current_position, facing_direction)
            if lab_map[next_position_in_lab] == "#":
                
                #Check if looping
                obstructions_in_twos.append(next_position_in_lab)
                if len(obstructions_in_twos) == 2:
                    tuple_of_visited_combinations = (*obstructions_in_twos,)

                    if tuple_of_visited_combinations in spots_visited:
                        return True
                    spots_visited.add(tuple_of_visited_combinations)
                    obstructions_in_twos = []

                # Switch Direction

                facing_direction = switch_direction_90_degrees(facing_direction)
            else:
                current_position = next_position_in_lab

        except :
            return False
# Gathering the positions where the guard would be looping for the Historians

infinte_loop_positions = []
for key, map_schematic in map_schematics.items():
    if test_obstruction(map_schematic):
        infinte_loop_positions.append(key)

answer_6_2 = len(infinte_loop_positions)
print(answer_6_2)
