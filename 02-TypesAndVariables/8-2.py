import math
radius = float(input("Enter radius: "))
if radius > 0:
    circumference = 2 * math.pi * radius
    area = math.pi * math.pow(radius,2)
    print(f'r = {radius} --> circumference = {round(circumference,2)}, area = {round(area,2)}')
else:
    print('Radius cant be lower than one!')