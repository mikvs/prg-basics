x = float(input('Enter first number: '))
y = float(input('Enter second number: '))
if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
else: 
    print(f'Both of the numbers {x} and {y} are negative')