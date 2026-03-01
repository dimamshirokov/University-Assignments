#  Создать базовый класс по следующей предметной области. Известны оклад
# (зарплата) и ставка процента подоходного налога. Определить размер
# подоходного налога и сумму, получаемую на руки. Исходными данными
# являются величина оклада (переменная oklad, выражаемая числом) и ставка
# подоходного налога (переменная procent, выражаемая числом). Размер налога
# (переменная nalog) определяется как oklad∗procent/100, а сумма, получаемая
# на руки (переменная summa) — как oklad-nalog

class Salary:
    def __init__(self, salary_before_taxes: float, tax_percentage: float) -> None:
        self.tax= salary_before_taxes * (tax_percentage / 100)
        self.salary= salary_before_taxes - self.tax

    def __str__(self) -> str:
        return f'\nSalary: {self.get_salary()}$\nTax: {self.get_tax()}$\n'

    def get_tax(self) -> float:
        return self.tax
    
    def get_salary(self) -> float:
        return self.salary
    
if __name__ == '__main__':
    salary = Salary(10000, 13)
    print(salary)