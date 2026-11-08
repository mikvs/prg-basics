input_number = (input("Enter your decimal number: "))
decimal_number = int(input_number)
binary = ""
while decimal_number > 0:
    remainder = decimal_number%2
    decimal_number //= 2
    binary = str(remainder) + binary
print(f'{input_number}(10) = {binary}(2)')