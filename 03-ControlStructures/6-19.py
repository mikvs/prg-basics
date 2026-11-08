print("--SURVEY--")

first_q = input("Are you intrested in computer science? (y/n): ")
second_q = input("Do you like playing computer games? (y/n): ")
third_q = input("Do you have an Instagram account? (y/n): ")

if first_q == 'y' or first_q == 'Y':
    computer_science = True
else:
    computer_science = False

if second_q == 'y' or second_q == 'Y':
    computer_games = True
else:
    computer_games = False

if third_q == 'y' or third_q == 'Y':
    ig_acc = True
else:
    ig_acc = False


if computer_science:
    computer_science = 'Yes'
else:
    computer_science = 'No'

if computer_games:
    computer_games = 'Yes'
else:
    computer_games = 'No'

if ig_acc:
    ig_acc = 'Yes'
else:
    ig_acc = 'No'

print(f'--SURVEY RESULTS--')
print(f'Intrested in computer science: {computer_science}')
print(f'Playing computer games: {computer_games}')
print((f'Has an Instagram account: {ig_acc}'))