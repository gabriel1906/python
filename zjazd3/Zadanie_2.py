class Employee:
    employee = Employee(Jan, Nowak, 100.0)


    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.worked_hours = 0


    def register_time(self, hours):
        self.worked_hours = hours


    def pay_salary(self):
        if worked_hours <= 8:
            self.to_pay = self.worked_hours * self.stawka
        else:
            self.to_pay = (self.worked_hours + (self.worked_hours - 8)  self.stawka * 2)
        return to_pay


 class PremiumEmployee(Employee):

     def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka):
        self.bonus = bonus


     def giv_bonus(self, amount):









#
#
# def test_employee():
#     employee == Employee('Jan', 'Nowak', 100.0)
#     assert employee.imie == 'Jan'
#     assert employee.nazwisko == 'Nowak'
#     assert employee.stawka == '500'
#
#
#     assert employee.register_time(5)
#     assert employee.pay_salary == 500
#     assert employee.pay_salary == 0.0
#     assert employee.pay_salary == 1200.0

