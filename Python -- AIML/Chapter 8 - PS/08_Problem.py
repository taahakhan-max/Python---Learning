"Write a python function to print multiplication table of a given number n using recursion."

    
def multiplication_table(n):   
    for i in range(1, n+1):
        print(f"{n} x {i} = {n*i}")
        
multiplication_table(5)        