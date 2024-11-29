def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
try:
    a=int(input("Num 1: "))
    b=int(input("Num 2: "))
    c=input("Enter to choose operation(+,-,*,/): ")
    if c=='+':
        add_numbers=addition(a,b)
        print(add_numbers)

    elif c=='-':
        sub_numbers=subtraction(a,b)
        print(sub_numbers)

    elif c=='*':
        mul_numbers=multiplication(a,b)
        print(mul_numbers)

    elif c == '/':
        division_numbers=division(a,b)
        print(division_numbers)

    else:
        print("No operation.")


except ZeroDivisionError as e:
    print(e)
except ValueError as e :
    print(e)
