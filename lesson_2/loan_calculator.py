# imports: json config, sub and os for clear terminal
import json
import subprocess
import os

# prompt for language choice
print("For English, type 'en' | Para español, escriba 'es'")
LANG = input()

# json config file
with open('loan.json', 'r') as file:
    MESSAGES = json.load(file)

# function for easier json access
def messages(message, lang):
    return MESSAGES[lang][message]

# function for fancy text for each line
def fancy(key):
    message = messages(key, LANG)
    print(f'--> {message} <--')

# function to clear screen
def clear_screen():
    subprocess.run('clear', shell=True, check = True)

# function for loan formula
def loan_calculation(a, d, r):
    try:
        m = a * (r / (1 - (1 + r) ** (-d)))
    except(ZeroDivisionError):
        m = loan_a / loan_d
    return m

# clear terminal before program start
clear_screen()

# introduction print
fancy('welcome')
print()

# loop for another operation
while True:

    # loan amount validation - variable loan_a
    while True:
        try:
            fancy('loan_a')
            loan_a = int(input('$'))
            if loan_a <= 0:
                raise ValueError
            break
        except(TypeError, ValueError):
            print('\n' + MESSAGES[LANG]['invalid'] + '\n')

    # loan duration in months validation - variable loan_d
    while True:
        try:
            fancy('loan_d')
            loan_d = int(input())
            if loan_d <= 0:
                raise ValueError
            break
        except(TypeError, ValueError):
            print('\n' + MESSAGES[LANG]['invalid'] + '\n')

    # interest rate validation - variable apr_rate
    while True:
        try:
            fancy('apr_rate')
            apr_rate = int(input('% - '))
            apr_rate /= 100
            monthly_apr = apr_rate / 12
            break
        except(TypeError, ValueError):
            print('\n' + MESSAGES[LANG]['invalid'] + '\n')

    # loan calculation
    monthly_loan_total = loan_calculation(loan_a, loan_d, monthly_apr)
    if LANG == 'en':
        print(f'\n--> Monthly Amount: [${monthly_loan_total:.2f}] <--\n')
    elif LANG == 'es':
        print(f'\n--> Monto Mensual: [${monthly_loan_total:.2f}] <--\n')

    # prompt user for another calculation
    while True:
        fancy('another')
        another = input()

        if another in ('y', 'n'):
            break
        print()
        fancy('invalid_another')

    if another == 'n':
        break
    print()

    clear_screen()