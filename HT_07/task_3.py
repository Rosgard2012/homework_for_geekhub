"""3. На основі попередньої функції (скопіюйте кусок коду) створити
 наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь
    по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись
    валідатором, перевірить ці дані і надрукує для кожної пари значень
     відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
 P.S. Не забудьте використати блок try/except ;)
"""


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


def validate_credentials(credentials):
    for data in credentials:
        username = data['username']
        password = data['password']
        try:
            validate_username(username)
            validate_password(password)
            additional_rule(username, password)
            print(f"Name: {username}\nPassword: {password}\nStatus: OK")
        except ValueError as e:
            print(f"Name: {username}\nPassword: {password}\nStatus: {e}")
        finally:
            print("-----")




user_data = [
    {"username": "Vasyl", "password": "12345"},
    {"username": "Stepan", "password": "qwert"},
    {"username": "Oksana", "password": "pss0ksana"},
    {"username": "Bohdan", "password": "Bohdan567"},
    {"username": "Iryna", "password": "password1"},
    {"username": "Mykola", "password": "pwd2Mykola"},
    {"username": "Marina", "password": "DRG122*sbword"},
    {"username": "Petro", "password": "password1234"},
]

validate_credentials(user_data)