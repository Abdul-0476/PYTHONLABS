size=float(input("Enter the size of data in MBs :"))
x=int(input("How many digits to show after the decimal point?"))
size=round(size/1000,x)
print("Size in GB : ",size)
