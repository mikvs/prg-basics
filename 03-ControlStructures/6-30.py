for i in range(7):
    row_numbers = [i + 1 + j * 7 for j in range(7)]
    print(" ".join(str(num) for num in row_numbers))