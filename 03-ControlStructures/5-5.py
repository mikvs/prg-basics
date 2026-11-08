total_sum = 0
counter = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break

    counter += 1
    total_sum += number

average = total_sum/counter
print(f"The total sum of the numbers is: {total_sum}")
print(f"The average is: {average}")