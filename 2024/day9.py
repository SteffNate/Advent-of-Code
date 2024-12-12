from itertools import chain, zip_longest


document = parse(9,list)

def convert_to_available_space(free_space_number):
    return ["." for i in range(free_space_number)] 

def split_files_and_spaces(disk):
    return {"files": disk[::2], "spaces": disk[1::2]}

split_disk = split_files_and_spaces(document[0])

files = [[str(index)] * int(value) for index, value in enumerate(split_disk["files"])]

free_spaces = [convert_to_available_space(int(number_of_spaces)) for number_of_spaces in split_disk["spaces"]]

expanded_filesystem = list(chain(*[item for file_space_air in zip_longest(files, free_spaces, fillvalue="n") for item in file_space_air]))

expanded_filesystem.remove("n")

def move_files_to_open_spaces(input_drive):
    new_drive = input_drive.copy()
    file_indices = [index for index, item in enumerate(new_drive) if item.isdigit()]
    
    for n in range(len(file_indices)):
        file_position = file_indices.pop()
        free_space_position = new_drive.index(".")
        if free_space_position < file_position:
            new_drive[free_space_position] = new_drive[file_position]
            new_drive[file_position] = "."
        else:
            break
    return new_drive 
    
moved_file_fragments = move_files_to_open_spaces(expanded_filesystem)
summary = [index * int(value) for index, value in enumerate(moved_file_fragments) if value != "."]
answer_9_1 = sum(summary)
print(answer_9_1)
# 2

def move_whole_files_to_open_spaces(input_drive):
    new_drive = input_drive.copy()
    
    files_index_length = [[index, len(item)] for index, item in enumerate(new_drive) if not len(item) == 0 and item[0].isdigit()]

    moved_items = set()

    while files_index_length:

        file_position = files_index_length.pop()

        free_space_position = next(([index, len(item)] for index, item in enumerate(new_drive) if len(item) >= file_position[1] and not len(item) == 0 and item[0] == "."), False)

        
        if free_space_position:
            if free_space_position[0] < int(file_position[0]):
    
                new_drive[free_space_position[0]] = new_drive[file_position[0]]

                new_drive[file_position[0]] = convert_to_available_space(file_position[1])

                remaining_space = free_space_position[1] - file_position[1]

                moved_items.add(new_drive[file_position[0]][0])

                if remaining_space > 0:
                    
                    remaining_space_index = free_space_position[0] + 1

                    remaining_space_file = convert_to_available_space(remaining_space)
                    
                    new_drive.insert(remaining_space_index, remaining_space_file) 
                
                
                files_index_length = [[index, len(item)] for index, item in enumerate(new_drive) if not len(item) == 0 and item[0].isdigit() and not item[0] in moved_items]


        else:
            continue

    return new_drive
    
expanded_filesystem_packed = list([item for file_space_air in zip_longest(files, free_spaces, fillvalue="n") for item in file_space_air])

expanded_filesystem_packed.remove("n")

move_blocks = move_whole_files_to_open_spaces(expanded_filesystem_packed)

unpack = list(chain(*[item for item in move_blocks]))

answer_9_2 = sum([index * int(value) for index, value in enumerate(unpack) if value != "."])
print(answer_9_2)
