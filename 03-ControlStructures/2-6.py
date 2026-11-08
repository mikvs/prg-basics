number = float(input("Enter your number: "))
if number < 0:
    print(f'Number {number} is negative')
elif number == 0:
    print(f'Number is 0')
elif number > 0:
    print(f'Number {number} is positive')
else:
    print(f'You typed {number}. Its not a number!')