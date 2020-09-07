

def hello_func():
    """
    understanding def functions

    without an argument:
    Example:
        def hello_func():
            return 'Hello Function'

        print(hellofunc())
        print(hellofunc().upper())

    With arguments:
    Example:

        def hello_func(greeting):
            return f'{greeting} Function'

        print(hello_func('hi')) # This will print hi Function
    Example2:

        def f(x):
            print(x ** 3 - 20)
        f(-3)

    Understanding *args and **kwargs

    args are arguments and kwargs are keyword arguments

    Let's give an example for this:

    def student_info(*args, **kwargs):
        print(args)
        print(kwargs)

    student_info('Math', 'Science', name='John', age=25)
    Here Math and John are not bound by a keyword like subjects for example
    but John is bound by name and 25 is bound by age.
    so when args are printed:
    it shall print a tuple of arguments:
    ('Math', 'Science')
    kwargs would be a dictionary:
    {'name': 'John', 'age': 25}

    Now if we change this to:
    student_info(subjects = ['Math', 'Science'], name='John', age=25)

    There are no args only kwargs
    so when printing args - the output will be ()
    and with kwargs:
    {'subjects': ['Math', 'Science'], 'name': 'John', 'age': 25}

    Now if we do this:
    def student_info(*args, **kwargs):
        print(args)
        print(kwargs)

    courses = ['Math', 'Science']
    info = {name = 'John', age = 25}

    student_info(courses, info) # will print it as a combined list of args and kwards
    student_info(*courses, **info) # will return args and then kwargs

    Example2 of args and kwargs
        def our_people(*people):
            for items in people:
                print("This is the name of an item in people", items)

        our_people("Ashley", "John", "Rajesh", "Bina", "Rounak", "Violette")

    Understanding Global and Local variables
        x = 1

        def my_function():
            x = 2
            print("This is the first:", x)

        print("This is the global variable:", x)  # so it will print this first
        my_function()  # will print whatever is in the local variable
        print(x)  # this is again global value of x that is 1

    """
    print("https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/")
    pass

help(hello_func)
