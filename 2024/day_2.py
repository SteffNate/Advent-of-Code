# no problemopy
import numpy as np

document = parse(2)

all_reports = [np.array([int(n) for n in i.split()]) for i in document]

def is_sorted(array):
    return any([all(array == sorted(array)), all(array == sorted(array, reverse=True))])

def check_safety(array):
    for index, value in enumerate(array):
        if index == len(array) - 1:
            return True
        if check_addition_or_subtraction(value, array[index+1]):
            continue
        return False
    
def check_addition_or_subtraction(value_1, value_2):    
    if 1 <= abs(value_1 - value_2) <= 3:
        return True
    return False

def report_secure_as_is(array):
    if is_sorted(array) and check_safety(array):
        return True
    return False

number_of_safe_reports = len([report for report in all_reports if report_secure_as_is(report)])

answer_1 = number_of_safe_reports


def dampen_problem(array):
    for i in range(len(array)):
        temp_array = np.delete(array, i)
        if secure_as_is(temp_array):
            return True
        continue
    return False

def run_problem_dampener(all_reports):
    safe_reports_with_problem_dampener = []
    for report in all_reports:
        if secure_as_is(report):
            safe_reports_with_problem_dampener.append(report)
            continue
        else:
            if dampen_problem(report):
                safe_reports_with_problem_dampener.append(report)
    return safe_reports_with_problem_dampener

number_of_safe_reports_with_problem_dampener = len(run_problem_dampener(all_reports))

answer_2 = number_of_safe_reports_with_problem_dampener
