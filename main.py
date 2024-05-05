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

