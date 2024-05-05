#1
class Animal:
    def __init__(self,name: str, view: str, age:int,speech: str):
        self.name = name
        self.view = view
        self.age = age
        self.speech = speech

animal1 = Animal('barsik','cat',5,'Meeeeeeeew')
print(f'Животное {animal1.name} издает звук {animal1.speech}')
print(f'Информация о животном\nИмя: {animal1.name}\nВид: {animal1.view}\nВозраст: {animal1.age}\nЗвук: {animal1.speech}')

#2
class Book:
    def __init__(self,name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def open_page(self, number_page: int):
        result = f'Страницы {number_page} не существует'
        if number_page > Book1.pages:
            result = result
        else:
            result = f'Страница {number_page} открылась'
        return result

Book1 = Book('Harry Potter','J.K. Rowling',335 )
print(Book1.open_page(34))

