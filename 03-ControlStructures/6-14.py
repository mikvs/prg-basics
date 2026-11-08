facebook = True
twitter = False
instagram = True
account_amount = 0
if facebook:
    account_amount += 1
if twitter:
    account_amount += 1
if instagram:
    account_amount += 1
if account_amount >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer!")