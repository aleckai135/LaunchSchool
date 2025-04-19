# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or the product of
# all numbers between 1 and the entered integer, inclusive.

user_input = int(input('Please enter a number greater than 0: \n'))

def product(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print('\nCompute the sum or compute the product?')

while True:
    operation = input('[s] for sum, [p] for product.\n')

    if operation in ('s', 'p'):
        if operation == 's':
            sum_num = sum(range(user_input + 1))
            print(f"""\nThe sum of the integers between 1
                  and {user_input} is {sum_num}.""")
            break

        if operation == 'p':
            print(f"""\nThe product of the integers between 1 and
                  {user_input} is {product(user_input)}.""")
            break

    print('\nWrong input.')