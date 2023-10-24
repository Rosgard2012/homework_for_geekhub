'''6. Write a script to get the maximum and minimum value in a dictionary.'''

my_dict = {'a': 9, 'b': 'Vasyl', 'c': [3, 7, 4], 'd': {'x': 10, 'y': 20,'z': 30}, 'e': 115}

def new_key(value):
    if isinstance(value, str):
        return (0, value)
    if isinstance(value, (list, dict)):
        return len(str(value))
    return value


max_value = max(my_dict.values(), key=new_key)
min_value = min(my_dict.values(), key=new_key)


print(f"Max value:    {max_value}")
print(f"Min value:    {min_value}")


'''max_k, max_v = max(d.items(), key=lambda x: x[1])
print(max_k)
# a

print(max_v)
# 100
https://note.nkmk.me/en/python-dict-value-max-min/'''