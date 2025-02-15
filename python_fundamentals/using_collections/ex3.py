# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

my_tup = (1,2,3,4,5)

my_list = list(my_tup)

my_list.reverse()

result = tuple(my_list[1:4])

print(result)

# reversed_tuple = (my_tup[3:0:-1])

# print(reversed_tuple)
