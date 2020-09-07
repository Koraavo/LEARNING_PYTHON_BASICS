def reverseList(lst):
    # your code here
    if not lst:
        return []
    else:
        new_list = []
        new_list.append(lst.pop())
        return new_list + reverseList(lst)


print(reverseList([1, 2, 3, 4, 5]))