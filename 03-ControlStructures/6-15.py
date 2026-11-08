ean_13 = input("Enter EAN-13 article number: ")
if len(ean_13) == 13:
    print('Article number is correct')
    if ean_13[0:3] == '590':
        print("Article manufactured in Poland")
    else:
        print("Article manufactured not in Poland!")
else: 
    print("Inncorrect article number!")