txt = input("Enter text: ")[::-1]
print(txt)

def my_function(x):
  return x[::-1]

txt1 = input("Enter text: ")
mytxt = my_function(txt1)

print(mytxt)
def reverse_string(text):
  reversed_string=" "

  for i in text:
    reversed_string=i+reversed_string
    return reversed_string

my_text=input("Enter: ")
r=reverse_string(my_text)
print(r)