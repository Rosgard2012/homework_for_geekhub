"""Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в float,
 а якщо і там ловить помилку - пропонує ввести значення ще раз (зручніше на даному етапі навчання для
 цього використати цикл while)
Виводить результат ділення першого на друге. Якщо при цьому виникає помилка - оброблює її і виводить
відповідне повідомлення"""

def divide_number(a, b):
    try:
        result = int(a) // int(b)
        return result
    except (ValueError, ZeroDivisionError):
        try:
            result = float(a) / float(b)
            return result
        except (ValueError, ZeroDivisionError):
            return None

while True:
    num1 = input("Введіть перше число: ")
    num2 = input("Введіть друге число: ")

    result = divide_number(num1, num2)

    if result is not None:
        print("Результат ділення:", result)
        break
    else:
        print("Неправильний формат числа або ділення на нуль.")
