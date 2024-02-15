"""
Given a list of numbers, create a new list containing only even 
numbers. (Use list comprehension)
"""

number_list = [1,2,3,4,5,6,7,8,9,10]
even_number_list = [ number for number in number_list if number%2==0]
print(even_number_list)