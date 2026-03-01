# Создайте класс Ведомость, имеющий атрибут класса: список_дисциплин
# (значением является список с названиями дисциплин); дисциплина (при
# задании значения проверять наличие дисциплины в атрибуте
# список_дисциплин), группа; методы: put – добавляет в ведомость информацию
# об оценке студента (фамилия, оценка – параметры метода). Для хранения
# данных внутри класса используйте словарь, в котором ключом является
# фамилия студента. Возможные оценки – «отлично», «хорошо», «удовл.»,
# «неудовл.», «н/я»; get – возвращает оценку, полученную студентом (фамилия
# студента – параметр метода); change – изменяет оценку, полученную
# студентом (фамилия студента и новая оценка – параметры метода); del –
# удаляет информацию о студенте из ведомости (фамилия студента – параметр
# метода); result – возвращает кортеж из 5 чисел (количество каждого вида
# оценок в ведомости); __init__ – конструктор; __str__ – возвращает строку,
# содержащую заголовки (название экзамена, группа) и результаты экзамена в
# виде таблицы; count – возвращает количество студентов в ведомости; names –
# возвращает список фамилий, имеющихся в ведомости. Продемонстрируйте
# работу с классами, создав необходимые объекты и вызвав все их методы. 

class Gradebook:
    disciplines_list: list[str] = []

    def __init__(self, discipline: str, group: str) -> None:
        if discipline not in Gradebook.disciplines_list:
            raise ValueError(f"Дисциплина '{discipline}' отсутствует в списке дисциплин")
        self.discipline = discipline
        self.group = group
        self._grades: dict[str, str] = {}

    def put(self, surname: str, grade: str) -> None:
        if grade not in ('отлично', 'хорошо', 'удовл.', 'неудовл.', 'н/я'):
            raise ValueError(f"Недопустимая оценка: {grade}")
        if surname in self._grades:
            raise ValueError(f"Студент {surname} уже существует в ведомости")
        self._grades[surname] = grade

    def get(self, surname: str) -> str:
        if surname not in self._grades:
            raise KeyError(f"Студент {surname} не найден")
        return self._grades[surname]

    def change(self, surname: str, new_grade: str) -> None:
        if new_grade not in ('отлично', 'хорошо', 'удовл.', 'неудовл.', 'н/я'):
            raise ValueError(f"Недопустимая оценка: {new_grade}")
        if surname not in self._grades:
            raise KeyError(f"Студент {surname} не найден")
        self._grades[surname] = new_grade

    def delete(self, surname: str) -> None:
        if surname not in self._grades:
            raise KeyError(f"Студент {surname} не найден")
        del self._grades[surname]

    def result(self) -> tuple[int, int, int, int, int]:
        excellent = sum(1 for grade in self._grades.values() if grade == 'отлично')
        good = sum(1 for grade in self._grades.values() if grade == 'хорошо')
        satisfactory = sum(1 for grade in self._grades.values() if grade == 'удовл.')
        unsatisfactory = sum(1 for grade in self._grades.values() if grade == 'неудовл.')
        not_shown = sum(1 for grade in self._grades.values() if grade == 'н/я')
        return (excellent, good, satisfactory, unsatisfactory, not_shown)

    def count(self) -> int:
        return len(self._grades)

    def names(self) -> list[str]:
        return list(self._grades.keys())

    def __str__(self) -> str:
        header = f"Дисциплина: {self.discipline}  Группа: {self.group}\n"
        separator = "-" * 50 + "\n"
        table_header = f"{'Фамилия':<20} {'Оценка':<15}\n"
        rows = []
        for surname, grade in self._grades.items():
            rows.append(f"{surname:<20} {grade:<15}")
        return header + separator + table_header + separator + "\n".join(rows)

if __name__ == '__main__':
    Gradebook.disciplines_list = ['Математика', 'Физика', 'Информатика']
    math_grades = Gradebook('Математика', 'ПМ25-1')
    print("Создана ведомость:")
    print(math_grades)
    print()

    math_grades.put('Широков', 'отлично')
    math_grades.put('Селиванов', 'хорошо')
    math_grades.put('Павлюченко', 'удовл.')
    math_grades.put('Бибиков', 'неудовл.')
    math_grades.put('Веретенников', 'н/я')
    print("После добавления студентов:")
    print(math_grades)
    print()

    print("Оценка Широкова:", math_grades.get('Широков'))
    print()

    math_grades.change('Селиванов', 'отлично')
    print("После изменения оценки Селиванова на 'отлично':")
    print(math_grades)
    print()

    math_grades.delete('Павлюченко')
    print("После удаления Павлюченко:")
    print(math_grades)
    print()

    results = math_grades.result()
    print(f"Результаты: отлично={results[0]}, хорошо={results[1]}, удовл.={results[2]}, неудовл.={results[3]}, н/я={results[4]}")
    print()

    print("Количество студентов:", math_grades.count())
    print("Фамилии студентов:", math_grades.names())
    print()

    print("Попытка добавить студента с недопустимой оценкой:")
    try:
        math_grades.put('Новый', 'превосходно')
    except ValueError as error:
        print("Ошибка:", error)
    print()

    print("Попытка добавить уже существующего студента:")
    try:
        math_grades.put('Бибиков', 'хорошо')
    except ValueError as error:
        print("Ошибка:", error)
    print()

    print("Попытка создать ведомость по несуществующей дисциплине:")
    try:
        invalid = Gradebook('Биология', 'ПМ25-1')
    except ValueError as error:
        print("Ошибка:", error)