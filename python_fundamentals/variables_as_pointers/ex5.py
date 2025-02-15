# The following program is nearly identical to that of the previous exercise. 
# However, this time, it should create a shallow copy of dict1. 
# Be careful: you're not allowed to use the copy module in this exercise.

# In addition, before you run this code, can you predict the output values?

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part of this line

print(dict1         is dict2) # no
print(dict1['a']    is dict2['a']) # yes
print(dict1['a'][0] is dict2['a'][0]) # yes
print(dict1['a'][1] is dict2['a'][1]) # yes
print(dict1['b']    is dict2['b']) # yes
print(dict1['b'][0] is dict2['b'][0]) # yes
print(dict1['b'][1] is dict2['b'][1]) # yes

# everything after line 14 is part of a nested list, which are all references to the original
# nested objects, thus the remaining are True.