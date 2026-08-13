C1 = "Make a lot of money" 
C2 = "buy now"
C3 = "subscribe this"
C4 = "click this"


message = (input("Enter your comment:"))

if((C1 in message) or (C2 in message) or (C3 in message) or (C4 in message)):
    
    print("This message is spam.")
    
else:
    print(" No Spam")    