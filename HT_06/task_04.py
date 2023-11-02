"""4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок
 і кінець діапазона, і вертатиме список простих чисел всередині
 цього діапазона. Не забудьте про перевірку на валідність
 введених даних та у випадку невідповідності - виведіть повідомлення.
"""


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


def prime_list(start, end):
    if start < 0 or end < 0 or start > end:
        print("Помилка: невірний діапазон")
        return []

    primes = [number for number in range(start, end + 1) if is_prime(number)]
    return primes


start_range = int(input("Введіть початок діапазону: "))
end_range = int(input("Введіть кінець діапазону: "))

prime_numbers = prime_list(start_range, end_range)

if prime_numbers:
    print(f"Прості числа у діапазоні від {start_range} "
          f"до {end_range}: {prime_numbers}")
