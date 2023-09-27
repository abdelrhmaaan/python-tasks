def arg2max(lst):
    # check if the list len < 2
    if len(lst) < 2:
        return None, None

    max1pos, max2pos = 0, 1

    if lst[max1pos] < lst[max2pos]:
        max1pos, max2pos = 1, 0

    for curPos in range(2, len(lst)):
        if lst[max1pos] < lst[curPos]:
            max1pos, max2pos = curPos, max1pos
        elif lst[max2pos] < lst[curPos]:
            max2pos = curPos

    return max1pos, max2pos


lst = [2, 15, 29, 24, 23, 55]
mx1, mx2 = arg2max(lst)
print(lst[mx1], lst[mx2])
