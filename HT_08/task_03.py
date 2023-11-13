'''3. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію
цієї функції. Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію
    по ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)).
    Подивіться як веде себе стандартний range в таких випадках.'''


def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("Step cannot be zero")

    if step > 0 and start >= stop:
        return

    if step < 0 and start <= stop:
        raise ValueError("arguments error: start >= stop for negative step")

    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step


if __name__ == '__main__':
    assert list(range(10)) == list(my_range(10))
    assert list(range(1, 11)) == list(my_range(1, 11))
    assert list(range(0, 30, 5)) == list(my_range(0, 30, 5))
    assert list(range(0, 10, 3)) == list(my_range(0, 10, 3))
    assert list(range(0, -10, -1)) == list(my_range(0, -10, -1))
    assert list(range(0)) == list(my_range(0))
    assert list(range(1, 0)) == list(my_range(1, 0))
    assert list(range(1, -10, 5)) == list(my_range(1, -10, 5))
    print('They are identical')

for i in my_range(1, 10, 2):
    print(i)

for i in my_range(0, -10, -1):
    print(i)