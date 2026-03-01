# Построить базовый класс с указанными в таблице полями и методами:
# конструктор; функция, которая определяет «качество» объекта – Q по
# заданной формуле; метод вывода информации об объекте. Построить
# дочерний класс (класс-потомок), который содержит: дополнительное поле P;
# функцию, которая определяет «качество» объекта дочернего класса – Qp и
# перегружает функцию качества родительского класса (Q), выполняя
# вычисление по новой формуле. Создать проект для демонстрации работы:
# ввод и вывод информации об объектах классов.

from datetime import datetime 

class Car:
    def __init__(self, brand: str, engine_power: int, number_of_seats: int) -> None:
        self.brand = brand
        self.engine_power = engine_power
        self.number_of_seats = number_of_seats

    def __str__(self) -> str:
        return f'\nBrand: {self.brand}\nEngine power: {self.engine_power}\nNumber of seats: {self.number_of_seats}\n'

    def quality(self) -> float:
        return round(0.1 * (self.engine_power * self.number_of_seats), 3)
    
class CarModel(Car):
    def __init__(self, car: 'Car', year_of_release: int) -> None:
        super().__init__(car.brand, car.engine_power, car.number_of_seats)
        self.year_of_release = year_of_release

    def __str__(self) -> str:
        return super().__str__() + f'Year of release: {self.year_of_release}\n'

    def quality(self) -> float:
        return round(super().quality() - 1.5 * (datetime.now().year - self.year_of_release), 3)
    
if __name__ == '__main__':
    car = Car('Porshe', 523, 2)
    print(car)
    print(f'Quality: {car.quality()}')
    car_model = CarModel(car, 1992)
    print(car_model)
    print(f'Quality: {car_model.quality()}')