# Используя класс Сотрудник в качестве базового создайте класс
# Преподаватель (Teacher), имеющий: атрибут дисциплины (disciplines), в
# котором хранятся названия дисциплин, которые ведет преподаватель; методы
# __init__ и __str__;методы добавить_дисциплину (add_dis) и
# удалить_дисциплину (delete_dis), которые позволяют изменять список
# дисциплин. Продемонстрируйте работу с классами, создав необходимые
# объекты и вызвав все их методы. 

class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name
    
    def get_age(self) -> int:
        return self.age
    
class Worker(People):
    def __init__(self, people: 'People', post: str, salary: float) -> None:
        super().__init__(people.name, people.age)
        self.post = post
        self.salary = salary

    def __str__(self) -> str:
        return f'Name: {self.get_name()}\nAge: {self.get_age()}\nPost: {self.get_post()}\nSalary: {self.get_salary()}$'
    
    def get_post(self) -> str:
        return self.post
    
    def get_salary(self) -> float:
        return self.salary
    
class Teacher(Worker):
    disciplines: list[str] = []

    def __init__(self, worker: 'Worker') -> None:
        super().__init__(worker, worker.post, worker.salary)

    def __str__(self) -> str:
        return super().__str__()

    def add_discipline(self, discipline: str) -> None:
        if discipline not in self.disciplines:
             self.disciplines.append(discipline)
        
    def delete_discipline(self, discipline: str) -> None:
        if discipline in self.disciplines:
            self.disciplines.remove(discipline)   

    def get_disciplines(self) -> list[str]:
        return self.disciplines
    
if __name__ == '__main__':
    teacher = Teacher(Worker(People('Rimma Ivanovna', 40), 'Teacher', 99999999999))
    teacher.disciplines = ['AADS', 'ML']
    print(teacher)
    teacher.add_discipline('DP')
    print(teacher.get_disciplines())
    teacher.delete_discipline('ML')
    print(teacher.get_disciplines())