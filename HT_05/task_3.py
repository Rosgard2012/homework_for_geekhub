"""3. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями. 
Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде 
перевiрятися рiвнiсть змiнних "x" та "y" та у випадку нервіності - виводити ще і різницю.
    Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      вiдповiдь - "х дорiвнює z"""


def compare_numbers(x, y):
    if x > y:
        print(f"x більше, ніж y на {x - y}")
    elif x < y:
        print(f"y більше, ніж x на {y - x}")
    else:
        print("x дорівнює y")

try:
    x = float(input("Введіть значення x (число): "))
    y = float(input("Введіть значення y (число): "))
except ValueError:
    print('Ви ввели не числа!')
else:
    compare_numbers(x, y)

