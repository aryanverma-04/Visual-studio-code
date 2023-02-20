'''This is the tutorial for dictionary in python'''




mydict = {
    'brand' : 'hyundai',
    'model' : 'i10',
    'color' : 'black',
    'color' : 'white'
}
print(len(mydict))

print(mydict['color'])

print(mydict.get('color'))

print(mydict.keys())

mydict['feul'] = 'petrol'

print(mydict.keys())

print(mydict.values())

print(mydict.items())

mydict['year'] = '2017'
print(mydict.items())

if 'year' in mydict:
    print("Year information is also present there..")

mydict.update({'year' : '2010'})
print(mydict)

mydict.pop('color')
print(mydict)

del mydict['brand']
print(mydict)


for x in mydict:
    print(x*2)

for x in mydict:
    print(mydict[x])

for x in mydict.values():
    print(x)


newdict = mydict.copy()
print(newdict)


lst = list(mydict.values())
print(lst)

family = {
    'child1':{
        'name' : 'kalu',
        'age'  : '20'
    },
    'child2':{
        'name' : 'goru',
        'age'  : '69'
    }
}

print(family)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)


for x in mydict:
    print(mydict.keys())

for x in mydict.values():
    if x == 'i10':
        continue
    print(x)

mydict.clear()
print(mydict)

del mydict
print(mydict)
