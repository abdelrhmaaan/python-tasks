# list [0], [8] = [8],[0]

def reverse_lst(lst):
    
    for inx1 in range(len(lst)//2):
        inx2 = len(lst) -1 -inx1 
        lst[inx1] , lst[inx2] = lst[inx2],lst[inx1]

def prnt_lst():
    lst = list(map(int ,input("enter intger nums: ").split()))

    reverse_lst(lst)

    print(lst)


prnt_lst()    