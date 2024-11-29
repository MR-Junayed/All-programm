def find_max(numbers):
    max_value=numbers[0]
    for i in numbers:
        if i>max_value:
            max_value=i
    return max_value
list={45,46,25,16,34}
max1= find_max(list)
print("Max= ",max1)