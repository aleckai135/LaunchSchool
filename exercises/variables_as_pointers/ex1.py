# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# {42, 'Monty Python', ('a', 'b', 'c'), (range(5, 10))}

# due to the collection being a set, the above result will probably be different after
# every print. set1 and set2 reference the same object, so any changes to the collection
# will show for both sets.