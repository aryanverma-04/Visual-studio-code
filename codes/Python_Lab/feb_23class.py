# age = eval(input("Enter age: "))
# print(type(age))
# print(age)
# f = "aryan"
# l = "verma"
# print("My name is {} {} ".format(f,l))
# print(f.split('a'))

'''List comprehension'''

lst = [[1,2,3],[4,5,6],[7,8,9]]
# print(lst)
l = []
for i in lst:
    print(i)
    l.append(i[1])
print(l)

m = [i[1] for i in lst]
print(m)


