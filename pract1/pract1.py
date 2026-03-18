# Level 1
#3.	Створіть програму, яка приймає два числа від користувача та виводить їх суму.

def user_sum():
    a = int(input("Enter first num: "))
    b = int(input("Enter second num: "))
    print(a + b)

print("Level 1")
user_sum()

# Level 2
# 3. Реалізуйте програму, яка визначає, чи є введене користувачем число простим.

def is_prime(num):
    if num <= 1:
        False
        return
    for i in range(2, num):
        if num % i == 0:
            False
            return
    return True

def is_prime_range(start, end):
    for i in range(start, end):
        if is_prime(i):
            print(f"Prime {i}")
        else:
            print(f"Not prime {i}")

print("Level 2")

is_prime_range(2, 10)

# Level 3
# 3. Створіть клас "Калькулятор" з методами для додавання, віднімання, множення та ділення. 
# Виведіть результат обчислень для певного прикладу.

class Calculator: 
    
    @staticmethod
    def add(*nums):
        result = 0
        for num in nums:
            result += num
        return result

    @staticmethod
    def sub(*nums):
        result = nums[0]
        for num in nums[1:]:
            result -= num
        return result
    
    @staticmethod
    def  mul(*nums):
        result = 1
        for num in nums:
            result *= num
        return result

    @staticmethod
    def div(*nums):
        result = nums[0]
        for num in nums[1:]:
            if num == 0:
                return result
            result /= num
        return result

print("Level 3")
print(Calculator.add(1, 2, 3))
print(Calculator.sub(7, 2, 1))
print(Calculator.mul(1, 2, 3))
print(Calculator.div(10, 2))

#Level 4
# 3.Створіть клас "Книготека" з можливістю додавання та видалення книг, 
# а також виведення списку усіх книг.

class Page:
    def __init__(self, text, num):
        self.text = text
        self.num = num

class Book:
    def __init__(self, title, description, author_name, pages):
        self.title = title
        self.description = description
        self.author_name = author_name
        self.pages = pages

    def print_book_info(self):
        print("Title:", self.title)
        print("Author:", self.author_name)
        print("Description:", self.description)
        print("Pages:", len(self.pages))

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == str.strip(title):
                self.books.remove(book)
                return

    def print_books(self):
        for book in self.books:
            book.print_book_info()

print("Level 4")
p1 = Page("Page text 1", 1)
p2 = Page("Page text 2", 2)

book1 = Book("Python Basics", "Learning Python", "John Smith", [p1, p2])

library = Library()
library.add_book(book1)
library.print_books()
library.remove_book("Python Basics")
library.print_books()
