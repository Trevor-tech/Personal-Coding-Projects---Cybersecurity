import random
import string

def PasswordGenerator ():
    alphabet = string.ascii_letters + string.digits + string.punctuation
   
    print ("Welcome to Trevski's Password Generator")
    print ("The home of uncrackable passwords")
   
    PasswordNumber = int(input("How many passwords would you like to generate?"))
    PasswordCharacter = int(input("How many characters should each password have?"))
    
    for number in range (PasswordNumber):
        Password= ''.join(random.choice(alphabet) for character in range(PasswordCharacter))
        print (f"Generated Password: {Password}")
    
PasswordGenerator()
        
    
                         

    