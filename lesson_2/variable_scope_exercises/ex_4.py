# What will the following code print and why?
# Don't run it until you have tried to answer.

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# Hello World Hello World

# calling the inner function prints it out, 
# then the outer function calls it again.

# WRONG, it doesnt execute until outer(), which then executes inner() ONE TIME