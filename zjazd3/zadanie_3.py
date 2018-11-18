class Company:

   def __init__(self, name):
        self.name = name
        self.employees = set():

     def add_employee(self, employee):
         self.employees.add(employee)

    def size(self):
        return len(self.employees)

    def pay_all_salary(self):
        sum_=0
       for e in self.employees:
           sum_ += e.pay_salary()
       return sum_

def test_company():
    employe = Employe('Jan', 'Nowak', '100.0')
    employee.register_time(5)
    google = Company("google")
    google.add_employee(employee)
    assert google.size() == 1
    assert google



















    def register_time(self, hours):
        self.worked_hours = hours

