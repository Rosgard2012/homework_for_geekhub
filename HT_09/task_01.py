'''HT #09
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після
   запуска програми на екран виводиться в лівій половині - колір
   автомобільного, а в правій - пішохідного світлофора.
   Кожну 1 секунду виводиться поточні кольори. Через декілька
   ітерацій - відбувається зміна кольорів - логіка така сама як і в
   звичайних світлофорах (пішоходам зелений тільки коли автомобілям
   червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
'''
import time


def traffic_light_cycle(cycles):
    print("Авто-світлофор\t   Пішохідний-світлофор")
    for _ in range(cycles):
        for _ in range(5):
            print("   Green\t      Red")
            time.sleep(1)

        for _ in range(2):
            print("  Yellow\t      Red")
            time.sleep(1)

        for _ in range(5):
            print("   Red\t          Green")
            time.sleep(1)

        for _ in range(2):
            print("  Yellow\t      Red")
            time.sleep(1)


if __name__ == "__main__":
    cycles = int(input("Введіть кількість циклів: "))
    traffic_light_cycle(cycles)