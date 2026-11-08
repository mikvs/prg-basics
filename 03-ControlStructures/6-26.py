pin_code = '0805'
amount_of_tries = 0
for i in range(0,3):
    attempts = input("Enter the PIN code: ")
    if attempts != pin_code:
        print('Incorrect...')
        amount_of_tries += 1
    else:
        print('Payment went through')
        break
if amount_of_tries == 3:
    print('Sorry, your payment card has been blocked')