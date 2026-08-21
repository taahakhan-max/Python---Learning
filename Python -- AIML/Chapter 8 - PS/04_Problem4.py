"Write a recursive function to calculate the sum of the first n natural numbers."

'''
sum(1) = 1
sum(2) = 1 + 2 = 3
sum(3) = 1 + 2 + 3 = 6
sum(10) = 1 + 2 + 3 + 4 +.... + n - 1 + n 

sum(n) = sum(n-1) + n
'''
def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n

print(sum(10))