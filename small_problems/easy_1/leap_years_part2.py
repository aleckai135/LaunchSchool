# In the previous exercise, we assumed that the Gregorian calendar has 
# been in continuous use since the year 1. However, the Gregorian 
# calendar wasn't adopted until much later; prior to that, much of 
# the world used the Julian calendar, which observed leap year every 4 years.

# in 1752, England, Ireland, and the British colonies all switched to 
# the Gregorian calendar. Update the function from the previous exercise
# so it uses the Julian calendar prior to 1752, and the Gregorian 
# calendar starting in 1752.

def is_leap_year(num):
    if num >= 1752: # gregorian
        return ((num % 4 == 0) and (num % 100 != 0) or (num % 400 == 0))
    else: # julian
        return num % 4 == 0

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)