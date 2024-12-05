document = parse(5, sections=paragraphs)

page_instructions = [[int(i) for i in page_instruction.split("|")] for page_instruction in document[0].split()]

page_instructions_manual = DefaultDict(set)

for instruction in page_instructions:
    page_instructions_manual[instruction[0]].add(instruction[1])
  
sleigh_launch_safety_manual_updates = [[int(page) for page in update.split(",")] for update in document[-1].split()]

def return_middle_page(correct_update):
    return correct_update[int(len(correct_update) / 2)]

def check_safety_manual(page_number, comparison_page):
    return comparison_page in page_instructions_manual[page_number]

result = []
bad_updates = []

for update in sleigh_launch_safety_manual_updates:
    safe = True
    
    for page_number_index in range(len(update) - 1, 0, -1):
        page_number = update[page_number_index]
        if any(check_safety_manual(page_number, comparison_page) for comparison_page in update[:page_number_index]):
            safe = False
            bad_updates.append(update)
            break
    if safe:
        result.append(return_middle_page(update))    

answer_5_1 = sum(result)
print(answer_5_1)

def check_and_fix_safety_update(line):
    modified_line = line.copy()
    for page_number_index in range(len(line) - 1, 0, -1):
        page_number = line[page_number_index]

        for comparison_page_index, comparison_page in enumerate(line[:page_number_index]):
            if check_safety_manual(page_number, comparison_page):
                modified_line[page_number_index], modified_line[comparison_page_index] = comparison_page, page_number

                return check_and_fix_safety_update(modified_line)
            
    return return_middle_page(modified_line)

anwer_5_2_fixed_updates = sum([check_and_fix_safety_update(i) for i in bad_updates])
print(anwer_5_2_fixed_updates)
