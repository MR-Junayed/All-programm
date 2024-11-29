n=int(input("Enter the number: "))
if n>1:
    for i in range(2,(n//2)+1):
        if (n%i!=0):
            print("The number is prime.")
            break
        else:
            print("The number is not prime")
            break
else:
    ptint("The number is not prime")
