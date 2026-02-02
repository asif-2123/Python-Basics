cars=int(input("Enter number of cars: "))
trucks=int(input("Enter number of trucks: "))
total=cars*60+trucks*100
print("Total collection is:",total)
if total>=10000:
    print("Profit")
else:
    print("Loss")
