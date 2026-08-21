" Write a python function which converts inches to centimeters."

def inches_to_cm(inches):
    return inches * 2.54


n = int(input("Enter length in inches: "))

print(f"{n} inches is equal to {inches_to_cm(n)} centimeters")