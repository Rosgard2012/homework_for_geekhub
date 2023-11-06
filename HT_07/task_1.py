''' 1. Створіть функцію, всередині якої будуть записано список із п'яти
 користувачів (ім'я та пароль). Функція повинна приймати три аргументи:
 два - обов'язкових (<username> та <password>) і третій - необов'язковий
 параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція вертає False
        якщо silent == False -породжується виключення LoginException
         (його також треба створити =))
'''
class LoginException(Exception):
    pass
def check_credentials(username, password, silent=False):
    users = [
        {'username': 'Vasyl', 'password': '12345'},
        {'username': 'Stepan', 'password': 'qwert'},
        {'username': 'Buba', 'password': '123qwe'},
        {'username': 'Reider', 'password': 'ewq321'},
        {'username': 'admin', 'password': 'admin'}
    ]

    for user in users:
        if user['username'] == username and user['password'] == password:
            return True

    if silent:
        return False
    else:
        raise LoginException("Неправильна пара ім'я/пароль")


try:
    username_input = input("Введіть ім'я користувача: ")
    password_input = input("Введіть пароль: ")
    silent_input = input("за замовчуванням = False: ")

    result = check_credentials(username_input, password_input)
    print("Результат:", result)

except LoginException as e:
    print("Помилка:", e)