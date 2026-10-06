# =================================================
#
# ATM SYSTEM
balance = 50000
while balance != 0:
    amount = int(input('How much do you want to withdraw?'))
    if balance >= amount > 0:
        balance -= amount
        print(f"your current balance is{balance}")
        if balance == 0:
            break
    elif amount > balance:
        print('insufficient funds')
        break

    else:
        print('invalid amount')
