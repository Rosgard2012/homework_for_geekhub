"""5. Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя,
яка б приймала 3 аргументи - один з яких операцiя, яку зробити! Аргументи брати від юзера
(можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2).
Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями
на предмет помилок!"""


def calculator(num1, operator, num2):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        elif operator == '%':
            return num1 % num2
        elif operator == '//':
            return num1 // num2
        elif operator == '**':
            return num1 ** num2
        else:
            return "Неправильний оператор. Використовуйте: +, -, *, /, %, //, **"
    except ZeroDivisionError:
        return "Ділення на нуль неможливе!"

try:
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть операцію (+, -, *, /, %, //, **): ")
    num2 = float(input("Введіть друге число: "))

    result = calculator(num1, operator, num2)
    print(f"Результат: {result}")
except ValueError:
    print("Некоректне введення числа!")
