# Необходимо разработать программную систему для управления транспортными средствами 
# транспортной компании, включающую учёт автомобилей и мотоциклов. 
# Система должна поддерживать сравнение транспортных средств по грузоподъёмности и топливному запасу, 
# а также предоставлять подробную информацию о каждом объекте. 
# Архитектура должна быть расширяемой для добавления новых типов транспорта (например, грузовиков) и 
# реализована с применением объектно-ориентированного подхода, наследования, 
# полиморфизма и магических методов Python.

class Vehicle:
    def __init__(self, model: str, vin: str, fuel_capacity: float, load_capacity: float) -> None:
        self.model = model
        self.vin = vin
        self.fuel_capacity = fuel_capacity
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        return f'{self.model} (VIN: {self.vin}), Fuel: {self.fuel_capacity} l, Load: {self.load_capacity} kg'
    
    def __eq__(self, other: 'Vehicle') -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented
        else:
            return self.load_capacity == other.load_capacity
        
    def __le__(self, other: 'Vehicle') -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented
        else:
            return self.load_capacity <= other.load_capacity

    def info(self) -> str:
        return f'Transport: {self.model} (VIN: {self.vin})'
    
class Car(Vehicle):
    def __init__(self, model: str, vin: str, fuel_capacity: float, load_capacity: float, seats: int) -> None:
        super().__init__(model, vin, fuel_capacity, load_capacity)
        self.seats = seats

    def __str__(self) -> str:
        return f'{self.model} (VIN: {self.vin}), Fuel: {self.fuel_capacity} l, Load: {self.load_capacity} kg, Seats: {self.seats}'

    def __add__(self, other: 'Car') -> 'Car':
        if not isinstance(other, Car):
            return TypeError
        else:
            return Car(
                self.model,
                self.vin,
                self.fuel_capacity + other.fuel_capacity,
                self.load_capacity + other.load_capacity,
                self.seats + other.seats
            )

    def info(self) -> str:
        return f'Car: {self.model}, Seats: {self.seats}'
    
class Motorcycle(Vehicle):
    def __init__(self, model: str, vin: str, fuel_capacity: float, load_capacity: float, has_sidecar: bool) -> None:
        super().__init__(model, vin, fuel_capacity, load_capacity)
        self.has_sidecar = has_sidecar

    def __str__(self) -> str:
        if self.has_sidecar:
            return f'{self.model} (VIN: {self.vin}), Fuel: {self.fuel_capacity} l, Load: {self.load_capacity} kg, with a sidecar'
        else:
            return f'{self.model} (VIN: {self.vin}), Fuel: {self.fuel_capacity} l, Load: {self.load_capacity} kg, without a sidecar'
        
    def __gt__(self, other: 'Motorcycle') -> bool:
        if not isinstance(other, Motorcycle):
            return NotImplemented
        else:
            return self.fuel_capacity > other.fuel_capacity

    def info(self) -> str:
        if self.has_sidecar:
            return f'Motorcycle: {self.model}, with a sidecar'
        else:
            return f'Motorcycle: {self.model}, without a sidecar'