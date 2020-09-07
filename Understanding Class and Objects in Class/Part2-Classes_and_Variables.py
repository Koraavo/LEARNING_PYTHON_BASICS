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
                self.pay = int(self.pay * self.raise_amount) # better to use self

    print(Employee.num_of_emps) # shall give 0

    emp_1 = Employee('Corey', 'Schafer', 50000)
    emp_2 = Employee('Test', 'User', 60000)

    print(Employee.num_of_emps) # two instances of employees

    print(emp_1.email)
    print(emp_2.email)
    print(emp_1.full_name())            # self does not need to be passed as it is passed automatically
    print(Employee.full_name(emp_1))    # Employee does not know for which emp,
                                        # you want the output, so you have to pass it as an argument

    # if let us say there is a raise every year for all the employees for a certain percent
    # you might want to use a class variable

    print(emp_1.pay) # 50000
    emp_1.apply_raise()
    print(emp_1.pay) # 52000

    # change the raise amount only for empl_1
    print(emp_1.raise_amount) # before changing the raise amount
    emp_1.raise_amount = 1.05
    emp_1.apply_raise()
    print(emp_1.pay)    # 54600

    # printing the raise amount
    # the attribute is first checked in the instance and then in the class
    print(Employee.raise_amount)
    # after changing the raise amount
    print(emp_1.raise_amount)

    print(emp_2.raise_amount)
    """
    pass


help(understanding_classes)


class Employee:
    num_of_emps = 0  # shall increase every time there is an employee instantiation
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


print("The number of employees before initiating the employees are", Employee.num_of_emps)  # shall give 0

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print("The number of employees after initiating the employees are", Employee.num_of_emps)  # two instances of employees

print("Employee1_email is", emp_1.email)
print("Employee1_email is", emp_2.email)
print(emp_1.full_name())  # self does not need to be passed as it is passed automatically
print(Employee.full_name(emp_1))  # Employee does not know for which emp,
# you want the output, so you have to pass it as an argument

# if let us say there is a raise every year for all the employees for a certain percent
# you might want to use a class variable

print("Employee1 pay: ", emp_1.pay)  # 50000
emp_1.apply_raise()
print("Employee1 pay after apply raise of 1.04 is: ", emp_1.pay)  # 52000

# change the raise amount only for empl_1
print("Employee 1 raise amount is: ", emp_1.raise_amount)  # before changing the raise amount
emp_1.raise_amount = 1.05
emp_1.apply_raise()
print("Raise amount increased for emp1 to 1.05, pay is ", emp_1.pay)  # 54600

# printing the raise amount
# the attribute is first checked in the instance and then in the class
print("Employee class raise amount is: ", Employee.raise_amount)
# after changing the raise amount
print("Employee1 raise amount is: ", emp_1.raise_amount)

print("Emp2 raise amount is: ", emp_2.raise_amount)
