"""2. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат
(напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині
викликає 3 попереднi,
обробляє їх результат та також повертає результат своєї роботи. Таким чином ми будемо викликати одну (четверту)
функцiю, а вона в своєму тiлi - ще 3."""


def input_number():
    number = int(input("Введіть число: "))
    if number % 2 == 0:
        return f"Введене число {number} є парним."
    else:
        return f"Введене число {number} є непарним."

def input_string():
    user_input = input("Введіть рядок: ")
    return user_input.upper()

def input_boolean():
    value = input("Введіть 'так' або 'ні' (сюрприз): ")
    return value.lower() == 'ні'

def perform_task(choice):
    if choice == 1:
        return input_number()
    elif choice == 2:
        return input_string()
    elif choice == 3:
        return input_boolean()
    else:
        return "Некоректний вибір завдання."

try:
    user_choice = int(input("Оберіть завдання, введіть номер від 1 до 3: "))
    result = perform_task(user_choice)
    print("Результат: ", result)
except ValueError:
    print("Некоректний ввід.")


