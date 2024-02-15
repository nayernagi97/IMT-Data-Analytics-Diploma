"""
Create a program that reverses the order of words in a 
sentence without changing word order (e.g., "Hello world" becomes "world 
Hello").
"""

sentence = input("please input the sentence:\n")
word_list = sentence.split(" ")
word_list.reverse()
print("\"{}\" becomes \"{}\"".format(sentence," ".join(word_list)))