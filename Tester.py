class Employee:
    vacation_days = 20


class Tester(Employee):
    name ='John'
    title = 'Manager'

    def __init__(self, name=name, title=title) -> None:
        self.name = name
        self.title = title

    def get_employee_details(self):
        return f"Employee name: {self.name} and the title{self.title}"

Mike = Tester('Mike', 'CEO')
Jennifer = Tester()