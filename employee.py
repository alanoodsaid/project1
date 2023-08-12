class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.empname = emp_name
        self.empid = emp_id
        self.empsalary = emp_salary
        self.empdepartment = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.empsalary / 50)
            total_salary = self.empsalary + overtime_amount
        else:
            total_salary = self.empsalary
        return total_salary

    def emp_assign_department(self, new_department):
        self.empdepartment = new_department

    def employee_details(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.empname)
        print("Employee Salary:", self.empsalary)
        print("Employee Department:", self.empdepartment)

    # Getter and setter methods for emp_name
    def get_emp_name(self):
        return self.empname

    def set_emp_name(self, emp_name):
        self.empname = emp_name

    # Getter and setter methods for emp_id
    def get_emp_id(self):
        return self.empid

    def set_emp_id(self, emp_id):
        self.empid = emp_id

    # Getter and setter methods for emp_salary
    def get_emp_salary(self):
        return self.empsalary

    def set_emp_salary(self, emp_salary):
        self.empsalary = emp_salary

    # Getter and setter methods for emp_department
    def get_emp_department(self):
        return self.empdepartment

    def set_emp_department(self, emp_department):
        self.empdepartment = emp_department


# Sample Employee Data


# Using the methods of the Employee class
# efor emp in employees:
    