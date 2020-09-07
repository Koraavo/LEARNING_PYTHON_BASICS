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

    """
    pass


help(understanding_classes)


class Employee:
    raise_amount = 1.04

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

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # better to use self

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)
print(repr(emp_1))     # meant to be seen by other developers
print(str(emp_1))     # display to the end user

print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1 + emp_2)
print(len(emp_1))