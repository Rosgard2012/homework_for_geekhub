#1. Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The "replacement" value is entered by user.
# The number of elements in the tuples must be different.


tuple_in_list = [
    (325, 'bimba', False, "name"),
    (3.14, "3,14*", "π ", True),
    (100, 'Ukraine', 444, 'Red'),
    (1, 22, 333, 4444, 5555),
    ()
]

replacement = input('Enter the replacement value:  ')

for i in range(len(tuple_in_list)):
    if tuple_in_list[i]:
        tuple_in_list[i] = tuple_in_list[i][:-1] + (replacement,)
    else:
        tuple_in_list[i] = (replacement,)
print(tuple_in_list)
