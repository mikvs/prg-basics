number1 = int(input('Please enter first number: '))
number2 = int(input('Please enter second number: '))
operator = input('Please enter a symbol of mathematical operation (+,-,*,/): ')
if operator == '+':
    result = number1+number2
elif operator == '-':
    result = number1-number2
elif operator == '*':
    result = number1*number2
elif operator == '/':
    result = number1/number2
else:
    print('Wrong symbol!')
# print result
print(f'{number1} {operator} {number2} = {result}')