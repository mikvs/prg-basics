previous_price = 200.00
current_price = float(input("Enter current product price: "))
discount = ((previous_price - current_price) / previous_price) * 100
if current_price < (previous_price * 0.9):
    print("Buy the product!!")
    print(f"Product price reduced by {discount}%")