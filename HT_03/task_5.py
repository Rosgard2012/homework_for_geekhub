"""5. Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary."""

original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

remove_values_dict = {}

for key, value in original_dict.items():
    if value not in remove_values_dict.values():
        remove_values_dict[key] = value


print(f' remove_values_dict  {remove_values_dict }')