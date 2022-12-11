from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        ...  # TODO инициализировать объект "Стакан"

class passport:
    def __init__(self,nationality, name,date):
        # Атрибутам присваиваются значения аргументов конструктора объекта
        self.nationality = nationality
        self.name = name
        self.date = date

    def read(self):
        print(f'{self.name} read')
if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass

    # TODO попробовать инициализировать не корректные объекты
