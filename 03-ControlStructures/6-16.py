washing_product = input("Select washing program: (j)acket, (u)nderwear, (s)hoes ")
rinse = input("Extra rinse? (y/n) ")
spin = input("Extra spin? (y/n ")

washing_time = 0

if washing_product == 'j' or washing_product == 'J':
    washing_time += 40
    washing_product = 'Jacket'
if washing_product == 'u' or washing_product == 'U':
    washing_time += 70
    washing_product = 'Underwear'
if washing_product == 's' or washing_product == 'S':
    washing_time += 20
    washing_product = 'Shoes'
else:
    print("Wrong character typed!")


if rinse == 'y' or rinse == 'Y':
    rinse = True
    spin = False
    washing_time += 15
elif spin == 'y' or spin == 'Y':
    spin = True
    rinse = False
    washing_time += 9
else:
    print("Wrong character typed!")

print(f'Washing product: {washing_product}')
print(f'Rinse: {rinse}')
print(f'Spin: {spin}')
print(f'Total washing time: {washing_time}')