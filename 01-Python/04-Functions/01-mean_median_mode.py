"""
Create a function that calculates the 
mean, median, and mode of a list of numbers.
"""
from statistics import mode,mean,median

# def measure_of_center(number_list:list):
#     #calculate mean
#     list_length = len(number_list)
#     list_sum = sum(number_list)
#     mean = list_sum/list_length
#     #calculate meadian
#     number_list.sort()
#     if list_length%2 == 0:
#         median = number_list[list_length//2] + number_list[(list_length//2)-1]
#     else:
#         median = number_list[list_length//2]
#     #calculate mode
#     number_counter = {}
#     for element in number_list:
#         if element in number_counter:
#             number_counter[element] +=1
#         else:
#             number_counter[element] = 1
#     mode = list(number_counter.keys())[list(number_counter.values()).index(max(number_counter.values()))]
#     return mean, median, mode


def measure_of_center(number_list:list):
    return mean(number_list), median(number_list), mode(number_list)
