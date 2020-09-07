def understanding_sets():

    """
    This is how you perform the well-known operations on sets in Python:

    A | B
    A.union(B)
    Returns a set which is the union of sets A and B.
    A |= B
    A.update(B)
    Adds all elements of array B to the set A.
    A & B
    A.intersection(B)
    Returns a set which is the intersection of sets A and B.
    A &= B
    A.intersection_update(B)
    Leaves in the set A only items that belong to the set B.
    A - B
    A.difference(B)
    Returns the set difference of A and B (the elements included in A, but not included in B).
    A -= B
    A.difference_update(B)
    Removes all elements of B from the set A.
    A ^ B
    A.symmetric_difference(B)
    Returns the symmetric difference of sets A and B (the elements belonging to either A or B, but not to both sets simultaneously).
    A ^= B
    A.symmetric_difference_update(B)
    Writes in A the symmetric difference of sets A and B.
    A <= B
    A.issubset(B)
    Returns true if A is a subset of B.
    A >= B
    A.issuperset(B)
    Returns true if B is a subset of A.
    A < B
    Equivalent to A <= B and A != B
    A > B
    Equivalent to A >= B and A != B
    """

    x={1,2,3}
    y={2,3,4}

    print (x|y) # union on x and y = 1, 2, 3, 4 {A.union(B)}
    # print(x |= y) # A.update(B)
    # Adds all elements of array B to the set A.
    print(y-x)
    print(x & y) # A.intersection(B)
    # Returns a set which is the intersection of sets A and B.
    #print(x &= y)
    print(x - y)
    print(x ^ y) # A.symmetric_difference(B)
    # the elements belonging to either A or B, but not to both sets simultaneously.

    if x.issubset(y): # lines of code will determine if all elements of x are in y ?
        print (True)
    else:
        print (False)
    return

help(understanding_sets)


