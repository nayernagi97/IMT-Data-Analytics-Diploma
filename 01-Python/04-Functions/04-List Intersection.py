"""
Build a function that finds the common elements between two 
lists and returns them in a new list.
"""

def find_common_elements(first_list, second_list):
    common_elements = []
    for element in first_list:
        if element in second_list:
            common_elements.append(element)
    
    return common_elements
