
class Employee:
    name = []
    emp_number = []

    def add_employee(self, name, emp_number):
        self.name.append(input("What is the name of the employee?\n"))
        self.emp_number.append(input("What is the employee number of employee?\n"))
