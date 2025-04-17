# function for cool prompt text
def prompt(message):
    print(f"==> {message}")

# function for invalid number handling
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

# print greeting
prompt('Welcome to Calculator!')

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
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        output = int(number1) / int(number2)

# print result
prompt(f"The result is {output}")