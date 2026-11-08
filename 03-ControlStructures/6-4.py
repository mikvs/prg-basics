new_password = input('Enter new password: ')
repeat_password = input('Repeat your password: ')

if new_password == repeat_password:
    if len(new_password) < 12:
        print('Password too short (min. 12 chars)')
    else:
        print('Password confirmed')
else:
    print("The passwords doesnt match! Check the spelling")