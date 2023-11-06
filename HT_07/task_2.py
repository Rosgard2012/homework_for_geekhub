'''2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із
   відповідним текстом.'''


def validate_username(username):
    if len(username) < 3 or len(username) > 50:
        raise ValueError("Ім'я повинно бути не меншим за 3 символа "
                         "і не більшим за 50")


def validate_password(password):
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise ValueError("Пароль повинен бути не меншим "
                         "за 8 символів і містити хоча б одну цифру")


def additional_rule(username, password):
    if (username.lower() in password.lower() or password.lower()
            in username.lower()):
        raise ValueError("Пароль не повинен містити "
                         "або повторювати ім'я користувача")


def validate_credentials(username, password):
    validate_username(username)
    validate_password(password)
    additional_rule(username, password)


try:
    username_input = input("Введіть ім'я користувача: ")
    password_input = input("Введіть пароль: ")

    validate_credentials(username_input, password_input)
    print("Пара ім'я/пароль успішно валідована")

except ValueError as e:
    print("Помилка валідації:", e)
