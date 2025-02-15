# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

#  the counter needs to be inside the loop, increasing by 1 with each iteration