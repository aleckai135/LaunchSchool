import json
import subprocess

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# choose language
while True:
    print('Choose a language: English - "en" | Spanish - "es"')
    LANG = input()

    if LANG in ["en", "es"]:
        break
    print('\nWrong entry.')

    # clears terminal
def clear_screen():
    subprocess.run('clear', shell=True, check = True)

# function that includes unique intro
def prompt(s):
    message = MESSAGES[LANG][s]
    print('\n==> ', message)

# function that catches non-float
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

# Implementation of loop logic.
while True:
    clear_screen()
    print(MESSAGES[LANG]['welcome'])

    # Ask the user for the first number.
    prompt('first')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid')
        number1 = input()

    # Ask the user for the second number.
    prompt('second')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid')
        number2 = input()

    # Ask the user for an operation to perform.
    prompt('operation')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('inv_op')
        operation = input()

    # Perform the operation on the two numbers.
    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)
                

    # Print the result to the terminal.
    print()
    prompt('result')
    print(f'[{output}]')

    # Ask user if they want to run it again.
    prompt('another')

    answer = input()

    while answer not in ['y', 'Y', 'n', 'N']:
        prompt('inv_choice')
        answer = input()

    if answer in ['n', 'N']:
        break