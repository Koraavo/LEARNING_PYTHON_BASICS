import argparse

"""
import math
import argparse

parser = argparse.ArgumentParser(description="Calculate volume of a cylinder")
parser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='Radius of Cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='Height of Cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()


def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * height
    return vol


if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print(f"Volume of a cylinder with radius {args.radius} and height {args.height} is {volume}")
    else:
        print(f"Volume of cylinder = {volume}")

"""
"""
Understanding argparse
Parameters:
"""


# add arguments
# parser.ArgumentParser('prog', # prog is the name of the program, taken from sys.argv[0], name of the file
#                     'usage',
#                     'description',
#                     'epilog',
#                     'parents',
#                     'formatter_class',
#                     'prefix_chars',
#                     'fromfile_prefix_chars',
#                     'argument_default',
#                     'allow_abbreviation',
#                     'conflict_handler',
#                     'addhelp')

# create the parser object
# parser = argparse.ArgumentParser(prog='test.py') # changing name of the file showing when exec the program

#usage:
parser = argparse.ArgumentParser(prog='test.py', # changing name of the file showing when exec the program
                                 # usage='%(prog)s [options]', # changes what should be shown under usage
                                 # description="This is a test program",  # provides a brief description
                                 # epilog="and that's the basis of ArgumentParser",  # provides extra info after des
                                 ) # changing name of the file showing when exec the program

# creating a parent parser object
parent_parser = argparse.ArgumentParser(add_help=False) # no help, so that there is no help conflict

# adding parent optional arguments
parent_parser.add_argument('--parent', type=int, help='int argument expected')

# adding a child parser to the parent parser
foo_parser = argparse.ArgumentParser(parents=[parent_parser])

# second child parser
bar_parser = argparse.ArgumentParser(parents=[parent_parser])

# adding argument to the child parser
foo_parser.add_argument('foo', help='add string argument')
bar_parser.add_argument('--bar', help='add optional string argument')

# regular parser with no parent
# parser.add_argument('--foo', help='foo of the %(prog)s program, name of the file is part1-Argumentparser.py')

# calling parser
# parser.parse_args()
# parent_parser.parse_args()

# calling parent argument's parameter through child parser
# a = foo_parser.parse_args()
# print("A is being printed", a)

# calling second child
b = bar_parser.parse_args()
print("B is being printed", b)

