print('Welcome to Calculator!')

# Ask the user for the first number.

print('Enter first number:')
number1 = input()

# Ask the user for the second number.

print('Enter second number:')
number2 = input()

# Ask the user for an operation to perform.

print('Enter desired operation:\n' \
'1. add 2. subtract 3. multiply 4. divide')
operation = input()

# Perform the operation on the two numbers.

if operation == '1':
  output = int(number1) + int(number2)
elif operation == '2':
  output = int(number1) - int(number2)
elif operation == '3':
  output = int(number1) * int(number2)
elif operation == '4':
  output = int(number1) / int(number2)

# Print the result to the terminal.

print(f'The result is: {output}')
