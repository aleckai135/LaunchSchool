# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:441:Lee Kim:/home/xyz:/bin/zsh'

parts = info.split(':')

result = '+'.join(parts)

print(result)

# Try this problem using the methods you've learned about in this chapter.
# Once you have that working, use the Python documentation for the str type
#  to find an alternative solution.