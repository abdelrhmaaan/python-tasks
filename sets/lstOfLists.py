# def lst_of_lsts(lsts):
#     st = set()
#     result = []
#     cnt = 0
#     for lst in lsts:
#         tup = tuple(lst)
#         cnt += 1
#         if tup not in st:
#             st.add(tup)
#             result.append(lst)

#     return result

# lsts = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6]]

# out = lst_of_lsts(lsts)
# print(out)


def lst_of_lsts(lsts):
    st = []  # Changed to an empty list
    result = []
    cnt = 0
    for lst in lsts:
        # tup = tuple(lst)
        cnt += 1
        if lst not in st:
            st.append(lst)  # Changed to append the tuple to the list

            result.append(lst)

    return result


input_list = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6]]
unique_lists = lst_of_lsts(input_list)
print(unique_lists)
