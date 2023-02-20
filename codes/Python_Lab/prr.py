lst = [12, 33, 44, 1 , 49, 21, 23, 19, 10, 14]

# for l in range(len(lst)-1):
#     print(lst[l]) 
#     lst[l+1] = lst[l]

lst[-1:]
print(lst)
lst = lst[-1:] + lst[:-1]
print(lst)