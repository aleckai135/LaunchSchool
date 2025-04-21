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
            2: 'Paper',
            3: 'Scissors'
        }
    if LANG == 'es':
        rps_dict = {
            1: 'Roca',
            2: 'Papel',
            3: 'Tijeras'
        }
    
    clear_screen()

# function for prompt
def prompt(key):
    message = messages(key, LANG)
    print(f'>>> {message} <<<\n')

# function for user choice
def user_choice():
    prompt('choices')
    global user
    global user_choi

    while True:
        try:
            user_choi = int(input())

            if user_choi in [1, 2, 3]:
                user = rps_dict[user_choi]
                print(f"\n>>> {messages('user_choice', LANG)}{user}  <<<")
                break

            prompt('error')
        except(ValueError, TypeError):
            prompt('error_type')

# function for opponent choice
def opponent_choice():
    opp_choice = randrange(1, 4)

    global opponent
    opponent = rps_dict[opp_choice]
    print(f">>> {messages('opp_choice', LANG)}{opponent}  <<<")

# game operation algorithm
def rps_game():
    if (user == rps_dict[1]) and (opponent == rps_dict[1]):
        prompt('tie')
    elif (user == rps_dict[1]) and (opponent == rps_dict[2]):
        prompt('win')
    elif (user == rps_dict[1]) and (opponent == rps_dict[3]):
        prompt('lose')
    elif (user == rps_dict[2]) and (opponent == rps_dict[2]):
        prompt('tie')
    elif (user == rps_dict[2]) and (opponent == rps_dict[1]):
        prompt('lose')
    elif (user == rps_dict[2]) and (opponent == rps_dict[3]):
        prompt('win')
    elif (user == rps_dict[3]) and (opponent == rps_dict[3]):
        prompt('tie')
    elif (user == rps_dict[3]) and (opponent == rps_dict[1]):
        prompt('win')
    elif (user == rps_dict[3]) and (opponent == rps_dict[2]):
        prompt('lose')

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

        if answer == 'n':
            break

# START
clear_screen()
main()