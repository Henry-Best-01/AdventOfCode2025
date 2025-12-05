import numpy as np


input_code = "/Users/henrybest/Downloads/input_for_day_3.txt"

# test case
batteries = [
    '987654321111111',
    '811111111111119',
    '234234234234278',
    '818181911112111'
]

# from file
batteries = np.loadtxt(input_code, dtype=str)


# counters to store values
counter_1 = 0
counter_2 = 0


# since you must read the joltage from left to right and need 2 values,
# the largest total joltage will have the highest number in your string
# excluding the last position. This function is recyclable for the second
# value by feeding in the remaining substring.
def find_largest_int_position(string):
    
    code_as_list = list(string)
    list_as_numbers = np.asarray(code_as_list, dtype=int)

    return np.argmax(list_as_numbers)

# cycle through batteries
for item in batteries:
    # case 1, only 2 batteries of each bank
    index_1 = find_largest_int_position(item[:-1])
    index_2 = find_largest_int_position(item[index_1+1:])

    # since they're still strings, you can concatenate them and then convert
    # to an int.
    joltage_of_battery = int(item[index_1] + item[index_2+index_1+1])

    counter_1 += joltage_of_battery

    # case 2, 12 batteries of each bank
    # define an empty string to store values in
    joltage_of_battery = ''
    start_index = 0

    for jj in range(12):
        # we want to define substrings of potential cells to turn on at each position
        last_index = len(item[start_index:])

        index = find_largest_int_position(item[start_index:start_index+last_index-11+jj])
        # concatenate the chosen index and increment the substring index
        joltage_of_battery += item[start_index+index]
        start_index += index + 1
    # convert to int and add to counter
    joltage_of_battery = int(joltage_of_battery)

    counter_2 += joltage_of_battery
        


print(counter_1)
print(counter_2)























