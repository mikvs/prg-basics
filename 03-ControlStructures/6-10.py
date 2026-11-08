human_age = int(input("Enter the dog's age in human years: "))

if human_age <= 2:
    dog_age = 10.5 * human_age
else:
    dog_age = 21 + (human_age - 2) * 4

print(f"The dog's age in dog's years is {dog_age} years.")