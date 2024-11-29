add_items = input("Enter an item:")
#n=int(input("Enter number of input: "))
with open("personal1.txt", 'r') as file:
    lines = file.readlines()
    if add_items +"\n" not in lines:
        with open("personal1.txt",'a')as file:
            file.write(add_items +'\n')
            print(f"{add_items} is appended")
    else:
        print(f"{add_items} is already here")
with open('personal1.txt', 'r') as file: