# This program shows how to use union and intersection of sets in python

s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}

print(s2.union(s3)) # returns a new set with all elements from both sets with no duplicates
print(s2.intersection(s3)) # returns a new set with elements that are common to both sets

s2 - s3 # returns a new set with elements that are in s2 but not in s3
print(s2.difference(s3))

s3 - s2 # returns a new set with elements that are in s3 but not in s2
print(s3.difference(s2))


