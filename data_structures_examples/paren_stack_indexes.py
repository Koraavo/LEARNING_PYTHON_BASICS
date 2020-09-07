from LEARNING_PYTHON_BASICS.Data_structures import Stacks


def start(inputString):
    s = Stacks.Stack()
    dict_paren = {}
    for i, c in enumerate(inputString):
        if c == '(':
            s.push(i)
        if c == ')':
            try:
                dict_paren[s.pop()] = i
            except IndexError:
                print('Too many closing parentheses')
    if not s.is_empty():
        print("Too many opening parenthesis")

    return dict_paren
inputString = "foo(bar(baz))blim"
print(start(inputString))
