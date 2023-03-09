class Car:
    def __init__(self,model: str,color: str,weight: float,number: str,year: int,passangers: int):
        self.model=model
        self.color=color
        self.weight=weight
        self.number=number
        self.year=year
        self.passangers=passangers
    def __str__(self):
        return f"Автомобиль {self.model}, color {self.color}, number {self.number}, year {self.year}"

    def __repr__(self):
        return f"Автомобиль {self.number}"

    def get_age(self):
        return 2023-self.year #возвращает возраст автомобиля

    def print_passangers_number(self): #метод печатает максимальное колличество пассажиров
        print(f'Максимальное количество пассажиров: {self.passangers}')

class Formula_1car(Car):
    def __init__(self,model:str,color: str,weight: float,number: str,year: int,passangers: int,competition: str,pilot: str):
        super().__init__(model,color,weight,number,year,passangers)
        self.competition=competition
        self.pilot=pilot

    def __str__(self):
        return f"Автомобиль {self.model}, color {self.color}, number {self.number}, competition {self.competition}, pilot {self.pilot},year {self.year}"

    def print_passangers_number(self):
        if self.passangers > 2:
            print('Осторожно, опасно! Для спортивных машин на Формуле 1 должно быть не больше 2 пассажиров')
        print(f'Максимальное количество пассажиров: {self.passangers}')