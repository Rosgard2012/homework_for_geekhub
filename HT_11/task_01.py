"""1. Створити клас Calc, який буде мати атребут last_result та 4 методи.
 Методи повинні виконувати математичні операції з 2-ма числами, а саме
  додавання, віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атребута last_result
 він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повинен повернути результат
 виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...
- Додати документування в клас (можете почитати цю статтю:
https://realpython.com/documenting-python-code/ )"""


class Calc:
    def __init__(self):
        self.last_result = None
        print("last_result --> None")

    def add(self, x, y):
        result = x + y
        self.last_result = result
        print(f"last_result --> {self.last_result}")
        print(f"{x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        result = x - y
        self.last_result = result
        print(f"last_result --> {self.last_result}")
        print(f"{x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        result = x * y
        self.last_result = result
        print(f"last_result --> {self.last_result}")
        print(f"{x} * {y} = {result}")
        return result

    def divide(self, x, y):
        result = x / y
        self.last_result = result
        print(f"last_result --> {self.last_result}")
        print(f"{x} / {y} = {result}")
        return result

calc = Calc()
calc.last_result
calc.add(3, 5)
calc.last_result
calc.subtract(3, 5)
calc.last_result
calc.multiply(3, 5)
calc.last_result
calc.divide(3, 5)
calc.last_result