"""
First Class Functions are functions that act just like other objects,
you can use them as an argument in a different function
you can return the function
assign function to variables

Closures allow us to take advantage of first class functions and return an inner function
that remembers and has access to variables, local to the scope in which they were created

"""

# functions are being passed as arguments
def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i)) # func(i) = cube(x)
    return result

squares = my_map(cube, [1, 2, 3, 4, 5])

print(squares)

# Treat a variable as a function
def logger(msg):

    def log_message():
        print("Log", msg)
    return log_message # NO PARENTHESIS

log_hi = logger('Hi')
log_hi()

# Another example:
def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')

print(print_h1.__name__) # basically print_h1 = wrap_text and wrap_text requires one argument