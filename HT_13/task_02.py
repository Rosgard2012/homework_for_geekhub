'''2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної
 бібліотеки (включіть фантазію). Наприклад вона може містити класи
 Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.books_assigned = []

    def assign_book(self, book):
        self.books_assigned.append(book)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        self.books_taken = []
        self.books_count = 0

    def take_book(self, book):
        self.books_taken.append(book)
        self.books_count += 1


class Author(Person):
    def __init__(self, name):
        super().__init__(name, None)


class Category:
    def __init__(self, name):
        self.name = name


class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category


class Shelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


teacher1 = Teacher("John Doe", 35, "Math")
teacher2 = Teacher("Mate Das", 30, "English")

student1 = Student("Vane Conavan", 15, 9)
student2 = Student("Masha Nenasha", 16, 10)

author1 = Author("Mark Twain")
author2 = Author("Jane Austen")

category1 = Category("Classic")
category2 = Category("Science Fiction")

book1 = Book("Adventures of Huckleberry Finn", author1, category1)
book2 = Book("Pride and Prejudice", author2, category1)
book3 = Book("Dune", author1, category2)
book4 = Book("Emma", author2, category1)
book5 = Book("The Adventures of Tom Sawyer", author1, category1)

shelf = Shelf()
shelf.add_book(book1)
shelf.add_book(book2)
shelf.add_book(book3)
shelf.add_book(book4)
shelf.add_book(book5)


teacher1.assign_book(book1)
teacher1.assign_book(book2)

teacher2.assign_book(book4)


student1.take_book(book1)
student1.take_book(book4)

student2.take_book(book2)
student2.take_book(book3)
student2.take_book(book5)


print(f"{teacher1.name} has assigned the following books:")
for book in teacher1.books_assigned:
    print(f"- {book.title}")

print(f"\n{teacher2.name} has assigned the following books:")
for book in teacher2.books_assigned:
    print(f"- {book.title}")


print(f"\nBooks on shelf: {[book.title for book in shelf.books]}")


print(f"\n{student1.name} (age {student1.age}) has taken "
      f"{student1.books_count} books.")
print(f" books:")
for book in student1.books_taken:
    print(f"- {book.title}")


print(f"\n{student2.name} (age {student2.age}) has taken "
      f"{student2.books_count} books.")
print(f" books:")
for book in student2.books_taken:
    print(f"- {book.title}")
