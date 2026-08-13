
# If-Elif-Else Ladder

Age = int(input("Enter your age: "))

if(Age>18):
    print("You are above the age of consent.")
    print("good for you.")
    
elif(Age<0):
    print("Aby bhaeee pagal hai kya? Age negative kaise ho sakta hai?")
        
elif(Age==0):
    print("Nunno mai hai kya.")
    
else: 
    print("You are below the age o consent.")
    
print("End of program.")