# Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.

# length = float(input('Enter the length in meters: '))

# width = float(input('Enter the width in meters: '))

# area_in_meters = length * width
# area_in_sqft = area_in_meters * 10.7639

# print(f'The area of the room is {area_in_meters:.2f} meters '
#       f'and {area_in_sqft:.2f} square feet.')

# Modify the program to let the user specify the measurement type (meters or feet). 
# Compute the area accordingly and print it and its conversion in parentheses.

length = float(input('Enter the length in meters: '))
width = float(input('Enter the width in meters: '))

area_in_meters = length * width
area_in_sqft = area_in_meters * 10.7639

while True:
    type = input('Measurement type? meters(m)/sqft(f): \n')

    if type in ('m', 'f'):

        if type == 'm':
            print(f'\nThe area of the room is {area_in_meters:.2f} meters '
                f'({area_in_sqft:.2f} square feet.)\n')
            break
            
        if type == 'f':
            print(f'\nThe area of the room is {area_in_sqft:.2f} square feet '
                f'({area_in_meters:.2f} meters.)\n')
            break
        
    print('\nWrong input.')