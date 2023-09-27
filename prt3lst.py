# define a function that takes


def argmax(lst):
    # check if the list its len is < 1?
    if len(lst) < 1:
        return None
    return lst.index(max(lst))


def max2nums(lst):
    idx1 = argmax(lst)
    temp = max(lst)
    lst[idx1] = min(lst) - 1
    idx2 = argmax(lst)
    lst[idx1] = temp
    return idx1, idx2


lis = [2, 3, 6, 4, 6, 7, 9]
idx1, idx2 = max2nums(lis)
print(lis[idx1], lis[idx2])
