import json
import subprocess
from random import choice

# Constants
VALID_CHOICES = [1, 2, 3, 4, 5]
LANG = 'en'

# globals
rps_dict = {
    1: 'Rock',
    2: 'Scissors',
    3: 'Paper',
    4: 'Lizard',
    5: 'Spock'
}
user_wins = 0
opp_wins = 0
opp = ''
user = ''
answer = ''

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
# def lang_pref():

    # clear_screen()

    # while True:
    #     LANG = input("'en' for English | 'es' para Español\n")
    #     if LANG in ('en', 'es'):
    #         break

    # dictionary for choices (en/es)

    # if LANG == 'es':
    #     rps_dict = {
    #         1: 'Piedra',
    #         2: 'Tijeras',
    #         3: 'Papel'
    #     }

    # clear_screen()

# function for prompt
def prompt(key):
    message = messages(key, LANG)
    print(f'>>> {message} <<<\n')

# function for printing user choice
def user_choice():
    prompt('choices')
    global user

    while True:
        try:
            user = int(input())
            if user in VALID_CHOICES:
                print(f"\n>>> {messages('user_choice', LANG)}"
                      f"{rps_dict[user]}  <<<")
                break

            prompt('error')
        except(ValueError, TypeError):
            prompt('error_type')

# function for printing opp choice
def opponent_choice():
    global opp
    opp = choice(VALID_CHOICES)

    print(f">>> {messages('opp_choice', LANG)}{rps_dict[opp]}  <<<")

# game operation algorithm that prints the winner/loser/tie
def rps_game():
    global user_wins
    global opp_wins

    # Rock[1] | Scissors[2] | Paper[3] | Lizard[4] | Spock[5]
    if ((user == 1 and (opp in (2, 4))) or
        (user == 3 and (opp in (1, 5))) or
        (user == 2 and (opp in (3, 4))) or
        (user == 5 and (opp in (1, 2))) or
        (user == 4 and (opp in (5, 3)))):

        prompt('win')
        user_wins += 1
        print(f">>> {messages('user_current_wins', LANG)}"
              f"{user_wins} Wins.  <<<")

        if user_wins == 3:
            prompt('grand_win')
            user_wins = 0
            opp_wins = 0

        elif opp_wins == 3:
            prompt('grand_loser')
            user_wins = 0
            opp_wins = 0

    elif ((user == 3 and (opp in (2, 4))) or
          (user == 2 and (opp in (1, 5))) or
          (user == 1 and (opp in (5, 3))) or
          (user == 5 and (opp in (3, 4))) or
          (user == 4 and (opp in (1, 2)))):

        prompt('lose')
        opp_wins += 1
        print(f">>> {messages('opp_current_wins', LANG)}"
              f"{opp_wins} Wins.  <<<")

        if user_wins == 3:
            prompt('grand_win')
            user_wins = 0
            opp_wins = 0

        elif opp_wins == 3:
            prompt('grand_loser')
            user_wins = 0
            opp_wins = 0

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

    # welcome
    prompt('welcome')

    # play again loop
    while True:

        # user option
        user_choice()

        # opp choice
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