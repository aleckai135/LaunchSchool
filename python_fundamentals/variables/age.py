age = int(input('how old are you? '))

print(f'You are {age} years old.')
counter = 0
years = 10

while counter < 4:
  print(f'In {years} years, you will be {age + years} years old.')
  years += 10
  counter += 1