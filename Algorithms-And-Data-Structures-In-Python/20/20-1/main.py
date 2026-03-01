# Опишите класс Salary. Для класса задаются атрибуты: фамилия, имя и отчество, год поступления на работу, 
# оклад в рублях, процент надбавки, количество отработанных дней в месяце, 
# количество рабочих дней в месяце, начисленная и удержанная суммы. 
# Включите в описание класса методы: вычисления начисленной суммы, вычисления удержанной суммы, 
# вычисления суммы, выдаваемой на руки, а также свойство только для чтения, 
# позволяющее определить стаж работы (вычисляется как полное количество лет, 
# прошедших с момента зачисления на работу до задаваемого текущего года). Начисленная сумма вычисляется
# за отработанные дни месяца плюс надбавка. Удержания — подоходный налог 13%.

from datetime import datetime

class Salary:
    def __init__(self, surname: str, name: str, patronymic: str, admission_year: int,
                 salary_before_bonuses: float, bonus_percentage: float,
                 worked_days: int, total_worked_days: int) -> None:
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.admission_year = admission_year
        self.salary_before_bonuses = salary_before_bonuses
        self.bonus_percentage = bonus_percentage
        self.worked_days = worked_days
        self.total_worked_days = total_worked_days
        self.accrued_amount = self.calculate_accrued_amount()
        self.withheld_amount = self.calculate_withheld_amount()
        self.salary = self.calculate_salary()
        self.work_experience = self.calculate_work_experience()

    def __str__(self) -> str:
        return f'''
Surname: {self.surname}
Name: {self.name}
Patronymic: {self.patronymic}
Admission Year: {self.admission_year}
Salary Before Bonuses: {self.salary_before_bonuses}
Bonus Percentage: {self.bonus_percentage}
Worked Days: {self.worked_days}
Total Worked Days: {self.total_worked_days}
Accrued Amount: {self.accrued_amount}
Withheld Amount: {self.withheld_amount}
Salary: {self.salary}
Work Experience: {self.work_experience}
'''

    def calculate_accrued_amount(self) -> float:
        return round((self.salary_before_bonuses / self.total_worked_days) * (self.worked_days) + \
            self.salary_before_bonuses * (self.bonus_percentage / 100), 3)
    
    def calculate_withheld_amount(self) -> float:
        return round(self.accrued_amount * 0.13, 3)
    
    def calculate_salary(self) -> float:
        return round(self.accrued_amount - self.withheld_amount, 3)
    
    def calculate_work_experience(self) -> int:
        return datetime.now().year - self.admission_year
    
if __name__ == '__main__':
    salary = Salary('Shirokov', 'Dmitrii', 'Maksimovich', 2023, 120000, 10, 17, 20)
    print(salary)