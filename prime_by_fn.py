def is_prime(n):
    if n<=1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
n1=int(input("Enter the number: "))
if is_prime(n1):
    print("prime")
else:
    print("Not prime")