import re

document = parse(3)

pattern_find_instructions = r"\bmul\b\([0-9]{1,4},[0-9]{1,4}\)"
pattern_find_mul_inputs = r"[0-9]*,[0-9]*"

input = "".join(document)
correct_instructions = re.findall(pattern_find_instructions,input)

pattern_find_mul_inputs = r"[0-9]*,[0-9]*"
mul_inputs = [re.findall(pattern_find_mul_inputs, i)[0].strip().split(",") for i in correct_instructions]
answer_1 = sum(int(summation) for summation in [int(pos1) * int(pos2) for pos1, pos2 in mul_inputs])

alt_nested_horribleness_answer_1 = sum(int(summation) for summation in [int(pos1) * int(pos2) for pos1, pos2 in  [re.findall(pattern_find_mul_inputs, i)[0].strip().split(",") for i in re.findall(pattern_find_instructions,input)]])

# Part 2

split_on_words = re.split(r"(do\(\))|(don't\(\))",input)

dos = []
for index, value in enumerate(split_on_words):
    if index == 0:
        dos.append(value)
    if value == "do()":
        dos.append(split_on_words[index+2])

input_2 = "".join(dos)

correct_instructions_specified = re.findall(pattern_find_instructions,input_2)

mul_inputs_corrected = [re.findall(pattern_find_mul_inputs, i)[0].strip().split(",") for i in correct_instructions_specified]

sum_of_corrected_instructions_answer_2 = sum(int(summation) for summation in [int(pos1) * int(pos2) for pos1, pos2 in mul_inputs_corrected])
