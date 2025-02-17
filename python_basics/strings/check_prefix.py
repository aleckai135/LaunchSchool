# Write a function that checks whether a string starts with a specific prefix.

def starts_with(string, string_pre):
  if string.startswith(string_pre):
    return True
  else:
    return False

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True