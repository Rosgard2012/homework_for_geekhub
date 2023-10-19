# 2. Write a script which accepts two sequences of comma-separated colors from user. 
#    Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_list_1 = input("Enter colors for color_list_1, separated by commas: ").split(',')
color_list_2 = input("Enter colors for color_list_2, separated by commas: ").split(',')

set_color_1 = set(color_list_1)
set_color_2 = set(color_list_2)

difference_set = set_color_1 - set_color_2

print("Set of unique colors for color_list_1: ", difference_set)