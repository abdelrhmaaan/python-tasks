lst = list(map(int, input("Eneter an integer valuse please!: ").split()))

## sol number 1
# mx_num1 = max(lst)
# lst[lst.index(mx_num1)] = 0

# mx_num2 = max(lst)

# print(mx_num2 + mx_num1)

## sol number 2
mx1 = max(lst)
mx2 = 0

for x in lst:
    if x > mx2 and x != mx1:
        mx2 = x


print(mx1 + mx2)
