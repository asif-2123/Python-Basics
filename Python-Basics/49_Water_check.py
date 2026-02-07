liters=float(input("Enter canteen capacity in liters: "))
km=int(input("Enter total distance in km: "))
needed=km*0.25
if liters>=needed:
    print("Yes, enough water")
else:
    print("Additional water needed:",needed-liters,"liters")
