def frequent_num_fast(lst):
    freq_lst = [0] * (max(lst) + 1)

    for value in lst:
        freq_lst[value] += 1

    most_freqNum = freq_lst.index(max(freq_lst))
    return most_freqNum, freq_lst[most_freqNum]


lst = [1, 2, 2, 1, 1, 4, 5]

n1, n2 = frequent_num_fast(lst)

print(f"num{n1},frq{n2}")
