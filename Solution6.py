import numpy as np


input_file = "/Users/henrybest/Downloads/input_for_day_6.txt"

# test case
data = [
    ['123 ','328', ' 51' ,'64'],
    ['45' ,'64', ' 387', '23'],
    ['6 ','98 ',' 215',' 314'],
    ['* ', ' + ','  * ','  +'],
]


# part 1
# load from text file
data = np.loadtxt(input_file, dtype=str)


# parse into an array of integers and a list of operations
values = np.asarray(data[:-1], dtype=int)
operations = data[-1]

# list to collect outputs
outputs = []

# cycle through operations
for jj, operation in enumerate(operations):
    # using "in" means you handle spaces
    if '*' in operation:
        line_answer = np.prod(values[:, jj])
    elif '+' in operation:
        line_answer = np.sum(values[:, jj])
    outputs.append(line_answer)

# want to add up all values for the grand sum
grand_sum = np.sum(outputs)
print(grand_sum)

# part 2

# test case (where the spaces are not blindly ignored)
data = [
    ['123', '328', ' 51', '64 '],
    [' 45', '64 ', '387', '23 '],
    ['  6', '98 ', '215', '314'],
    ['* ', ' + ','  * ','  +'],
]

# loadtxt removes all spaces, so this isn't working.
# try another way to load the strings without removing spaces
# data = np.loadtxt(input_file, dtype=str)

# manually open and store as lists
all_lines = []
with open(input_file, 'r') as lines:
    for jj, line in enumerate(lines):
        all_lines.append(line)

# operators are always placed at the bottom left corner of
# each array element, so use this to find which string indices go
# with each problem so spaces are considered
indicies = []
for jj, character in enumerate(all_lines[-1]):
    if character == '*' or character == '+':
        indicies.append(jj)

data = []
for line in all_lines:
    current_list = []
    for jj in range(len(indicies)-1):
        start_index = indicies[jj]
        end_index = indicies[jj+1]-1
        current_list.append(line[start_index:end_index])
    current_list.append(line[end_index+1:-1])
    data.append(current_list)


# continue as normal
values = np.asarray(data[:-1], dtype=str)
operations = data[-1]


def parse_string(list_of_strings_of_value):
    # define some function that takes in a list of strings
    # and spits out a list of values
    output = []
    # get longest length to know how many digits
    longest = 0
    for item in list_of_strings_of_value:
        if len(item) > longest:
            longest = len(item)
    # loop from right to left
    for jj in range(longest):
        index = longest - jj - 1
        current_item = ''
        for item in list_of_strings_of_value:
            if index < len(item):
                if item[index] != ' ':
                    current_item += item[index]
        output.append(int(current_item))
    return output

outputs = []
for jj, operation in enumerate(operations):
    line_outputs = parse_string(values[:, jj])
    if '*' in operation:
        line_answer = np.prod(line_outputs)
    elif '+' in operation:
        line_answer = np.sum(line_outputs)
    
    outputs.append(line_answer)

print(np.sum(outputs))


