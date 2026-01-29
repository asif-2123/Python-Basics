m=int(input("Enter the month number: "))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print("The number of days is: 31")
elif m==4 or m==6 or m==9 or m==11:
    print("The number of days is: 30")
elif m==2:
    print("The number of days is: 28 or 29")
else:
    print("Invalid month number")
