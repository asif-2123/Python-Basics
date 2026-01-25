y=int(input("Enter the year: "))
if (y%4==0 and y%100!=0) or y%400==0:
    print("The answer is: Leap Year")
else:
    print("The answer is: Not a Leap Year")
