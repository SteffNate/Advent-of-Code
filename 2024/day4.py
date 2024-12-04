document = parse(4)

def find_inline_xmas(line):
    return len(re.findall(r"(?=(XMAS|SAMX))", line))

def find_xmas_start_indexes(line):
    indexes_of_x_and_s = [index for index, value in enumerate(line) if value in "XS"]
    return indexes_of_x_and_s

def word_is_xmas(word):
    return word == "XMAS" or word == "SAMX"

def check_index_for_word_horizontal(index, paragraph):
    word = paragraph[0][index] + paragraph[1][index] + paragraph[2][index] + paragraph[3][index]
    return word_is_xmas(word)

def check_index_for_word_diagonal(index, paragraph):
    if index > 2:
        word_diagonal_left = paragraph[0][index] + paragraph[1][index-1] + paragraph[2][index-2] + paragraph[3][index-3]
    else:
        word_diagonal_left = False
    if index < 137:
        word_diagonal_right = paragraph[0][index] + paragraph[1][index+1] + paragraph[2][index+2] + paragraph[3][index+3]
    else:
        word_diagonal_right = False
    return word_is_xmas(word_diagonal_left) + word_is_xmas(word_diagonal_right)
    
def find_horisontal(paragraph, indexes):
    return sum([check_index_for_word_horizontal(index, paragraph) for index in indexes])

def find_diagonal(paragraph, indexes):
    return sum([check_index_for_word_diagonal(index, paragraph) for index in indexes])

def ceres_search(all_lines):
    number_of_xmas = 0
    for i in range(len(all_lines)):

        init_line = all_lines[i]
        start_indexes = find_xmas_start_indexes(init_line)
        inline = find_inline_xmas(init_line)

        number_of_xmas += inline
        try:
            paragraph = all_lines[i:i+4]
            
            horisontal = find_horisontal(paragraph, start_indexes)

            diagonal = find_diagonal(paragraph, start_indexes)
            
            number_of_xmas += horisontal
            number_of_xmas += diagonal
        except:
            continue

    return number_of_xmas
  
%%timeit
answer_1 = ceres_search(document)

def word_is_mas(word):
    return word == "MAS" or word == "SAM"

def find_mas_start_indexes(line):
    indexes_of_x_and_s = [index for index, value in enumerate(line) if value in "MS"]
    return indexes_of_x_and_s

def check_index_for_mas_cross(index, paragraph):
    if  index < len(paragraph[0]) - 2:
        word_diagonal_right = paragraph[0][index] + paragraph[1][index+1] + paragraph[2][index+2]
        
    else:
        word_diagonal_right = False
        
    if word_is_mas(word_diagonal_right):  
        word_diagonal_left = paragraph[0][index+2] + paragraph[1][index+1] + paragraph[2][index]

        if word_is_mas(word_diagonal_left):
            return 1
            
    return 0
    
def find_cross(paragraph, indexes):
    return sum([check_index_for_mas_cross(index, paragraph) for index in indexes])

def ceres_search_ex_mas(all_lines):
    number_of_x_mas = 0
    for i in range(len(all_lines)):

        init_line = all_lines[i]
        start_indexes = find_mas_start_indexes(init_line)
        try:
            paragraph = all_lines[i:i+3]
            number_of_x_mas+= find_cross(paragraph, start_indexes)
        
        except:
            continue

    return number_of_x_mas
    
%%timeit
answer_2 = ceres_search_ex_mas(document)
