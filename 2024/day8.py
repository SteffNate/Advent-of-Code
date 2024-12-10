# day 8
from itertools import combinations

document = parse(8)

print(len(document), len(document[0]))

map_of_antennas = {(x, y): position 
                         for y, row in enumerate(document) 
                         for x, position in enumerate(row)
                        }

def get_different_frequencies(map_of_antennae):
    return list(set([i for i in map_of_antennae.values() if i != "."]))

def get_position_of_same_frequency_antennas(map_of_antennae, frequency):
    positions = [position for position, frequency_type in map_of_antennae.items() if frequency_type == frequency]
    return positions

def get_relative_position(antenna_1, antenna_2):
    return tuple(map(operator.sub, antenna_1, antenna_2))

def check_antinode_positions(antenna_1, antenna_2):
    difference_in_position = get_relative_position(antenna_1, antenna_2)
    
    antinode_1_position = tuple(map(operator.add, antenna_1, difference_in_position))
    antinode_2_position = tuple(map(operator.sub, antenna_2, difference_in_position))

    return (antinode_1_position, antinode_2_position)

def within_bounds(position):
    return all(min_pos <= current_position <= max_pos  for min_pos, current_position, max_pos in zip((0, 0), position, (49,49)))

def look_for_antinode_positions(map_of_antennas):
    valid_antinode_positions = set()
    frequency_types = get_different_frequencies(map_of_antennas)
    same_frequency_positions = {frequency: get_position_of_same_frequency_antennas(map_of_antennas, frequency) for frequency in frequency_types}
    
    for frequency_positions in same_frequency_positions.values():
        antenna_combinations = combinations(frequency_positions, 2)
        for combination in antenna_combinations:
            antinode_positions = check_antinode_positions(combination[0], combination[1])
            for possible_antinode in antinode_positions:
                if within_bounds(possible_antinode):
                    valid_antinode_positions.add(possible_antinode) 
            
                

    return valid_antinode_positions

antinode_positions =  look_for_antinode_positions(map_of_antennas)
# answer 8_1
len(antinode_positions)

#part2
def find_antinodes_in_line(antenna, distance, addition):
        current_position = antenna
        antinodes = []
        while within_bounds(current_position):
                if addition == True:
                    new_position = tuple(map(operator.add, current_position, distance))
                    current_position = new_position
                elif addition == False:
                    new_position = tuple(map(operator.sub, current_position, distance))
                    current_position = new_position
                else:
                      print("error")
                      
                antinodes.append(new_position)
        
        return antinodes

def check_antinode_positions_extended(antenna_1, antenna_2):
    difference_in_position = get_relative_position(antenna_1, antenna_2)
    
    diagonal_add = find_antinodes_in_line(antenna_1, difference_in_position, True)
    diagonal_sub = find_antinodes_in_line(antenna_2, difference_in_position, False)

    return diagonal_add + diagonal_sub

def look_for_antinode_positions_extended(map_of_antennas):
    valid_antinode_positions = set()
    frequency_types = get_different_frequencies(map_of_antennas)
    same_frequency_positions = {frequency: get_position_of_same_frequency_antennas(map_of_antennas, frequency) for frequency in frequency_types}

    
    for frequency_positions in same_frequency_positions.values():
        antenna_combinations = combinations(frequency_positions, 2)
        for combination in antenna_combinations:
            antinode_positions = check_antinode_positions_extended(combination[0], combination[1])
            valid_antinode_positions.update([i for i in combination])
            for possible_antinode in antinode_positions:
                if within_bounds(possible_antinode):
                    valid_antinode_positions.add(possible_antinode) 
            
                

    return valid_antinode_positions


# answer 8_2
len(look_for_antinode_positions_extended(map_of_antennas))
