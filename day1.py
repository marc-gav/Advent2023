import utils
from pprint import pprint as pp
import re

def find_earliest_occurrence(text, substrings):
    pattern = '|'.join(substrings)
    match = re.search(pattern, text)
    return match.group(0)

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
def problem1(day_input):
    lines_ = [[digit for digit in line if digit.isdigit()] for line in day_input]
    return sum([int(digits[0] + digits[-1]) for digits in lines_])

def problem2(day_input):
    all_elements = list(numbers.keys()) + list(numbers.values())
    sum = 0
    for line in day_input:
        first_element = find_earliest_occurrence(line, all_elements)
        if first_element in numbers.keys():
            first_element = numbers[first_element]
        last_element = find_earliest_occurrence(line[::-1], [occ[::-1] for occ in all_elements])[::-1]
        if last_element in numbers.keys():
            last_element = numbers[last_element]

        sum += int(first_element + last_element)

    return sum      

if __name__ == "__main__":
    day_input = utils.read_day("input1.txt")
    print(problem1(day_input))
    print(problem2(day_input))
