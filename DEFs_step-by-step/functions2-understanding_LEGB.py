'''
LEGB
Local, Enclosing, Global, Built-in
'''

def outer():
    """
    for a in range(2):
        x = 'global {}'.format(a)

    def outer():
        for b in range(3):
        x = 'outer {}'.format(b)

        def inner():
            # x = 'inner x'
            for c in range(4):
                x = 'inner {}'.format(c)
            print(x)
            print(a, b, c)

        inner()
        print(x)
        print(a, b)

    outer()
    print(x)
    print(a)

    let's understand this step by step
    1 - line 12 is executed
        range(2) = 0,1
        x = 0
        x = global 0
        x = 1
        x = global 1
    final a = 1
    final x = global 1

    2 - line 15 def outer(): gets executed
        b = range(3)
        b = 0
        x = outer 0
        b = 1
        x = outer 1
        b = 2
        x = outer 2
    final b = 2
    final x = outer 2

    3 - line 19 def inner(): gets executed
        c = range(4)
        similarly
        final c = 3
        final x = inner 3

    4 - first print(x) in inner gets executed since inner is called first
    so first print(x) = inner 3
    print(a, b, c) - a from global value is 1, b = 2 and c = 3

    5 - print(x) after inner() gets called is executed
        since this is not a part of the inner local scope,
        x = outer 2 from the outer scope
        c does not exist anymore
        print(a,b) = 1, 2

    6 - both outer and inner scopes are executed and therefore only global scopes remain
        print(x) = global 1
        print(a) = 1
    """
    pass

help(outer)
