'''3. Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль
      (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс
      (файл <{username}_balance.TXT>) та історію транзакцій
      (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова
      перевірка введених даних (введено цифри; знімається не більше,
       ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу
      (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка
      додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете
      реалізувати функціонал додавання нового користувача - не стримуйте
       себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow
       банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль).
       Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
        (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на
         ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне
       завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json
     відповідно)
    P.S.S. Добре продумайте структуру програми та функцій (edited)
'''