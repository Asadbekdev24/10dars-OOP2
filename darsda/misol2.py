import os
os.system("cls")


class Employee:
    def __init__(self, surname:str, position:str, salary:int) -> None:
        self.surname=surname
        self.position=position
        self.salary=salary

class Enterprice_Employee(Employee):
    def __init__(self, surname: str, position: str, salary: int, reytinggi:int) -> None:
        super().__init__(surname, position, salary)
        self.reyting=reytinggi

ishchi1=Enterprice_Employee("Ali", "qorovul", 300, 80)
ishchi2=Enterprice_Employee("Vali", "farrosh", 500, 45)
ishchi3=Enterprice_Employee("Jaha", "meneger", 400, 65)
ishchi4=Enterprice_Employee("Asadbek", "Direktor",600, 90)
ishchi5=Enterprice_Employee("Valijon", "Direktor ukasi",410, 90)

ishchilar=[ishchi1,ishchi2,ishchi3,ishchi4,ishchi5]

for el in ishchilar:
    if el.reyting>70:
        print(f"{el.surname}  Urraa oyligiz oshdi")
