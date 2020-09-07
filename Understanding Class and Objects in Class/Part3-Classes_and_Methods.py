'''
Python OOP 1 - Classes and Instances - https://youtu.be/ZDa-Z5JzLYM
Python OOP 2 - Class Variables - https://youtu.be/BJ-VvGyQxho
Python OOP 3 - Classmethods and Staticmethods - https://youtu.be/rq8cL2XMM5M
Python OOP 4 - Inheritance - https://youtu.be/RSl87lqOXDE
Python OOP 5 - Special (Magic/Dunder) Methods - https://youtu.be/3ohzBxoFHAY
Python OOP 6 - Property Decorators - https://youtu.be/jCzT9XFZ5bw

Important in the list:
Closures:
https://www.youtube.com/watch?v=swU3c34d2NQ

First Class Functions:
https://www.youtube.com/watch?v=kr0mpwqttM0

Decorators:
https://www.youtube.com/watch?v=FsAPt_9Bf3U

Corey Schafer
'''

import datetime


def understanding_classes():
    """
    data and functions in a class are called attributes and methods
    for example if you have a lot of employees
    create a class and assign similar attributes to all the employees: like name, salary, department

    class is a blueprint for creating instances
    each employee will be an instance of the class

    class Employee:
    # emp_1.fname = 'Corey'
    # emp_1.lname = 'Schafer'
    # emp_1.email = 'corey.schafer@company.com'
    # emp_1.pay = 50000

    # emp_2.fname = 'Test'
    # emp_2.lname = 'User'
    # emp_2.email = 'test.user@company.com'
    # emp_2.pay = 60000

        num_of_emps = 0 # shall increase everytime there is an employee instantiation
        raise_amount = 1.04


    # similar = emp_1.fname = 'Corey'
    # emp_1 is passed as self and thus self.first = emp_1.first
    # since self is equivalent to emp_1/emp_2, if self is excluded in methods, it will give an error
        def __init__(self, fname, lname, pay):
            self.first = fname
            self.last = lname
            self.pay = pay
            self.email = fname + '.' + lname + '@company.com'

            Employee.num_of_emps += 1

        def full_name(self):
            return f'{self.first} {self.last}'

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)  # better to use self

        # this changes the regular method as a class method and therefore
        # instead of self you have cls as the first entry

        # Regular methods pass self as the first variable
        # class method pass cls as the first variable
        # static method dont pass anything automatically and are like regular functions

        @classmethod
        def set_raise_amt(cls, amount):
            cls.raise_amount = amount

        @classmethod  # as alternative constructors
        def from_string(cls, emp_str):
            fname, lname, pay = emp_str.split("-")
            return cls(fname, lname, pay)

        @staticmethod
        def is_workday(day):
            if day.weekday == 5 or day.weekday == 6:  # checking if it is sat or sunday
                return False  # not working
            return True



        print("The number of employees before employee instances", Employee.num_of_emps)  # shall give 0

        emp_1 = Employee('Corey', 'Schafer', 50000) # Developer subclass
        emp_2 = Employee('Test', 'User', 60000)

        print("The number of employees after employee instances", Employee.num_of_emps)  # two instances of employees
        print(emp_1.email)
        print(emp_2.email)
        print("Without passing self", emp_1.full_name())  # self does not need to be passed as it is passed automatically
        print("with Employee class", Employee.full_name(emp_1))  # Employee does not know for which emp,
        # you want the output, so you have to pass it as an argument


        # if let us say there is a raise every year for all the employees for a certain percent
        # you might want to use a class variable

        print("Employee pay without raise", emp_1.pay)  # 50000
        emp_1.apply_raise()
        print("Employee pay with raise", emp_1.pay)  # 52000

        # change the raise amount only for emp_1
        print("Raise amount before changing the amount", emp_1.raise_amount)  # before changing the raise amount
        emp_1.raise_amount = 1.05
        emp_1.apply_raise()
        print("Pay after applying a raise of 1.05 for emp_1", emp_1.pay)  # 54600

        # printing the raise amount
        # the attribute is first checked in the instance and then in the class
        print("Raise amount for Employee class", Employee.raise_amount)
        # after changing the raise amount to 1.05 for emp_1
        print("Changing raise amount for emp_1", emp_1.raise_amount)

        print("Not altering raise amount for emp_2", emp_2.raise_amount)

        # changing this using the class method to 1.06
        Employee.set_raise_amt(1.06)
        print("Class raise set to 1.06", Employee.raise_amount)
        print("emp_1 changed as before to 1.05", emp_1.raise_amount)
        print("Class raise set to 1.06", emp_2.raise_amount)

        emp_str_1 = 'John-Doe-70000'
        emp_str_2 = 'Steve-Smith-30000'
        emp_str_3 = 'Jane-Doe-90000'

        # class method
        new_employee_1 = Employee.from_string(emp_str_1)
        print(new_employee_1.email)

        # Static method printing
        my_date = datetime.date(2020, 8, 16)
        print("Weekday?", Employee.is_workday(my_date))
    """
    pass


