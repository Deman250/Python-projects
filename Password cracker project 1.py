from time import time
from itertools import product

password = input("Enter the password: ")
start_time = time()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
characters = letters 

found = False
guesses = 0

for length in range(1, len(password) + 1):
    for attempt in product(characters, repeat=length):
        guess = "".join(attempt)
        guesses += 1
        if guesses % 1_000_000 == 0:
            print(f"...{guesses:,} guesses so far, current length {length}")
        if guess == password:
            end_time = time()
            found = True
            break
    if found:
        break

if found:
    print(f"Password found: {guess}")
    print(f"{password=} : {guesses} guesses")
    print(f"Time taken: {end_time - start_time} seconds")
else:
    print("Password not found.")