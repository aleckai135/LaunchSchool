# imports
import json
import subprocess
from random import randrange

# clear screen function
def clear_screen():
    subprocess.run('clear', shell=True, check = True)

# config json file for internationalization
with open('rps_comments.json', 'r') as file:
    MESSAGES = json.load(file)

# function for language preference
def lang_pref():
    global LANG

    while True:
        LANG = input("'en' for English | 'es' para Español\n")
        if LANG in ('en', 'es'):
            break

# dictionary for choices
rps_dict = {
        1: 'Rock',
        2: 'Paper',
        3: 'Scissors'
    }

# function for prompt
def prompt(key):
    message = messages(key, LANG)
    print(f'>>> {message} <<<')

# function for user choice
def user_choice():
    while True:
        try:
            user_choice = int(input())
            if (user_choice > 0) & (user_choice < 4):
                break
        except(ValueError):
            'Number must be between 1 and 3'

    global user
    user = rps_dict[user_choice]
    print(f'>>> You chose: {user} <<<')

# function for opponent choice
def opponent_choice():
    opponent_choice = randrange(1, 4)

    global opponent
    opponent = rps_dict[opponent_choice]
    print(f'>>> Opponent chose: {opponent} <<<')

# function for welcome screen
def welcome():
    prompt('welcome')
    print()
    prompt('decision_time')
    prompt('choices')

# game operation algorithm
def rps_game():
    if user == 'Rock' & opponent == 'Rock':
        prompt('tie')
    elif user == 'Rock' & opponent == 'Scissors':
        prompt('win')
    elif user == 'Rock' & opponent == 'Paper':
        prompt('lose')

    if user == 'Scissors' & opponent == 'Scissors':
        prompt('tie')
    elif user == 'Scissors' & opponent == 'Rock':
        prompt('win')
    elif user == 'Scissors' & opponent == 'Paper':
        prompt('lose')

    if user == 'Paper' & opponent == 'Paper':
        prompt('tie')
    elif user == 'Paper' & opponent == 'Rock':
        prompt('win')
    elif user == 'Paper' & opponent == 'Scissors':
        prompt('lose')

# function for ease of use of json file
def messages(message, language):
    return MESSAGES[language][message]

# function to prompt user for another game
def another():
    prompt('again')
    answer = input()
    if answer in ('y', 'n'):
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        prompt('Only "y" or "n" is valid.')

# clears screen before program start
clear_screen()

# main function for entire program
def main():

    # loop to keep playing
    while True:

        # clears screen
        clear_screen()

        # language preference
        lang_pref()

        # welcome
        welcome()

        # user option
        user_choice()

        # opponent choice
        opponent_choice()

        # game algorithm
        rps_game()

        # prompt user for another game
        another()
    
main()