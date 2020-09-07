"""
Write a program to solve the following problem:
You have two jugs:
a 4-gallon jug and a 3-gallon jug.
Neither of the jugs have markings on them.
There is a pump that can be used to fill the jugs with water.
How can you get exactly two gallons of water in the 4-gallon jug?
"""


def two_gal():
    jug1_size, jug2_size = 4, 3
    jug1, jug2 = 0, 0
    final_size = 2

    if jug1_size > final_size:
        jug1 = jug1_size - jug2_size

    if jug1 < final_size:
        jug2 = jug1
        jug1 = 0

    if jug1 != final_size:
        jug1 = jug1_size
        if jug2 != jug2_size:
            jug2 = jug2_size - jug2
            jug1 = jug1_size - jug2
            return jug1


print(two_gal())

