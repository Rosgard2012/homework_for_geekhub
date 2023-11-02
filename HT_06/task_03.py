"""3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число
 від 0 до 1000, и яка вертатиме True,
 якщо це число просте і False - якщо ні."""


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(number**0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

number_to_check = int(input("Введіть число для перевірки: "))
if is_prime(number_to_check):
    print(f"{number_to_check} є простим числом.")
else:
    print(f"{number_to_check} не є простим числом.")
