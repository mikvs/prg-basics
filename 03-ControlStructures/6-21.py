amount = int(input("Enter the amount in PLN: "))
five_pln = amount//5
rest_of_five = amount % 5
two_pln = rest_of_five//2
rest_of_two = rest_of_five % 2
one_pln = rest_of_two
print(f'The amount of {amount} PLN in coins: ')
print(f'5 PLN coins: {five_pln}')
print(f'2 PLN coins: {two_pln}')
print(f'1 PLN coins: {one_pln}')