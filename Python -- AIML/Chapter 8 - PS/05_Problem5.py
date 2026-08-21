''' 
Write a program to print first n lines following pattern:

* * *
* *            _ for n = 3
*

'''
def pattern(n):
    if n==0:
        return
    
    print("* " * n)
    pattern(n-1)
 
pattern(3)    
    