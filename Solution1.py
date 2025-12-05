import numpy as np

my_input_code = "/Users/henrybest/Downloads/input_secret_code.txt"

#define starting lock value
start_val = 50
#values on the lock
n_vals = 100


current_val = start_val

# define counters for each part of the question
counter = 0
counter2 = 0


data = np.loadtxt(my_input_code,dtype=str)


def turn(value, counter=counter, counter2=counter2, current_val=current_val):
    """Simulate turning the dial. I am simply looping through since my previous
    method of floor division and remainder checking was double counting some
    rotations.
    """
    if str(value)[0] == "L":
        for _ in range(int(value[1:])):
            current_val -= 1
            if current_val == 0 or current_val == 100:
                counter2 += 1
            if current_val == -1:
                current_val = 99
        if current_val == 0 or current_val == 100:
            counter += 1
            
    elif str(value)[0] == "R":
        for _ in range(int(value[1:])):
            current_val += 1
            if current_val == 0 or current_val == 100:
                counter2 += 1
            if current_val == 100:
                current_val = 0
        if current_val == 0 or current_val == 100:
            counter += 1
    # return this as a tuple so they update correctly
    return counter, counter2, current_val


for item in data:
    counter, counter2, current_val = turn(
        item, counter=counter, counter2=counter2, current_val=current_val
    )


print(current_val)
print(counter)
print(counter2)
        
