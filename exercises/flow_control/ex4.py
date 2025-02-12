def all_caps_if_ten_characters(word):
  if len(word) > 10:
    print(word.upper())
  else:
    print(word)

user_input = input('Enter a word: ')

all_caps_if_ten_characters(user_input)