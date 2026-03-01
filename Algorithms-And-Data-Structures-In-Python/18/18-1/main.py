# Создайте класс Point (точка), у которого имеются 2 атрибута x и y
# (координаты) и методы __init__() и __str__(), и класс Rect (прямоугольник), у
# которого есть: • два атрибута (верхний левый угол и правый нижний угол
# прямоугольника). Значениями атрибутов являются объекты класса Point; •
# методы __init__() и __str__(); метод sides(), возвращающий длины сторон
# прямоугольника; метод perim(), вычисляющий периметр прямоугольника.
# Продемонстрируйте работу с классами, создав необходимые объекты и вызвав
# все их методы

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Point: ({self.x},{self.y})'
    
class Rectangle:
    def __init__(self, upper_left_point: 'Point', lower_right_point: 'Point') -> None:
        self.upper_left_point = upper_left_point
        self.lower_right_point = lower_right_point

    def __str__(self) -> str:
        return f'Rectangle: {self.sides()}'

    def sides(self) -> tuple[float, float, float, float]:
        width = abs(self.lower_right_point.x - self.upper_left_point.x)
        height = abs(self.upper_left_point.y - self.lower_right_point.y)
        return (height, width, height, width)

    def perimeter(self) -> float:
        return sum(self.sides())
    
if __name__ == '__main__':
    first_point = Point(10, 0)
    print(first_point)
    second_point = Point(0, 5)
    print(second_point)
    rectangle = Rectangle(first_point, second_point)
    print(rectangle)
    print(f'Perimeter: {rectangle.perimeter()}')