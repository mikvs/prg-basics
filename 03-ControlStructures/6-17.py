time_24 = input("Enter time in 24hr format (hh:mm): ")
parts = time_24.split(":")
hour = int(parts[0])
minutes = parts[1]
print(f'Time in 24-hour format: {time_24}')
if hour == 0:
    print(f'Time in 12-hour format: 12:{minutes}am')
if hour >0 and hour <=11:
    print(f'Time in 12-hour format: {hour}:{minutes}am')
if hour == 12:
    print(f'Time in 12-hour format: 12:{minutes}pm')
if hour >12 and hour <= 23:
    print(f'Time in 12-hour format: {hour - 12}:{minutes}pm')