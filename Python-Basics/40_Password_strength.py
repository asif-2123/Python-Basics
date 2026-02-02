password=input("Enter the password: ")
length=len(password)
if length<6:
    print("Weak Password")
elif length<=10:
    print("Moderate or Strong Password")
else:
    print("Very Strong Password")
