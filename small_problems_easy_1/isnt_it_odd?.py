# Write a function that takes one integer argument and returns 
# True when the number's absolute value is odd, False otherwise.

def odd_num(num):
    return num % 2 != 0

print(odd_num(5))