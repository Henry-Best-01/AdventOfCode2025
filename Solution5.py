import numpy as np

input_file = "/Users/henrybest/Downloads/input_for_day_5.txt"

# test case
data = [
    '3-5',
    '10-14',
    '16-20',
    '12-18',
    '',
    '1',
    '5',
    '8',
    '11',
    '17',
    '32',
]

data = np.loadtxt(input_file, dtype=str)


# we basically want to make two arrays, and check one against the contents of the other
ranges = []
values = []
for item in data:
    if '-' in item:
        ranges.append(item)
    elif item == '':
        continue
    else:
        values.append(item)

# we can exlude duplicate values in our ranges list (also makes it a numpy array)
#ranges = np.unique(ranges)

fresh_items = []

# now sort into fresh and spoiled items. we know the item id is within a string by
# subtracting it from the boundaries and detecting a sign change in the output.
for item in values:
    for range_of_items in ranges:
        # get the difference between
        index_of_hyphen = range_of_items.find('-')
        first_bound = int(range_of_items[:index_of_hyphen])
        second_bound = int(range_of_items[index_of_hyphen+1:])
        
        check = ((int(item)-first_bound) * (int(item)-second_bound))
        if check <= 0:
            fresh_items.append(item)
            # break so we stop checking more ranges
            break

print(len(fresh_items))



# to get all item ids, we only need to look at the range of items.
# we also need to consider the overlap between ranges.

# make this into a list of tuples instead of a list of strings
tuple_ranges = []
for range_of_items in ranges:
    index_of_hyphen = range_of_items.find('-')
    first_bound = int(range_of_items[:index_of_hyphen])
    second_bound = int(range_of_items[index_of_hyphen+1:])
    tuple_ranges.append((first_bound, second_bound))
    
# sort them by minimum value by making it into a numpy array
tuple_ranges = np.asarray(tuple_ranges)
tuple_ranges = np.sort(tuple_ranges, axis=0)

# join together overlapping ranges
new_tuple_ranges = []

for jj in range(np.size(tuple_ranges, 0)):
    candidate_range = tuple_ranges[jj, :]
    for kk in range(jj+1, np.size(tuple_ranges, 0)):
        # check if the next smallest value is less than the biggest candidate range value
        if tuple_ranges[kk, 0] <= candidate_range[-1]:
            candidate_range[-1] = tuple_ranges[kk, -1]
    # append to our new list if there is a new maximum value
    if jj > 0:
        if candidate_range[-1] > new_tuple_ranges[-1][-1]:
            new_tuple_ranges.append(candidate_range)
    else:
        new_tuple_ranges.append(candidate_range)

new_tuple_ranges = np.asarray(new_tuple_ranges)

# get differences between ranges. plus one is because ranges are inclusive.
range_lengths = new_tuple_ranges[:, -1] - new_tuple_ranges[:, 0] + 1

# finally just print the sum
print(np.sum(range_lengths))











