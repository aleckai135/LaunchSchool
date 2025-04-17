## Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# for num in range(100):
#     if num % 2 != 0:
#         print(num)

## Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# for num in range(1, 100, 2):
#     print(num)

## Consider adding a way for the user to specify the starting and 
## ending values of the odd numbers printed.

number1 = int(input('Starting number: '))

number2 = int(input('Ending number: '))

number3 = int(input('Step: '))

for num in range(number1, number2, number3):
    print(num)