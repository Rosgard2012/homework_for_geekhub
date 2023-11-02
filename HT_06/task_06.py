"""6. Написати функцію, яка буде реалізувати логіку циклічного
 зсуву елементів в списку. Тобто функція приймає два аргументи:
  список і величину зсуву (якщо ця величина додатня - пересуваємо
   з кінця на початок, якщо від'ємна - навпаки - пересуваємо
    елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]"""


def cyclic_shift(lst, shift):
    if not lst:
        return lst
    shift = shift % len(lst)
    if shift == 0:
        return lst

    if shift > 0:
        return lst[-shift:] + lst[:-shift]
    else:
        return lst[-shift:] + lst[:-shift]


lst1 = [1, 2, 3, 4, 5]
shift1 = 1
shift1 = 3
result1 = cyclic_shift(lst1, shift1)
print(result1)

lst2 = [1, 2, 3, 4, 5]
shift2 = -2
shift2 = -3
result2 = cyclic_shift(lst2, shift2)
print(result2)
