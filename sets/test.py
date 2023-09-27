lst = [[1, 2], [3, 1], [3, 1], [3, 1]]


def lstOfLists(lst):
    emp = []
    for item in lst:
        for num in item:
            emp.append(num)
    st = set(emp)
    return st


# print(lstOfLists(lst))
print(tuple(lst))
