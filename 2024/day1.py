document = parse(1)

input_list1 = []
input_list2 = []

for i in document:
    line1, line2 = i.split()
    input_list1.append(int(line1))
    input_list2.append(int(line2))

input1 = sorted(input_list1)
input2 = sorted(input_list2)

differences = []

for index1, index2 in zip(input1, input2):
    differences.append(abs(index1 - index2))

answer_1_1 = sum(differences)

total_difference = sum(abs(x - y) for x, y in zip(sorted(input_list1), sorted(input_list2)))

def add_frequency_of_appearance(value, list2):
    frequency = 0
    for i in list2:
        frequency += (int(value) == int(i))
    return frequency

frequencies = [add_frequency_of_appearance(i, input2) for i in input1]

similarity_score = []
for value, freq in zip(input1, frequencies):
    similarity_score.append(int(value)*int(freq))

answer_1_2 = sum(similarity_score)
