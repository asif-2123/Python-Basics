amount=int(input("Enter amount: "))
if amount%10!=0:
    print("Invalid amount")
else:
    n500=amount//500
    amount=amount%500
    n100=amount//100
    amount=amount%100
    n10=amount//10
    print("500 notes:",n500)
    print("100 notes:",n100)
    print("10 notes:",n10)
