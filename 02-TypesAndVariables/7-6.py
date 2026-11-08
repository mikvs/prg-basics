vehicle_speed=int(input('Enter vehicle speed: '))
speed_ok = vehicle_speed >= 40 and vehicle_speed <= 140
print(f'Speed is valid: {speed_ok}')