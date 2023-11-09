'''
5. Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих
 регістро-незалежних букв та цифр, які зустрічаються в рядку більше ніж 1 раз.
 Рядок буде складатися лише з цифр та букв (великих і малих). Реалізуйте
 обчислення за допомогою генератора.
    Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі
'''


def count_repeated_chars(input_string):
    normalized_string = input_string.lower()
    char_count = {}

    for char in normalized_string:
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) + 1

    repeated_chars = [char for char, count in char_count.items() if count > 1]
    return len(repeated_chars)


print(count_repeated_chars("abcde"))
print(count_repeated_chars("aabbcde"))
print(count_repeated_chars("aabBcde"))
print(count_repeated_chars("indivisibility"))
print(count_repeated_chars("^&TFGCQYUTjhg12vasuydmbasjxysdga"))
print(count_repeated_chars("aA11"))
print(count_repeated_chars("ABBA"))
