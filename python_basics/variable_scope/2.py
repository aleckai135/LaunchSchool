# What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    global x
    x = x + 5
    print(x)

my_function()

# print 15 since the function looks outside the scope to find the variable x-WRONG

# this will raise an UnboundLocalError, we need to use the global keyword for the 
# function to see x