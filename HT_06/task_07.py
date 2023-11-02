"""7. Написати функцію, яка приймає на вхід список (через кому),
 підраховує кількість однакових елементів у ньомy і виводить результат.
 Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
          1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]
    ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
"""


def count_elements(lst):
    count_temp = {}
    for element in lst:
        key = element if not isinstance(element, list) else str(element)
        if key in count_temp:
            count_temp[key] += 1
        else:
            count_temp[key] = 1

    result = ", ".join(f"{key} -> {value}"
                       for key, value in count_temp.items())
    print(result)


input_list = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]
count_elements(input_list)
