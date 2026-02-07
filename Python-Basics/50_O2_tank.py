p=int(input("Enter pressure: "))
t=int(input("Enter temperature: "))
if t>200 and p>80:
    print("Danger")
elif p>100:
    print("Safe")
elif p>=50:
    print("Warning")
else:
    print("Critical")
