# Without running the following code, determine what each line should print.

# print('johnson' in 'Joe Johnson') - false
# print('sen' not in 'Joe Johnson') - true
# print('Joe J' in 'Joe Johnson') true
# print(5 in range(5)) false
# print(5 in range(6)) true
# print(5 not in range(5, 10)) false
# print(0 in range(10, 0, -1)) false
# print(4 in {6, 5, 4, 3, 2, 1}) true
print({1, 2, 3} in frozenset({1, 2, 3}))
# print({3, 2} in {1, frozenset({2, 3})}) false