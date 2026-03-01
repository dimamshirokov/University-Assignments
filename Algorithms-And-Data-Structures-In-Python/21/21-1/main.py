# Создайте класс ПРОГРЕССИЯ с методами вычисления i-го элемента прогрессии, 
# её суммы и методом, выводящим сумму на экран. 
# Создайте дочерние классы: АРИФМЕТИЧЕСКАЯ, ГЕОМЕТРИЧЕСКАЯ со своими методами вычисления. 
# Создайте список n прогрессий и выведите сумму каждой из них экран.

class Sequence:
    def __init__(self, sequence: list[float]) -> None:
        self.sequence = sequence

    def __str__(self) -> str:
        return f'Sum: {self.calculate_sequence_sum()}'

    def calculate_sequence_sum(self) -> float:
        return sum(self.sequence)
    
    def calculate_element(self, index: int) -> float:
        return self.sequence[index]

class ArithmeticSequence(Sequence):
    def __init__(self, sequence: 'Sequence') -> None:
        super().__init__(sequence.sequence)

    def calculate_sequence_sum(self) -> float:
        if len(self.sequence) == 0:
            return 0
        elif len(self.sequence) == 1:
            return self.sequence[0]
        return ((self.sequence[0] + self.sequence[-1]) * (len(self.sequence))) / 2
    
    def calculate_element(self, index: int) -> float:
        return self.sequence[0] + (index - 1) * (self.sequence[1] - self.sequence[0])
    
class GeometricSequence(Sequence):
    def __init__(self, sequence: 'Sequence') -> None:
        super().__init__(sequence.sequence)

    def calculate_sequence_sum(self) -> float:
        if len(self.sequence) == 0:
            return 0
        elif len(self.sequence) == 1:
            return self.sequence[0]
        step = (self.sequence[1] / self.sequence[0])
        return ((self.sequence[0]) * (step ** len(self.sequence) - 1)) / (step - 1)

    def calculate_element(self, index: int) -> float:
        step = (self.sequence[1] / self.sequence[0])
        return self.sequence[0] * (step ** (index - 1))
    
if __name__ == '__main__':
    sequences = [ArithmeticSequence(Sequence([1, 5, 9, 13])),
                GeometricSequence(Sequence([1, 3, 9, 27])),
                ArithmeticSequence(Sequence([-10, -8, -6, -4, -2, 0]))]
    for sequence in sequences:
        print(sequence)
    print('5th element: ' + str(ArithmeticSequence(Sequence([-5, -3, -1, 1, 3, 5, 7, 9, 11])).calculate_element(5)))
    print('3d element: ' + str(GeometricSequence(Sequence([7, 49, 343])).calculate_element(3)))