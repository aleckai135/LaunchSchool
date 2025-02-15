# Without running this code, what will it print? Why?

import copy as c

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = c.copy(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# [1, 42, 3]

# the dict() constructor creates a shallow copy, thus nested lists are referenced