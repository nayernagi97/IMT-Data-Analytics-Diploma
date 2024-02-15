"""
Count Vowels: Write a program that counts the number of vowels in a given 
string.
"""
vowels = ["a", "e", "i","o","u"]
word = input("please input the Word:\n").lower()
count = 0

for vowel in vowels:
    count += word.count(vowel)

print("The Number of Vowels in the Word was: {}".format(count))