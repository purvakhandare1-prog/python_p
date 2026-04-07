import random
import string
def password_generator(length):
    characters=string.ascii_letters +string.digits +string.punctuation
    password=""
    for _ in range(length):
        password+=random.choice(characters)
    return password
length=int(input("enter user passwword length"))      
password=password_generator(length)
print(password)
