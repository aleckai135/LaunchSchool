# What will the following code do and why? 
# Don't run it until you have tried to answer.

if True:
    my_value = 20

print(my_value)

# it will print 20 since anything above 0 is considered truthy

# How about this code, instead:

if False:
    my_new_value = 42

print(my_new_value)

# NameError since the value is never intialized