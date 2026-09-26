import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(12):  # Generate a password of length 12
    password += random.choice(characters)
    
#print(password)



love = "I love you"
for i in range(1000):
    print(love)

name = "josie"
age = 21
town = "muranga"
print(f"My name is {name}, I am {age} years old and I am from {town}.")

