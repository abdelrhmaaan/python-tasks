lst = list(map(int, input("enter integer number: ").split()))


def indlst(lst):
    frst_mx = max(lst)
    idx_mx1 = lst.index(frst_mx)
    lst[idx_mx1] = min(lst) - 1
    scd_mx = max(lst)
    idx_mx2 = lst.index(scd_mx)
    lst[idx_mx1] = frst_mx
    return idx_mx1, idx_mx2


idx1, idx2 = indlst(lst)

print(
    "frist index:",
    idx1,
    "1st max:",
    "st[idx1]",
    "\n" + "second index",
    idx2,
    "2nd max:",
    "lst[idx2]",
)
print(lst[4])
