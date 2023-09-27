# def pair_bug(lst):
#     pos1, pos2 = 0, 1

#     for i in range(0, len(lst), 2):  # 0 2 4  3
#         for j in range(1, len(lst), 2):  # 1 3  # i+1= 1 , 1 2 3 4 5
#             print(j)
#             if lst[pos1] + lst[pos2] < lst[i] + lst[j]:
#                 pos1, pos2 = i, j


#     return pos1, pos2
def pair_bug(lst):
    pos1, pos2 = 0, 1

    for i in range(len(lst)):  # 0 2 4  3
        for j in range(i + 1, len(lst)):  # 1 3  # i+1= 1 , 1 2 3 4 5
            print(j)
            if lst[pos1] + lst[pos2] < lst[i] + lst[j]:
                pos1, pos2 = i, j

    return pos1, pos2


def main():
    lst = list(map(int, input("Eneter an integer valuse please!: ").split()))
    assert len(lst) > 1
    pos1, pos2 = pair_bug(lst)

    print("output is :", lst[pos1] + lst[pos2])


main()
