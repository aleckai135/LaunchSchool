## create a function that returns first letter of user input

# define function
def lower_first(word):
    try:
        return word[0].lower() + word[1:]
    except (TypeError, IndexError, ValueError):
        return word

# create a while loop to continue
while True:

# prompt user for input
    user_input = input('Enter a word to lower the first letter: ')

#   perform operation
    print(lower_first(user_input))

#   validate user input for another

    while True:
        again = input('\nAnother? y/n - ')

        if again in ('y', 'n'):
            if again == 'y':
                break
            
            break
        
        print('Wrong input.')

    if again == 'n':
        break