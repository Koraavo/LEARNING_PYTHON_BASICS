nums = [12, 23, 2, 35, 67, 62, 1, 3, 5, 4, 2, 6, 7]


def evens(stream):
    for n in stream:
        if n % 2 == 0:
            yield n


for n in evens(nums):
    print(n * 2, end=" ")
