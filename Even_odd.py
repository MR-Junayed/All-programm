a1=int(input("Enter a number: "))
if a1%2==0:
    print("Number is even.")
else:
    print("Number is odd.")
if a1%3 and a1%5:
    print("Number is divisible by 3 & 5.")
else:
    print("Number is not divisible by 3 & 5.")
if a1%3 or a1%5:
    print("Number is divisible by 3 or 5.")
else:
    print("Number is not divisible by 3 or 5.")