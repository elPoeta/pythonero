amount_due = 50
inserted_coins = 0

while True:
    coin = int(input('Insert Coin: '))
    if (coin == 25 or coin == 10 or coin == 5):
        inserted_coins += coin
        amount_due -= coin
    if amount_due > 0:
        print(f'Amount Due: {amount_due}')
    else:
        break

print(f'Change Owed: {(inserted_coins - 50)}')
