'''6. Write a script to get the maximum and minimum value in a dictionary.'''

my_dict = {'a': 9, 'b': 'Vasyl', 'c': [3, 7, 4], 'e': 115, 'z': 1, 'w': 0, 't': 333}


values = list(filter(lambda value: type(value) in (int, float), my_dict.values()))

min_value = min(values, default=0)
max_value = max(values, default=0)


print(f"Max value:    {max_value}")
print(f"Min value:    {min_value}")


'''max_k, max_v = max(d.items(), key=lambda x: x[1])
print(max_k)
# a

print(max_v)
# 100
https://note.nkmk.me/en/python-dict-value-max-min/
https://realpython.com/python-min-and-max/
'''
