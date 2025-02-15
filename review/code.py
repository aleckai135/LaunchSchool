user_input = int(input('enter a number to be squared: '))

squares = { f'{number}-squared': number * number
 for number in range(1, user_input + 1) }

print(squares)

# pretty-printed for clarity.
{
'1-squared': 1,
'2-squared': 4,
'3-squared': 9,
'4-squared': 16,
'5-squared': 25
}