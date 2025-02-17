# Using the following code, compare the value of name with the string 
#   'RoGeR' while ignoring the case of both strings. 
#   Print true if the values are the same; print false if they aren't. 
#   Next, perform a case-insensitive comparison between the value of 
#   name and the string 'DAVE'.

name = 'Roger'

name2 = 'RoGeR'

print(name.casefold() == name2.casefold())

name3 = 'DAVE'

print(name.casefold() == name3.casefold())