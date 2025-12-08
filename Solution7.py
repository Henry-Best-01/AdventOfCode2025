import numpy as np

input_text = "/Users/henrybest/Downloads/input_for_day_7.txt"


# as we saw with solution 6, the numpy loadtxt function does not always
# work as we expect for strings

# test case
test_data = [
    list('.......S.......'),
    list('...............'),
    list('.......^.......'),
    list('...............'),
    list('......^.^......'),
    list('...............'),
    list('.....^.^.^.....'),
    list('...............'),
    list('....^.^...^....'),
    list('...............'),
    list('...^.^...^.^...'),
    list('...............'),
    list('..^...^.....^..'),
    list('...............'),
    list('.^.^.^.^.^...^.'),
    list('...............'),
]

data = []
with open(input_text, 'r') as lines:
    for line in lines:
        # minus one handles the new line character
        data.append(list(line[:-1]))

class tachyon_state:
    def __init__(self, array):
        self.current_state = array
        self.max_propogations = len(array)-1
        self.indicies_to_propogate = []
        for jj, value in enumerate(self.current_state[0]):
            if value == 'S':
                self.indicies_to_propogate.append(jj)
        self.current_prop = 1
        self.total_splits = 0
        self.number_timelines_at_each_position = np.zeros(np.size(array, 1))
        self.number_timelines_at_each_position[
            self.indicies_to_propogate
        ] += 1
    
    def propogate(self):
        # this is the main working method within the class
        indicies_to_remove = []
        if self.current_prop <= self.max_propogations:
            for jj, index in enumerate(self.indicies_to_propogate):
                if self.current_state[self.current_prop][index] == '.':
                    self.current_state[self.current_prop][index] = '|'
                elif self.current_state[self.current_prop][index] == '^':
                    indicies_to_remove.append(index)
                    self.indicies_to_propogate.append(index-1)
                    self.indicies_to_propogate.append(index+1)
                    self.current_state[self.current_prop][index-1] = '|'
                    self.current_state[self.current_prop][index+1] = '|'
                    self.total_splits += 1
                    # when split, the timelines increase in each direction
                    # but get removed from the current location
                    self.number_timelines_at_each_position[
                        index-1
                    ] += self.number_timelines_at_each_position[
                        index
                    ]
                    self.number_timelines_at_each_position[
                        index+1
                    ] += self.number_timelines_at_each_position[
                        index
                    ]
                    self.number_timelines_at_each_position[index] = 0
                    
            # need to remove indicies 
            if len(indicies_to_remove) > 0 and len(self.indicies_to_propogate) > 0:
                temp_list = []
                for jj in range(len(self.indicies_to_propogate)):
                    index = self.indicies_to_propogate[-jj]
                    if index not in indicies_to_remove:
                        temp_list.append(index)
                self.indicies_to_propogate = list(np.unique(temp_list))
                        
            self.current_prop += 1
            return False
        else:
            return self.total_splits, self.number_timelines_at_each_position

        
# initialize the test class
test_case = tachyon_state(test_data)
output_value = False
while output_value is False:
    output_value = test_case.propogate()
print(test_case.current_state)
print(output_value[0], np.sum(output_value[1]))



# initialize the real class
real_case = tachyon_state(data)
output_value = False
while output_value is False:
    output_value = real_case.propogate()
print(output_value[0], np.sum(output_value[1]))








