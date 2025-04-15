# function that includes unique intro

def prompt(s):
    print('==> ', s)

# function that catches non-int

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

# Implementation of loop logic.

while True:

  print('Welcome to Calculator!')

  # Ask the user for the first number.

  prompt('Enter first number:')
  number1 = input()

  while invalid_number(number1):
      prompt("Hmm... that doesn't look like a valid number.")
      number1 = input()

  # Ask the user for the second number.

  prompt('Enter second number:')
  number2 = input()

  while invalid_number(number2):
      prompt("Hmm... that doesn't look like a valid number.")
      number2 = input()

  # Ask the user for an operation to perform.

  prompt('Enter desired operation:\n' \
  '1. add 2. subtract 3. multiply 4. divide')
  operation = input()

  while operation not in ["1", "2", "3", "4"]:
      prompt('You must choose 1, 2, 3, or 4')
      operation = input()

  # Perform the operation on the two numbers.

  match operation:
      case '1':
          output = int(number1) + int(number2)
      case '2':
          output = int(number1) - int(number2)
      case '3':
          output = int(number1) * int(number2)
      case '4':
          output = int(number1) / int(number2)

  # Print the result to the terminal.

  print()
  prompt(f'The result is: {output}\n')

  # Ask user if they want to run it again.

  prompt('Another one? y/n')

  answer = input()

  while answer not in ['y', 'Y', 'n', 'N']:
      prompt('Please put in y/n')
      answer = input()

  if answer in ['n', 'N']:
      break
  
  print()