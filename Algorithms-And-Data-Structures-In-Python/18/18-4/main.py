# Используя класс People в качестве базового, создайте класс Сотрудник
# (Worker), имеющий атрибуты: должность (post); зарплата (salary) и методы:
# __init__ – конструктор; __str__ – для вывода строковой информации. Создать
# два метода для класса Сотрудник и один метод для класса People.
# Продемонстрируйте работу с классами, создав необходимые объекты и вызвав
# все их методы. 

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
    
if __name__ == '__main__':
    people = People('Dima', 20)
    worker = Worker(people, 'Vice President of Development at Yandex', 1000000)
    print(worker)