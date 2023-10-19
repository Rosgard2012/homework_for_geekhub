data_input = input("Enter a sequence of numbers separated by commas:  ")
number_list = [int(x) for x in data_input.split(',')]
number_tuple = tuple(number_list)
print("List of entered numbers:", number_list)
print("A tuple of entered numbers:", number_tuple)