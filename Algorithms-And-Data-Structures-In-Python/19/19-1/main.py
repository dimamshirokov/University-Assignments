# Класс – трапеция. Методы – расчет площади и периметра трапеции. Поля – стороны трапеции, площадь и периметр.

import math

class Trapezoid:
    def __init__(self, sides: list[float]) -> None:
        if len(sides) != 4:
            raise Exception('Error: It must have four sides!')
        self.sides = sides
        self.square = self.calculate_square()
        self.perimeter = self.calculate_perimeter()

    def __str__(self) -> str:
        return f'\nTrapezoid: {self.get_sides()}\nSquare: {self.get_square()}\nPerimeter: {self.get_perimeter()}\n'
    
    def get_sides(self) -> list[float]:
        return self.sides

    def get_square(self) -> float:
        return self.square
    
    def get_perimeter(self) -> float:
        return self.perimeter
    
    def calculate_square(self) -> float:
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        d = self.sides[3]
        return round(((a + b) / 2) * math.sqrt((c ** 2) - ((((a - b) ** 2 + c ** 2 - d ** 2) / (2 * (a - b))) ** 2)), 3)
    
    def calculate_perimeter(self) -> float:
       return round(sum(self.sides), 3)
    

if __name__ == '__main__':
    try:
        trapezoid = Trapezoid([4, 16, 10, 10])
        print(trapezoid)
    except Exception as error:
        print(error)