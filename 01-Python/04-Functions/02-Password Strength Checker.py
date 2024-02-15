"""
Design a function that checks the strength of a 
password based on length, special characters, and uppercase/lowercase 
requirements.
"""

def password_checker(password:str):
    strength = 0
    length = len(password)
    special_chracters = "@#$%^&*!"
    upper_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_characters = "abcdefghijklmnopqrstuvwxyz"

    if length > 8:
        strength +=1

    if any(char in special_chracters for char in password):
        strength += 1

    if any(char in upper_characters for char in password):
        strength += 1

    if any(char in lower_characters for char in password):
        strength += 1

    if strength <= 2 :
        return "weak password"
    
    if strength > 2:
        return "strong password"
