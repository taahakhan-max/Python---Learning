#This is a simple dictionary program that takes input from the user and returns the corresponding value from the dictionary. It also demonstrates how to update the dictionary with a new key-value pair.

words = {
          "Kutta"  :"Dog",
          "Maddi"  : "Gandu",
          "Shaibu" : "Dalla",
          "Waleed" : "Bhonsrdu",
          "Moazam" : "Billo",
          "Attique": "Bhappu",
          "DC"     : "Bhosdike",
          "Shafee" : "Mai Chittu",
          "Asim"   : "Rana Gandhi",
          "Guru"   : "Chutiya"
        }

word = input("Enter your desire words:")

print(words[word])

words.update({"Mere yaar": "Saare Behenchod"})
