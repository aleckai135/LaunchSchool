# imports
import json
import subprocess
from random import randrange

# Constants
VALID_CHOICES = [1, 2, 3]

# clear screen function
def clear_screen():
    subprocess.run('clear', shell=True, check = True)

# config json file for internationalization
with open('rps_comments.json', 'r') as file:
    MESSAGES = json.load(file)

# function for ease of use with json file
def messages(message, language):
    return MESSAGES[language][message]

# function for language preference
def lang_pref():
    global LANG
    global rps_dict

    clear_screen()

    while True:
        LANG = input("'en' for English | 'es' para Español\n")
        if LANG in ('en', 'es'):
            break

    # dictionary for choices (en/es)
    if LANG == 'en':
        rps_dict = {
            1: 'Rock',
            2: 'Scissors',
            3: 'Paper'
        }
    if LANG == 'es':
        rps_dict = {
            1: 'Piedra',
            2: 'Tijeras',
            3: 'Papel'
        }
    
    clear_screen()

# function for prompt
def prompt(key):
    message = messages(key, LANG)
    print(f'>>> {message} <<<\n')

# function for printing user choice
def user_choice():
    prompt('choices')
    global user
    global user_choi

    while True:
        try:
            user_choi = int(input())

            if user_choi in VALID_CHOICES:
                user = rps_dict[user_choi]
                print(f"\n>>> {messages('user_choice', LANG)}{user}  <<<")
                break

            prompt('error')
        except(ValueError, TypeError):
            prompt('error_type')

# function for printing opponent choice
def opponent_choice():
    opp_choice = randrange(1, 4)

    global opponent
    opponent = rps_dict[opp_choice]
    print(f">>> {messages('opp_choice', LANG)}{opponent}  <<<")

# game operation algorithm that prints the winner/loser/tie
def rps_game():

    # Rock[1] | Scissors[2] | Paper[3]
    if ((user == rps_dict[1] and opponent == rps_dict[2]) or
        (user == rps_dict[3] and opponent == rps_dict[1]) or
        (user == rps_dict[2] and opponent == rps_dict[3])):
        prompt('win')

    elif ((user == rps_dict[3] and opponent == rps_dict[2]) or
          (user == rps_dict[2] and opponent == rps_dict[1]) or
          (user == rps_dict[1] and opponent == rps_dict[3])):
        prompt('lose')

    else:
        prompt('tie')

# function to prompt user for another game
def another():
    prompt('again')

    while True:
        global answer
        answer = input()

        if answer in ('y', 'n'):
            if answer == 'y':
                break
            break

        prompt('again_invalid')

    clear_screen()

# main function for entire program
def main():

    # language preference
    lang_pref()

    # welcome
    prompt('welcome')

    # play again loop
    while True:

        # user option
        user_choice()

        # opponent choice
        opponent_choice()

        # game algorithm
        rps_game()

        # prompt user for another game
        another()

        # break out of loop condition
        if answer == 'n':
            break

# START
clear_screen()
main()