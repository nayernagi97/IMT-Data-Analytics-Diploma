"""
Create a function that generates a random password 
meeting specific length and character requirements.
"""
import random

def Password_Generator(length, character):
    password = ""
    for _ in range(length):
        password += character[random.randint(0,len(character)-1)]
    
    return password

