" Write a python program to remove a given word from a list and strip it at the same time.  "

def remove(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item.strip(word))
            
    return n

l = ["apple", "banana", "cherry", "banana", "date"]

print(remove(l, "at"))