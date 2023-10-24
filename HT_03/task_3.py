'''3. Write a script to concatenate following dictionaries to create a new one.
    dict_1 = {'foo': 'bar', 'bar': 'buz'}
    dict_2 = {'dou': 'jones', 'USD': 36}
    dict_3 = {'AUD': 19.2, 'name': 'Tom'}'''

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

result_dict = dict_1.copy()
result_dict.update(dict_2)
result_dict.update(dict_3)
print(f' Update:                      {result_dict}')

result_dict = dict(list(dict_1.items()) + list(dict_2.items()) + list(dict_3.items()))
print(f' Dict list:                   {result_dict}')

result_dict = {**dict_1, **dict_2, **dict_3}
print(f' ** (розгортання словників) : {result_dict}')