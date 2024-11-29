person=input("Enter name: ")
mark=int(input("Enter your  mcq mark:"))
if mark>= 40:
    print(f"eligible for written exam")
    mark = int(input("Enter your written mark:"))
    if mark >= 20:
        print(f"eligible for viva")
        mark = int(input("Enter your  viva mark:"))
        if mark >= 4:
            print(f"Congratulations you are appointed for the job")
        else:
            print("not eligible better luck next time")
    else:
        print("not eligible better luck next time")
else:
    print("not eligible better luck next time")