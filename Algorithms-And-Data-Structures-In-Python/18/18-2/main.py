# Создайте класс Point (точка), у которого имеются 2 атрибута x и y
# (координаты) и методы __init__() и __str__(), и класс Treyg (треугольник), у
# которого есть: • три атрибута (верхушки треугольника). Значениями атрибутов
# являются объекты класса Point; • методы __init__() и __str__(); • метод sides(),
# возвращающий длины сторон треугольника; • метод perim(), вычисляющий
# периметр треугольника. Продемонстрируйте работу с классами, создав
# необходимые объекты и вызвав все их методы.

import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Point: ({self.x},{self.y})'
    
class Triangle:
    def __init__(self, upper_point: 'Point', lower_left_point: 'Point', lower_right_point: 'Point') -> None:
        self.upper_point = upper_point
        self.lower_left_point = lower_left_point
        self.lower_right_point = lower_right_point

    def __str__(self) -> str:
        return f'Triangle: {self.sides()}'
    
    def sides(self) -> tuple[float, float, float]:
        return (distance(self.lower_left_point, self.upper_point),
                distance(self.upper_point, self.lower_right_point),
                distance(self.lower_right_point, self.lower_left_point))
    
    def perimeter(self) -> float:
        return sum(self.sides())

def distance(first_point: 'Point', second_point: 'Point') -> float:
    return round(math.sqrt(math.pow(second_point.x - first_point.x, 2) + math.pow(second_point.y - first_point.y, 2)), 3)
    
if __name__ == '__main__':
    first_point = Point(0, 0)
    print(first_point)
    second_point = Point(0, 5)
    print(second_point)
    third_point = Point(10, 0)
    print(third_point)
    triangle = Triangle(first_point, second_point, third_point)
    print(triangle)
    print(f'Perimeter: {triangle.perimeter()}')