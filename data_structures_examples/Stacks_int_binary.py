"""
Convert integer to binary
Example: 242
242/2 = 121 --> 0 ( bottom of the stack)
121/2 = 60  --> 1
60/2 = 30   --> 0
30/2 = 15   --> 0
15/2 = 7    --> 1
7/2 = 3     --> 1
3/2 = 1     --> 1
1/2 = 0     --> 1 (top of the stack)


"""

from LEARNING_PYTHON_BASICS.Data_structures.Stacks import Stack


def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_number = ""
    while not s.is_empty():
        bin_number += str(s.pop())

    return bin_number


print(div_by_2(242))
