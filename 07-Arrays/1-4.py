arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[3])
print('Middle value', arr[2])

elementy = '2 '
for i in range(1,len(arr)):
    elementy += str(arr[i]) + ' '
print(elementy)


