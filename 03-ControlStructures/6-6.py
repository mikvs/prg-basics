hours = float(input("How many hours the car was parked?: "))

if hours < 1:
    print("No fee")
elif hours >= 1 and hours < 3:
    print("fee of 5PLN")
elif hours >= 3 and hours < 7:
    print("fee of 15PLN")
elif hours > 6:
    print("fee of 20PLN")