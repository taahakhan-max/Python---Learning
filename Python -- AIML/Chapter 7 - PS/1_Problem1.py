# This program shows the multiplication table of any number in for loop.

value = int(input("Enter a value:"))

i = 1 
j = value
for i in range(1,11):
    print(f"{j} x {i} = {j * i} ")
    