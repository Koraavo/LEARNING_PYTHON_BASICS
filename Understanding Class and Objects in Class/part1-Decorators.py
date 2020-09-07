def decorator_function(original_message):
    def wrapper_function():
        # original_message = display
        print(f'wrapper executed this before {original_message.__name__}')
        return original_message()

    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)
decorated_display()

# decorated display is basically wrapper_function
print(decorated_display.__name__)
print()

#
def decorator_function(original_message):
    def wrapper_function(*args, **kwargs):
        # original_message = display
        print(f'wrapper executed this before {original_message.__name__}')
        return original_message(*args, **kwargs)

    return wrapper_function

class decorator_class(object):

    def __init__(self, original_message):
        self.original_message = original_message

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_message.__name__}')
        return self.original_message(*args, **kwargs)


@decorator_function # display = decorator_function(display)
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('display info ran with arguments {0} and {1}'.format(name, age))

display_info('John', 25)
print()
display()
# decorated display is basically wrapper_function
#print(display.__name__)
print()

@decorator_class # display = decorator_function(display) # class decorator
def display():
    print('display function ran')

@decorator_class
def display_info(name, age):
    print('display info ran with arguments {0} and {1}'.format(name, age))

display_info('John', 25)
print()
display()
# decorated display is basically wrapper_function
#print(display.__name__)