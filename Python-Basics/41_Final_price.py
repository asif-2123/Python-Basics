price=float(input("Enter the price: "))
if price>5000:
    discount=price*0.20
elif price>=2000:
    discount=price*0.10
else:
    discount=price*0.05
final=price-discount
print("The final price is:",final)
