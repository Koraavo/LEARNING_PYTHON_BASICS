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

        # similar = emp_1.fname = 'Corey'
        # emp_1 is passed as self and thus self.first = emp_1.first
        # since self is equivalent to emp_1/emp_2, if self is excluded in methods, it will give an error

        def __init__(self, fname, lname, pay):
            self.first = fname
            self.last = lname
            self.pay = pay
            self.email = fname + '.' + lname + '@company.com'

        def full_name(self):
            return f'{self.first} {self.last}'


    emp_1 = Employee('Corey', 'Schafer', 50000)
    emp_2 = Employee('Test', 'User', 60000)

    print(emp_1.email)
    print(emp_2.email)


    print(emp_1.full_name())   # self does not need to be passed as it is passed automatically
    print(Employee.full_name(emp_1))   # Employee does not know for which emp,
                                        # you want the output, so you have to pass it as an argument
    """
    pass

help(understanding_classes)

class Employee:

    # similar = emp_1.fname = 'Corey'
    # emp_1 is passed as self and thus self.first = emp_1.first
    # since self is equivalent to emp_1/emp_2, if self is excluded in methods, it will give an error

    def __init__(self, fname, lname, pay):
        self.first = fname
        self.last = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def full_name(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# emp_1.fname = 'Corey'
# emp_1.lname = 'Schafer'
# emp_1.email = 'corey.schafer@company.com'
# emp_1.pay = 50000

# emp_2.fname = 'Test'
# emp_2.lname = 'User'
# emp_2.email = 'test.user@company.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)


print(emp_1.full_name())   # self does not need to be passed as it is passed automatically
print(Employee.full_name(emp_1))   # Employee does not know for which emp,
                            # you want the output, so you have to pass it as an argument

