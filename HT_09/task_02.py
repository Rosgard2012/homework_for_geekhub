'''
2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість
   символів. На екран повинен вивестись список із трьома блоками - символи
   з початку, із середини та з кінця файлу. Кількість символів в блоках - та,
   яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів
   більша, ніж є в файлі (наприклад, файл із двох символів і треба вивести по
   одному символу, то що виводити на місці середнього блоку символів?)
   В репозиторій додайте і ті файли, по яким робили тести.
   Як визначати середину файлу (з якої брать необхідні символи) - кількість
   символів поділити навпіл, а отримане "вікно" символів відцентрувати щодо
   середини файла і взяти необхідну кількість. В разі необхідності заокруглення
   одного чи обох параметрів - дивіться на свій розсуд.
   Наприклад:
   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
                     ⏫ центр

   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно

'''


def display_blocks(file_name, block_size):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

            if len(content) < block_size:
                raise ValueError("Кількість символів більша, ніж є в файлі.")

            mid_point = len(content) // 2

            start_mid = max(0, mid_point - block_size // 2)
            end_mid = start_mid + block_size

            print(content[:block_size], end=" ")
            print(content[start_mid:end_mid], end=" ")
            print(content[-block_size:], end=" ")
            print("\n" + "_" * (block_size * 3 + 2))

    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
    except ValueError as ve:
        print(f"Помилка: {ve}")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")


file_name = "for_task_02/test_file.txt"

with open(file_name) as files:
    print(files.read())

block_size = 3
display_blocks(file_name, block_size)
