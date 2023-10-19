# 7. Write a script to concatenate all elements in a list into a string and print it. 
#    List must be include both strings and integers and must be hardcoded.

sample_list = [1, '!', 'com', '_', 11, '_', 'Pyton', '_', 2024, 'Viktory']
result = ''

for element in sample_list:
	result += str(element)

print(result)