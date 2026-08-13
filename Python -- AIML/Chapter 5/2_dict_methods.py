d = {} #empty dictionary
marks = {
    "Taaha":43,
    "Guru" :12, 
    "Nooo" :65
}

# print(marks, type(marks))


# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Majeed": 45, "Taaha": 100})
# print(marks)

print(marks.get("Lama")) # returns None if key is not found
print(marks["Taaha"])    #returns error if key is not found

''' 
Methods: Functions that are associated with a class or object 
and can access or modify the object’s data  

'''