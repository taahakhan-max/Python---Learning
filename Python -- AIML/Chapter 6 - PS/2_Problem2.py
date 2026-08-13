marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
marks4 = int(input("Enter marks for subject 4: "))


# For total percentage calculation

total_percentage = (100 * (marks1 + marks2 + marks3 + marks4)) / 400
'''
if(total_percentage >= 90):
    print("Grade: A")
    
elif(total_percentage >= 80):
    print("Grade: B")
    
elif(total_percentage >= 70):
    print("Grade: C")
    
elif(total_percentage >= 60):
    print("Grade: D")
            
elif(total_percentage >= 50):
    print("Grade: E")
    
else:
    print("Grade: F")
    print("You have failed the exam. Please try again.")
                                    
print("Total percentage: ", total_percentage) '''

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and marks4 >= 33):
    print("Congratulations! You have passed the exam.")
    
else:
    print("You have failed the exam. Please try again.")    