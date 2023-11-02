"""5. Написати функцію <fibonacci>, яка приймає один аргумент
 і виводить всі числа Фібоначчі, що не перевищують його."""


def fibonacci(number):
    x, y = 0, 1
    while x <= number:
        print(x)
        x, y = y, x + y


number = int(input("Введіть число: "))

print("Числа Фібоначчі, що не перевищують", number, ":")
fibonacci(number)

