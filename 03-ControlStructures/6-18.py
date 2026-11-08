point = input("Enter coordinates of your point [P(x,y)]: ")
coordinates = point.split(",")
x = int(coordinates[0])
y = int(coordinates[1])
print(f'x = {x}')
print(f'y = {y}')
if x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
elif x > 0 and y < 0:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')
elif x == 0 and y == 0:
    print(f'Point P({x},{y}) is located at the origin of the coordinate system')
elif x == 0:
    print(f'Point P({x},{y}) is located on Y axis')
elif y == 0:
    print(f'Point P({x},{y}) is located on X axis')