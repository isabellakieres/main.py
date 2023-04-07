def count_vowels(text):
    vowel_sum = 0
    if type(text) == str:
        for char in text:
            if char in "aAeEiIoOuU":
                vowel_sum += 1
        return vowel_sum
    else:
        return 42



def hamming(text1, text2):
    hamming_distance = 0
    if len(text1) != len(text2):
        return 0
    else:
        for i in range (len(text1)):
            if text1[i] != text2[i]:
                hamming_distance += 1
        return hamming_distance



from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

    @abstractmethod
    def __str__(self):
        pass

class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"

class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f'Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}'



class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f'{self.name}, {self.author}'



class BookShelf:
    def __init__(self):
        self.books = []

    def add_book_list(self, books):
        for object in books:
            if isinstance(object, Book):
                self.books.append(object)

    def books_by_author(self, author):
        return [book.name for book in self.books if book.author == author]

    def get_books(self):
        return [book.name for book in self.books]

    def clear_shelf(self):
        self.books.clear()

