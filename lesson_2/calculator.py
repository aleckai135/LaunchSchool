import pdb # for debugging purposes - pdb.set_trace()
import json # for storing messages in config file

# function for cool prompt text
def prompt(message):
    print(f"==> {message}")

# function for invalid number handling
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

# json config file for storing messages
with open('comments.json', 'r') as file:
    COMMENTS = json.load(file)

# ask for language preference
print("For english - en | For spanish - es")
LANG = input()

# print greeting
prompt(COMMENTS[LANG]['welcome'])

# another operation loop start
while True:

    # prompt for first number
    prompt("What's the first number?")
    number1 = input()

    # loop for invalid number
    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    # prompt for first number
    prompt("What's the second number?")
    number2 = input()

    # loop for invalid number
    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()

    # prompt for operation
    prompt("What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide")
    operation = input()

    # loop for invalid operation
    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
        operation = input()

    # match/case for operation choice
    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    # print result
    prompt(f"The result is {output}")

    # ask user if go again
    prompt('Would you like to do another operation? (y) ')
    again = input()

    if again != 'y':
        break