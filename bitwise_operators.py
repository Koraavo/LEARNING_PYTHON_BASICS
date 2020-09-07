def add_fun(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a


print(add_fun(2, 3))
print(add_fun(12, 15))

"""
Operator	Name	Description
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""