# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of 
# all numbers between 1 and the entered integer, inclusive.

result = int(input('Please enter a number greater than 0: \n'))
result = 0

def sum(num):
    for _ in range(0, num):
        result += _
        return result

def product(num):
    return

print('\nCompute the sum or compute the product?')

while True:
    operation = input('[s] for sum, [p] for product.\n')

    if operation in ('s', 'p'):
        if operation == 's':
            print(f'\nThe sum of the integers between 1 and {result} is '
                  f'{sum(result)}.')
            break

        if operation == 'p':
            print(f'\nThe sum of the integers between 1 and {result} is '
                  f'{product(result)}.')
            break

    print('\nWrong input.')