class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, new_pages):
        if isinstance(new_pages, int):
            self.pages = new_pages
        else:
            raise ValueError


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, new_duration):
        if isinstance(new_duration, float):
            self.duration = new_duration
        else:
            raise ValueError


    def __repr__(self):
        return f"{self.__class__.__name__}(name=--{self.name!r}, author={self.author!r}, duration={self.duration!r})"
