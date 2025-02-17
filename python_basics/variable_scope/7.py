# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# prints 2, since we use the global keyword, we can modify the a variable.