balance=int(input("Enter account balance: "))
amount=int(input("Enter withdrawal amount: "))
if amount%100==0 and balance-amount>=500:
    print("Transaction Successful")
else:
    print("Transaction Failed")
