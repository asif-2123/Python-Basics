n=int(input("Enter the number: "))
last=n%10
second=(n//10)%10
rest=n//100
result=rest*100+last*10+second
print("The answer is:",result)
