#Continue
n=int(input("Enter the range: "))
i_start=1
sum=0
for i in range(n+1):
    sum=sum+i
    if i==3:
        continue
    print(f"Sum from {i_start} to {i} is: ",sum)
#Break
i_start=1
sum=0
for i in range(n+1):
    sum=sum+i
    if i==3:
        break
    print(f"Sum from {i_start} to {i} is: ",sum)