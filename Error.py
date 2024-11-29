try:
#test the code of a block to diagnosis error.
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a / b
    print(c)
except ZeroDivisionError as e:
    # handle the error
    print(e)
#multiple exception handling
except ValueError as e:
    print(e)
finally:    #it will always print or execute
    print("no matter what code will execute")