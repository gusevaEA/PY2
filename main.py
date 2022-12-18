# TODO Написать 3 класса с документацией и аннотацией типов
class Passport:
    def __init__(self,nationality, name,date):
        # Атрибутам присваиваются значения аргументов конструктора объекта
        self.nationality = nationality
        self.name = name
        self.date = date

    def show_status(self):
        print(f'{self.name} arrived')

class Book:
    def __init__(self,name,author,country):
        self.name = name
        self.author = author
        self.country = country

    def read(self):
        print(f'{self.name} read')

    def get_author(self):
        return self.author

class Animals:
    def __init__(self,type,color,weight):
        self.type = type
        self.color = color
        self.weight = weight

    def get_weight_kg(self):
        """
        Класс Passport,Book,Animals
        Извлечение

        :return:
        """
        return self.weight/1000

    def read(self):
        print(f'{self.name}read')

if __name__ == "__main__": #TODO работоспособность экземпляров класса проверить с помощью doctest
    dog = Animals("sobaka","white",5200)
    dog_weight = dog.get_weight_kg()
    print(dog_weight)

    book_1 = Book("IDIOT","Dostoevskiy","Russia")
    book_1_author = book_1.get_author()
    print(book_1_author)

    passport_1 = Passport("Russian","Sasha","10.01.2001")
    passport_1.show_status()