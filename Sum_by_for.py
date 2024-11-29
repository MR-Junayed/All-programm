n=int(input("Enter the range: "))
i_start=1
sum=0
for i in range(n+1):
    sum=sum+i
print(f"Sum from {i_start} to {n} is: ",sum)