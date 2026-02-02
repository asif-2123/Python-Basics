income=float(input("Enter monthly income: "))
emi=float(input("Enter EMI: "))
if income>=3*emi:
    print("Loan Approved")
else:
    print("Loan Rejected")
