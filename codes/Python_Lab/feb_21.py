# '''This is the tutorial for tuples in python'''


mytuple = ('apple', 'cherry', 'banana', 'kiwi','jackfruit', 'orange','watermelon')
# # print(mytuple)

# # print(len(mytuple))
# # newtuple = ("apple")
# # print(type(newtuple))

# # newtuple = ("apple",)
# # print(type(newtuple))

# '''we can also inititlize a tuple using the tuple constructor ()'''


# # newtuple = tuple(('2l9','2','uuus'))
# # print(type(newtuple))

# '''the tuple's index starts with 0'''
# ''' [starting index : ending index : jump ]'''

# # print(mytuple[3])
# # print(mytuple[-3])
# numtuple = (0,1,2,3,4,5,6,7,8,9,10)
# # print(numtuple[2:5])
# # print(numtuple[:4])
# # print(numtuple[5:])
# # print(numtuple[:-3:2])

# # if 'apple' in mytuple:
#     # print("Present")

# y = list(mytuple)
# y[0] = 'papaya'
# # y.append('grapes') ''' Append adds the item to the last of the list'''
# mytuple = tuple(y)
# # print(mytuple)
# # mytuple[3] = 'jaj'  !!! Cannot do as tuple does not supports direct item assignment
# # print(type(mytuple))

# '''We can add a tuple to another tuple'''

# # mytuple = mytuple + numtuple
# # print(mytuple)
# # print(len(mytuple))

# y.remove('papaya')
# mytuple = tuple(y)
# # print(mytuple)

# ''' Unpacking a tuple'''
# # (a,b,c,d,*e) = mytuple
# # print(type(a))
# # print(b)
# # print(type(e))

# # (a,*d,e) = mytuple
# # print(type(a))
# # print(type(d))
# # print(type(e))

# # for x in mytuple:
#     # print(x)

# # # for x in range(len(mytuple)):
# # #     # print(mytuple[x])
# # #     print(x)
# # i = 0
# # while i < len(mytuple):
# #     print(mytuple[i])
# #     i = i + 1

# # multi = mytuple * 2
# # print(mytuple)
# # print(multi)

# # print(mytuple.count('banana'))

# # mytuple = mytuple * 2
# # print(mytuple.count('banana'))

print(mytuple.index('apple'))