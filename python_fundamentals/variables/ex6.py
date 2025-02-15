# Which of the subsequent statements reassign the variable? 
# Which statements mutate the value of the object that obj references? 
# Which statements do neither?

# obj = 'ABcd' - reassign
# obj.upper() - neither
# obj = obj.lower() - reassign
# print(len(obj)) - neither
# obj = list(obj) - reassign
# obj.pop() - mutates
# obj[2] = 'X' - mutates
# obj.sort() - mutates
# set(obj) - neither
# obj = tuple(obj) - reassign