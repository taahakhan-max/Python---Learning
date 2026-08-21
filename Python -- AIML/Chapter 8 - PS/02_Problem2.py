

def f_to_c(f):
    return (f - 32) * 5/9

f = int(input("Enter temperature in Fahrenheit: "))
c = f_to_c(f)
print(f"{round(c, 2)} degrees Celsius")