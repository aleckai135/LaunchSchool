# Create a nested dictionary that contains the following data.

# Car

# type	color	year
# sedan	blue	2003

# Truck

# type	color	year
# pickup	red	1998

nested_dict = {
  'Car' : {
    'type' : 'sedan',
    'color' : 'blue',
    'year' : '2003',
  },
  'Truck' : {
    'type' : 'pickup',
    'color' : 'red',
    'year' : 1998
  }
}

print(nested_dict)