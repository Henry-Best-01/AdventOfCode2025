import numpy as np


input_text = "/Users/henrybest/Downloads/input_for_day_2.txt"


# load ranges as strings
my_list = np.loadtxt(input_text, delimiter=',', dtype=str)


# given test case
"""
my_list = [
    '11-22',
    '95-115',
    '998-1012',
    '1188511880-1188511890',
    '222220-222224',
    '1698522-1698528',
    '446443-446449',
    '38593856-38593862',
    '565653-565659',
    '824824821-824824827',
    '2121212118-2121212124'
]
"""


total_sum_1 = 0
total_sum_2 = 0

def check_substrings(first_number, last_number):
    """check through each range to find potential substrings"""
    min_str_len = int((np.log10(first_number)+1)/2)
    max_str_len = int((np.log10(last_number)+1)/2)

    invalid_numbers_1 = []
    invalid_numbers_2 = []

    for value in range(first_number, last_number+1):
        test_string = str(value)
        if len(test_string) == 0 or len(test_string) == 1:
            continue
        else:
            # append all answers for solution 1, only requires one check
            if test_string[:len(test_string)//2] == test_string[len(test_string)//2:]:
                invalid_numbers_1.append(int(test_string))

            # find answers for solution 2, requries multiple checks.
            # kk loops over length of possible substrings
            for kk in range(1, 1+len(test_string)//2):
                new_test = test_string[:kk]
                # define a validity check
                is_valid = True
                
                #ll loops over the remainder chunks of the string
                for ll in range(1, len(test_string)//kk):

                    # new_test is everything up to [:kk], so we need to see if
                    # [kk*ll: (ll+1)*kk] is equal to new_test
                    # if not, then make a note it's not a valid answer
                    if test_string[kk*(ll):kk*(ll+1)] != new_test:
                        is_valid = False
                    # if we get to the end and it is still a valid invalid substring, append it 
                    # if is_valid is True:
                    if kk*(ll+1) == len(test_string) and is_valid == True:
                        invalid_numbers_2.append(int(test_string))
                
    return invalid_numbers_1, invalid_numbers_2

# loop through each range
for item in my_list:
    break_index = item.find('-')
    first_num = int(item[:break_index])
    last_num = int(item[break_index+1:])

    current_values_1, current_values_2 = check_substrings(first_num, last_num)
    # remove any duplicates in the second list
    current_values_2 = np.unique(current_values_2)

    total_sum_1 += np.sum(current_values_1)
    total_sum_2 += np.sum(current_values_2)

# print the solutions
print(total_sum_1, total_sum_2)
    
    














