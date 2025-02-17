# create a list comprehension from the following dictionary:

cats_colors = {
'Tess': 'brown',
'Leo': 'orange',
'Fluffy': 'gray',
'Ben': 'black',
'Kat': 'orange',
}

# uppercase the names
# limit the results: 
# if the cat is 'orange' 
# if first letter is 'L'

new_list = [ names.upper() 
            for names in cats_colors
            if cats_colors[names] == 'orange'
            if names[0] == 'L' ]

print(new_list)