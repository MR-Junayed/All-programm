list=[10,"applr",54,True,2,56,4,3]
x=int(input("Enter position: "))
key=len(list)
print(key)
print("Second Elemnent",list[x])
for i in list:
    print(f"Element {list.index(i)}: {i}")
print(list[1:4])
print(list[4:-1])

my_list = [10, 20, 30]
v=int(input("position="))
my_list[v] = 25
print(my_list)

numbers = [7, 2, 9, 1, 5]
numbers.append(6)
numbers.sort()
print(numbers)