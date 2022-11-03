lst =  [12,24,35,24,88,120,155,88,120,155]

lst = lst[::-1]   #reversing the list so that we can get original order reversed
res_set = set()   
res_lst = []

for i in lst:
    if i not in res_set:
        res_lst.append(i)
        res_set.add(i)

print(res_lst)


