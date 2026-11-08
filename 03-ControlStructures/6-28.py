a = 0
b = 1
for i in range(20):
    print(a, end=' ')
    old_b = b
    b = old_b + a
    a = old_b