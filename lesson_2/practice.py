# switch to virtual environment by typing in terminal: 'act_a' | 'act_b' | 'act_c'
# ensure __init__.py in directory (to utilize .pylintrc configurations)
# _______________________________________________________________________________________________________________________________________________________________________________________________________________________________
def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

print(extract_region('en_US.UTF-8')) # US
print(extract_region('en_GB.UTF-8')) # GB
print(extract_region('ko_KR.UTF-16')) # KR