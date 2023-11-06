"""7. Написати функцію, яка приймає на вхід список (через кому),
 підраховує кількість однакових елементів у ньомy і виводить результат.
 Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
          1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]
    ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
"""


def count_elements(lst):
    counts = {}
    for item in lst:
        key = str(item)
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    result = []
    for item, count in counts.items():
        result.append(f"{item} -> {count}")
    return ", ".join(result)


input_list = [1, 1, 'foo', [1, 2], 1, [1, 2], {'a': 1}, True, False, {1, 2}]
print(count_elements(input_list))