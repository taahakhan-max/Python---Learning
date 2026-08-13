

s = set()

s.add(20)
s.add(20.2)
s.add('20') 

# length of s after these operations?

print(len(s))  # Output: 2, because 20 and 20.0 are considered the same in a set, while '20' is a different type (string).