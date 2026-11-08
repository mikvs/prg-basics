amount = int(input("Enter number of purchased products: "))
base_price = float(input("Enter product pirce: "))
if amount <= 2:
    amount_to_pay = base_price*amount
elif amount > 2:
    discount = (base_price*amount) * 0.25
    amount_to_pay = (base_price * amount) - discount

print(f"Number of products purchased: {amount}")
print(f"Product price: {base_price}")
print(f"Amount to pay: {amount_to_pay}")