help(understanding_classes)


class Employee:
    num_of_emps = 0  # shall increase everytime there is an employee instantiation
    raise_amount = 1.04

    # similar = emp_1.fname = 'Corey'
    # emp_1 is passed as self and thus self.first = emp_1.first
    # since self is equivalent to emp_1/emp_2, if self is excluded in methods, it will give an error

    def __init__(self, fname, lname, pay):
        self.first = fname
        self.last = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # better to use self

    # this changes the regular method as a class method and therefore
    # instead of self you have cls as the first entry

    # Regular methods pass self as the first variable
    # class method pass cls as the first variable
    # static method dont pass anything automatically and are like regular functions

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod  # as alternative constructors
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split("-")
        return cls(fname, lname, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:  # checking if it is sat or sunday
            return False  # not working
        return True

print("The number of employees before employee instances", Employee.num_of_emps)  # shall give 0

emp_1 = Employee('Corey', 'Schafer', 50000) # Developer subclass
emp_2 = Employee('Test', 'User', 60000)

print("The number of employees after employee instances", Employee.num_of_emps)  # two instances of employees
print(emp_1.email)
print(emp_2.email)
print("Without passing self", emp_1.full_name())  # self does not need to be passed as it is passed automatically
print("with Employee class", Employee.full_name(emp_1))  # Employee does not know for which emp,
# you want the output, so you have to pass it as an argument


# if let us say there is a raise every year for all the employees for a certain percent
# you might want to use a class variable

print("Employee pay without raise", emp_1.pay)  # 50000
emp_1.apply_raise()
print("Employee pay with raise of 1.04: ", emp_1.pay)  # 52000

# change the raise amount only for emp_1
print("Raise amount before changing the amount", emp_1.raise_amount)  # before changing the raise amount
emp_1.raise_amount = 1.05
emp_1.apply_raise()
print("Pay after applying a raise of 1.05 for emp_1", emp_1.pay)  # 54600

# printing the raise amount
# the attribute is first checked in the instance and then in the class
print("Raise amount for Employee class", Employee.raise_amount)
# after changing the raise amount to 1.05 for emp_1
print("Changing raise amount for emp_1", emp_1.raise_amount)

print("Not altering raise amount for emp_2", emp_2.raise_amount)

# changing this using the class method to 1.06
Employee.set_raise_amt(1.06)
print("Class raise set to 1.06 using @classmethod: ", Employee.raise_amount)
print("emp_1 changed as before to 1.05", emp_1.raise_amount)
print("Class raise set to 1.06", emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# class method
new_employee_1 = Employee.from_string(emp_str_1)
print(new_employee_1.email)

# Static method printing
my_date = datetime.date(2020, 8, 16)
print("Weekday?", Employee.is_workday(my_date))
