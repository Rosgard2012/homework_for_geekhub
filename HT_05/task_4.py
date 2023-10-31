"""4. Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe
 kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)"""


def process_string(input_string):
    length = len(input_string)
    letters = sum(c.isalpha() for c in input_string)
    digits = sum(c.isdigit() for c in input_string)

    if 30 <= length <= 50:
        print(f"Довжина рядка: {length}")
        print(f"Кількість букв: {letters}")
        print(f"Кількість цифр: {digits}")
    elif length < 30:
        sum_of_digits = sum(int(s) for s in input_string if s.isdigit())
        only_letters = ''.join(c for c in input_string if c.isalpha() and c != ' ')
        print(f"Сума всіх чисел: {sum_of_digits}")
        print(f"Рядок без цифр: {only_letters}")
    elif length > 50:
        modified_string = ''
        for i, char in enumerate(input_string):
            if i % 2 == 0:
                modified_string += char.upper()
            else:
                modified_string += char.lower()
        print(f"Модифікований рядок: {modified_string}")


input_string = input("Введіть рандомний рядок чисел: ")
process_string(input_string)

