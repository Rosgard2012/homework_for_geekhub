# 6. Write a script to check whether a value from user input is contained in a group of values.
#    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#         [1, 2, 'u', 'a', 4, True] --> 5 --> False

group_of_values = [1, 2, 'u', 'a', 4, True] 
user_input = input("Enter values: ")
if user_input in group_of_values:
    print("True")
else:
    print("False")

