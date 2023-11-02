"""1. Написати функцію <square>, яка прийматиме один аргумент - сторону
 квадрата, і вертатиме 3 значення у вигляді кортежа: периметр квадрата,
  площа квадрата та його діагональ."""


def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = round(side * (2 ** 0.5), 2)
    return perimeter, area, diagonal


side_length = float(input("Введіть довжину сторони квадрата: "))

result = square(side_length)
print(f"Периметр: {result[0]}, Площа: {result[1]}, Діагональ: {result[2]}")
