# Take your code from the previous Check the Weather exercise and 
# rewrite it as a match-case statement. 
# Feel free to add more cases besides 'sunny' and 'rainy'.

weather = 'snowy'

match weather:
  case 'sunny':
    print("It's a beautiful day today!")
  case 'rainy':
    print('I need an umbrella.')
  case _:
    print("Let's stay inside.")