#date=input("Enter the DDMMYYYY:")
date="12102024"
length=len(date)
year=int(date[:-5:-1])
print(year)
if year%4==0:
    print("True")
else:
    print("False")