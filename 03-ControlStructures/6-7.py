user_age = int(input("How old are you? : "))

if user_age < 13: 
    print("Your age group: Child")
elif user_age >= 13 and user_age <= 19:
    print("Your age group: Teen")
elif user_age >= 20 and user_age <= 64:
    print("Your age group: Adult")
elif user_age >= 65:
    print("Your age group: Senior")