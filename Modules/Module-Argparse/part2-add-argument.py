import argparse

add_argument('name/flage',
             'action',
             'nargs',
             'const',
             'default',
             'type',
             'choices',
             'required',
             'help',
             'metavar',
             'dest'
             )
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--foo')
parser.add_argument('bar')

a = parser.parse_args()
print(a)

# if you wish to print the output at dict
b = parser.parse_args()
print(vars(b))


