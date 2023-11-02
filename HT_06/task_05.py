"""5. Написати функцію <fibonacci>, яка приймає один аргумент
 і виводить всі числа Фібоначчі, що не перевищують його."""


def fibonacci(num):
    x, y = 0, 1
    while x <= num:
        print(x)
        x, y = y, x + y


num = int(input("Введіть число: "))

print("Числа Фібоначчі, що не перевищують", num, ":")
fibonacci(num)
