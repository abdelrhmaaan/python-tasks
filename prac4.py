lst = [2, 4, 4, 4, 4, 5, 2, 2]


def rpeated_num(lst):
    cnt = 1
    rp_num = min(lst)
    for i in range(len(lst)):
        Cucnt = 1
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                Cucnt += 1

        if cnt < Cucnt:
            cnt = Cucnt
            rp_num = lst[i]
        elif cnt == Cucnt and rp_num > lst[i]:
            rp_num = lst[i]

    return rp_num, cnt


num, cnt = rpeated_num(lst)

print(f"num{num} and coutn {cnt}")
