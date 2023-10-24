'''2. Write a script to remove an empty elements from a list.
    Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]'''

Test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

Filtered_list = []

for del_element in Test_list:
    if del_element:
        Filtered_list.append(del_element)

print(f'Test list:   {Test_list}')

print(f'Filtered_list:  {Filtered_list}')