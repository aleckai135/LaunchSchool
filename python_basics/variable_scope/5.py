# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# 2, because the variable a is prioritized within the function.
# this is called 'variable shadowing' - WRONG

# it prints - UnboundLocalError: local variable 'a' referenced before assignment
# we are trying to print the local a variable's value before it has been assigned a value