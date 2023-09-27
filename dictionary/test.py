a = [x for x in range(100)]

dc = dict.fromkeys(a, "6")

keys = dc.fromkeys(a).keys()
print(keys)
