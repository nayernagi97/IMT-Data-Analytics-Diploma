"""
Write a function that takes a list of words and returns the number 
of words starting with a vowel.
"""

def vowel_counter(word_list):
    count = 0
    vowels = ["a", "e", "i","o","u"]
    for word in word_list:
        if word[0].lower() in vowels:
            count +=1
    return count
