# What will the following code print and why? 
# Don't run it until you have tried to answer.

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# 25
# 25

# to utilize inner 1, must use nonlocal before.

# WRONG, the first inner function returns 25, but the second returns 15.
# this is due to func2 only accessing func instead of func1 due to scope.