'''1. Напишіть програму, де клас «геометричні фігури» (Figure) містить
властивість color з початковим значенням white і метод для зміни кольору
фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи
 __init__ для
завдання початкових розмірів об'єктів при їх створенні.'''


class Figure:
    def __init__(self):
        self.color = 'white'

    def change_color(self, new_color):
        self.color = new_color

class Oval(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length


oval = Oval(10, 15)
print(f"Oval color: {oval.color}")
print(f"Oval width: {oval.width}, Oval height: {oval.height}")

oval1 = Oval(2, 3)
oval1.change_color('red')
print(f"Oval color: {oval1.color}")
print(f"Oval width: {oval1.width}, Oval height: {oval1.height}")

square = Square(8)
print(f"Square color: {square.color}")
print(f"Square side length: {square.side_length}")

square1 = Square(5)
square1.change_color('black')
print(f"Square color: {square1.color}")
print(f"Square side length: {square1.side_length}")