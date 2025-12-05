import numpy as np


input_file = "/Users/henrybest/Downloads/input_for_day_4.txt"


# test case
data = [
    list('..@@.@@@@.'),
    list('@@@.@.@.@@'),
    list('@@@@@.@.@@'),
    list('@.@@@@..@.'),
    list('@@.@@@@.@@'),
    list('.@@@@@@@.@'),
    list('.@.@.@.@@@'),
    list('@.@@@.@@@@'),
    list('.@@@@@@@@.'),
    list('@.@.@@@.@.'),
]


# actual case
data = np.loadtxt(input_file, dtype=str)
# massage loaded data into same array like above
all_data = []
for row in data:
    all_data.append(list(row))
data = all_data


# handle edges and corners. also makes this into a numpy array
data = np.pad(data, 1, mode='constant')



counter_1 = 0
counter_2 = 0

# we want to find which objects have less than 4 "@" symbols as neighbors
def check_neighborhood(index_1, index_2):
    # define subgrid, note that index_1 and index_2 have to be increased by
    # 1 to compensate for the padding. Note that making a copy is required,
    # otherwise python will overwrite the actual data with a "0" on the
    # current position
    subgrid = data[index_1:index_1+3, index_2:index_2+3].copy()

    # exclude current position
    subgrid[1, 1] = '0'

    # define a bool mask to see if this is a valid position
    mask = subgrid == '@'

    if np.sum(mask) < 4:
        return 1
        
    else:
        return 0

def check_neighborhood_with_replacement(index_1, index_2):
    # similar to before, but now we want to change the grid as we make
    # progress. Only run this function after counter_1 is computed!

    subgrid = data[index_1:index_1+3, index_2:index_2+3].copy()

    subgrid[1, 1] = '0'
    mask = subgrid == '@'

    if np.sum(mask) < 4:
        # update main grid
        data[index_1+1, index_2+1] = 'x'
        return 1
    else:
        return 0
    
    
# loop through all positions

for jj in range(np.size(data, 0)-1):
    for kk in range(np.size(data, 1)-1):
        if data[jj+1, kk+1] == '@':
            counter_1 += check_neighborhood(jj, kk)

print(counter_1)

# always be careful with while loops. I'm using a break after every
# full cycle
while True:
    check_sum = counter_2
    for jj in range(np.size(data, 0)-1):
        for kk in range(np.size(data, 1)-1):
            if data[jj+1, kk+1] == '@':
                counter_2 += check_neighborhood_with_replacement(jj, kk)
    if counter_2 == check_sum:
        break

print(counter_2)
























