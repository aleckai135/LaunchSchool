# Write some code that determines and prints whether the number 
# 3 appears inside each of these lists:

def is_three(list):
  for num in list:
    if num == 3:
      print('True')
    else:
      print('False')

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

# is_three(numbers1)
# is_three(numbers2)
# is_three(numbers3)
# is_three(numbers4)
# is_three(numbers5)

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

# You should print True or False depending on each result.