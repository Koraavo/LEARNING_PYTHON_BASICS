'''
Python OOP 1 - Classes and Instances - https://youtu.be/ZDa-Z5JzLYM
from Corey Schafer
'''

def understanding_classes():
    """
    data and functions in a class are called attributes and methods
    for example if you have a lot of employees
    create a class and assign similar attributes to all the employees: like name, salary, department

    class is a blueprint for creating instances
    each employee will be an instance of the class
    """
    pass

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_1)

# Let's say we want employee one and two to have a first and a last name
emp_1.fname = 'Corey'
emp_1.lname = 'Schafer'
emp_1.email = 'corey.schafer@company.com'
emp_1.pay = 50000

emp_2.fname = 'Test'
emp_2.lname = 'User'
emp_2.email = 'test.user@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
