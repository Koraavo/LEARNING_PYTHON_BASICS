# sorting from ascending to descending and vice versa
# the command works only if it is an array

def understanding_sorting():
    """
    # Sequence = Numbers (double digits, single digits),
    Floats, Capital Letters and then small letters

    list1 = (["A", "X", "R", "9.23", "10", "18", "I", "05", "7", "a", "p"])
    # Temporary sorting: original list1 remains the same
    # sorted is a function
    print(sorted(list1))
    print(sorted(list1, reverse=True))  # This is descending

    # permanent sorting
    # sort is a method
    sort does not work on Tuples, since Tuples are immutable
    list1.sort()

    # Sorting Dictionaries
    This will sort as per the keys and not their values
    di = {'name': 'Kinjal', 'age': None, 'os': 'Mac', 'job': 'Student'}
    s_di = sorted(di)

    L = ["cccc", "b", "dd", "aaa"]
    print("Normal sort :", sorted(L)) # prints ["aaa", "b", "cccc", "d"]
    print("Sort with len :", sorted(L, key=len))  # Key Len sorts as per length

    # Sorting a Class
    from operator import attrgetter
    class Employee():
        def __init__(self, name, age, pay):
            self.name = name
            self. age = age
            self.pay = pay

        def __repr__(self):
            return f'{self.name}, {self.age}, ${self.pay}'

    e1 = Employee('John', 25, 50000)
    e2 = Employee('Kinjal', 32, 60000)
    e3 = Employee('Violette', 30, 70000)

    employees = [e1,e2,e3]
    #s_employees = sorted(employees) # this will result in a unorderable error
                                    #because python does not know how to sort it

    #print(s_employees)

    def e_sort(emp):
        return emp.name
    s_employees = sorted(employees, key=e_sort) # created a user_defined function and put as key
    print(s_employees)
    s_employees = sorted(employees, key=attrgetter('name'))
    print(s_employees)

    """
    pass

help(understanding_sorting)

