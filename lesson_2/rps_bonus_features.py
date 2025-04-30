import subprocess
from random import choice

# Constants
VALID_CHOICES = [1, 2, 3, 4, 5]
choices = {
    1: 'Rock',
    2: 'Scissors',
    3: 'Paper',
    4: 'Lizard',
    5: 'Spock'
}

# clear screen function
def clear_screen():
    subprocess.run('clear', shell=True, check = True)

# function for prompt
def prompt(message):
    print(f'>>> {message} <<<\n')

# displays welcome for program start
def display_welcome():
    prompt('Welcome to Rock Paper Scissors!')

# displays choices
def display_choices():
    prompt('1 for Rock - 2 for Scissors - 3 for Paper'
            '- 4 for Lizard - 5 for Spock')

# get and validate user input
def get_validated_user_choice():
    while True:
        try:
            user_choice = int(input())

            if user_choice in VALID_CHOICES:
                return user_choice
            else:
                prompt('Number must be between 1 and 5')

        except(ValueError, TypeError):
            prompt('Only numbers, please.')

# get opponent choice
def get_opponent_choice():
    return choice(VALID_CHOICES)

# display user and opponent choice
def display_choices_made(user_choice, opp_choice):

    print(f"\n>>> You chose: {choices[user_choice]} <<<")
    print(f">>> Opponent chose: {choices[opp_choice]} <<<\n")

# updates scores
def update_scores(user_choice, opp_choice, current_scores):
    user_wins, opp_wins = current_scores

    # Rock[1] | Scissors[2] | Paper[3] | Lizard[4] | Spock[5]
    if ((user_choice == 1 and (opp_choice in (2, 4))) or
        (user_choice == 3 and (opp_choice in (1, 5))) or
        (user_choice == 2 and (opp_choice in (3, 4))) or
        (user_choice == 5 and (opp_choice in (1, 2))) or
        (user_choice == 4 and (opp_choice in (5, 3)))):
        user_wins += 1

    elif ((user_choice == 3 and (opp_choice in (2, 4))) or
          (user_choice == 2 and (opp_choice in (1, 5))) or
          (user_choice == 1 and (opp_choice in (5, 3))) or
          (user_choice == 5 and (opp_choice in (3, 4))) or
          (user_choice == 4 and (opp_choice in (1, 2)))):
        opp_wins += 1

    return (user_wins, opp_wins)

# displays winner
def display_winner(scores):
    user_wins, opp_wins = scores

    print(f">>> You currently have: {user_wins} Wins.  <<<")
    print(f">>> Opponent currently has: {opp_wins} Wins.  <<<\n")

    if user_wins == 3:
        prompt('GAME OVER - you are the CHAMPION!')
    elif opp_wins == 3:
        prompt('GAME OVER - you are the biggest loser there is.')

# reset scores back to 0
def reset_scores_if_needed(scores):
    user_wins, opp_wins = scores

    if user_wins == 3 or opp_wins == 3:
       return (0, 0)
    return scores

# prompts to play again, gets and validates user response
def prompt_play_again(scores):
    user_wins, opp_wins = scores

    if user_wins == 3 or opp_wins == 3:
        prompt('Play Again? y/n')

        while True:
            answer = input()

            if answer in ('y', 'n'):
                return answer
            else:
                prompt("Only 'y' or 'n' is valid.")

# main function for entire program
def main():

    # displays welcome
    display_welcome()

    # Initialize scores
    scores = (0, 0)  # (user_wins, opp_wins)

    # play again loop
    while True:

        # displays choices
        display_choices()

        # user choice and validation
        user_choice = get_validated_user_choice()

        # get opponent choice
        opp_choice = get_opponent_choice()

        # displays user and opponent choice
        display_choices_made(user_choice, opp_choice)

        # who wins
        scores = update_scores(user_choice, opp_choice, scores)

        # displays winner
        display_winner(scores)

        # prompt user for another game, end if 'n'
        answer = prompt_play_again(scores)
        if answer == 'n':
            break
            
        # resets scores to 0 if someone reaches 3
        scores = reset_scores_if_needed(scores)

# START
clear_screen()
main()