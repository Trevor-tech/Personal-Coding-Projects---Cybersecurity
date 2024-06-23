import random
import string
#is this the comment section lol
def PasswordGenerator(length: int=10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    Password = ''.join(random.choice(alphabet) for i in range(length))
    return Password

Password = PasswordGenerator()
print (f"Password Generator: {Password}")