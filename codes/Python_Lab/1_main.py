# import math
# print("Hello")
# # if (10>3):
# #     print("10 is greater than 3")
# # else:
# #     print("10 is smaller than 3")

# This is a single line comment in python 

''' This
    is
    a
    multiline 
    comment 
    in 
    python
'''

# print("The value of factorial 5 is:",math.factorial(5))

# print("Hello Python")

# if ( 10> 3):
#      print("10 is always greater than 3")
#      print("Prove if you can !! ")

# The indentation in python must be of equal 

'''THis is a multiline comment in python
    this is the second line of the multiline comment
                                                        '''


# x = 5
# y = 's'
# z = "How are u "


# from argparse import _MutuallyExclusiveGroup
# from cgi import print_directory
# from operator import truediv
# import this
# from traceback import print_list


# x = str(3)
# y = int(3)
# z = float(3)
# print(x,y,z)

# x = y = z = 'Hello world'

# x, y, z = 'apple', 'samsung' , 'vivo'

# fruits =  ['apple', 'samsung', 'vivo']
# x, y, z = fruits


# print(x,y,z)
# print(type(x))
# print(type(y))
# print(type(z))

# x = "python"
# print("this is "+x)

# x = "python"
# y = "is awesome"
# z = x + y
# print(z)

# x = 5
# z = x + y
# print(z)

# my_var = "awesome δ"

# def mufunc():
#     global my_var 
#     my_var = "fantastic"
#     print("Python is :"+my_var)

# mufunc()
# print(my_var)

# x = 5j
# print(type(x))

# x = memoryview(bytes(4))	
# print(x)

# x = 20e3
# print(type(x))

# x = 5 + 10j
# y = 15 + 20j
# print("The sum of two complex numbers is:",x+y)

# x, y, z = 3, 12.22, 19j
# print(x,y,z)
# print(type(x))
# print(type(y))
# print(type(z))

# a = complex(y)
# print(a)
# print(type(a))

# import random
# print(random.randrange(1,100000))

# x = int("3")
# print(x)

# we can make multiline string in python as same as we make multiline comments

# s = '''this 
# is 
# a 
# mutliline
# string 
# in 
# python'''

# print(s)

# x = 'Hello world'
# print(x[4])

# for x in 'banana khalo friends':
#     print(x)

# x = 'banana khalo friends'
# print(len(x))
# print('banana' not in x)
# if "banana" in x:
    # print("banana is present in the text")
# print(x[5:10])
# print(x[:10])
# print(x[10:])

# b = "Hello, World!"
# print(b[-5:-2])

# s = "Hello my name is aryan"

# print(s)
# print(s.upper())
# print(s.lower())
# print(s.strip())
# print(s.replace('a','H'))
# print(s.split(' '))

# '''We can easily concatenate two strings and also place some text between the strings'''

# a = "aryan"
# b = 'verma'
# c = a+"░"+b
# print(c)

# age = 19
# s = "I'm aryan and my age is "+age
# print(s)
# year = 2
# s = "I'm aryan and my age is {1} and im current in {0} year \n"
# print(s.format(age,year))

# txt = "We are the so-called \"Vikings\" from the north."

# print(txt)
 
# s = 'Hello I\'m aryan and what is your\'s name'
# print(s)

# s = "hello my name is Aryan eeeeeeeeeeeeeeee"
# print(s.capitalize())
# print(s.center(1000))
# print(s.count('e'))   

# s = 'Hello'
# x = s.encode()
# print(x)

# print(10>3)

# num1,num2 = input("Enter two numbers: ").split()

# if (num1>num2):
#     print("Number entered first is greater")
# else:
#     print("Number entered secound is greater")

# class myclass():
#   def myclass(aabbcc):
#       return 4

# myobj = myclass()
# print(bool(myobj))

# def myfunc():
    # return True
# print not (myfunc())

# x = 200
# print(isinstance(x, str))

# x = 3
# # print(2**x)

# '''Now we are at the type of inbuilt datatypes in python like lists, sets, dictionary and Tuples'''

# from audioop import add
# from cgi import print_directory
# from cmath import sin
# import email
# from typing_extensions import Self
# from unicodedata import name


mylist = ['Samsung', 'apple', 'Vivo','realme','oppo','Jio']
# print(mylist)
# print(type(mylist))
# print(len(mylist))

newlist = ['a',1,'aryan',9399]
# print(newlist)
# print(mylist[:1])

# if 'samsung' in mylist:
    # print("true")
# mylist[2] = 'realme'
# mylist[1:] = ['corona', 'dengue', 'maleria']
# mylist[1:4] = ['mids']
# mylist.insert(1,'realme')
# mylist.append('Micromax')
# mylist.extend(newlist)
# mylist.insert(0,'apple')
# mylist.remove('apple')
# mylist.remove('apple')
# mylist.pop(0)
# del mylist[0]
# del mylist
# mylist.clear()
# for i in range(len(mylist)):
    # print(mylist)
# print(mylist)

# i = 0
# while i < len(mylist):
    # print(mylist[i])
    # i+=

# newlist = []
# for x in mylist:/
    # if 'a' in x:
        # newlist.append(x)
# print(newlist)
# x = 2
# for i in range(x):
    # print("h")

# newlist = [x for x in range (3)]
# newlist = [x for x in range(10) if x < 5]
# newlist = [x.upper() for x in mylist]
# newlist = [ x for x in range(mylist)]
# mylist.sort(reverse=1)
# mylist.sort()
# print(mylist)

# newlist.sort()
# print(newlist)

# thislist = [100, 38,59,33, 87,56,73]
# def myfunc(n):
#     return abs(n - 50)
# thislist.sort(key=myfunc)
# print(thislist)

# mylist.sort(key=str.lower)
# mylist.reverse()
# print(mylist)
# thislist = mylist.copy()
# print(thislist)

# finalist = list(mylist)
# print(finalist)
# list3 = mylist+ newlist
# print(list3)
# print("Hello world")
# import this

'''Tuple in python are ordered/ unchangble/ and allows Duplicates'''

# print("Tuple Tutorials")

mytuple = ('apple', 'samsung', 'realme','vivo','oppo','motorola')
# print(mytuple)
# print(type(mytuple))

# print(len(mytuple))

# singletuple = ("samsung",)
# print(type(singletuple))

# thistuple = tuple(("aryan", 'verma'))
# print(type(thistuple))

# print(mytuple[2])
# print(mytuple[-5])

# print(mytuple[:2])
# if 'samsung' in mytuple:
    # print("samsung is present in the tuple")

# y = list(mytuple)
# y.insert(2,'nokia')
# print(type(y))
# mytuple = tuple(y)
# print(type(mytuple))
# print(mytuple)

# '''we can also print a list in reverse order by using the following syntax'''
# print(mylist[::-1])     

'''Conditional statements, Loops and functions in Python'''

# a = 2
# b , c = 2, 's'
# if a > b :
#     print("a is greater than b")
# else:
#     print("b is greater than a ")
# # if a > c :
#     # print("c is smaller")

# if c =='d':
#     print("the character stored at c is \"s\" ")
# elif a != b:
#     print("the value of a and b is not matching")


# a = int(input("Enter two numbers "))
# b = int(input("Enter two numbers "))
# # a,b = int(input("Enter two numbers ")).split()
# if a == b:
#     print("a is equals to b")

# if 3 > 1: print("equal")
# a = 2 
# b = 2
# print("A") if a > b else print("=")if a ==b else ("B")

# import datetime

# x = datetime.datetime.now()
# # print(x)
 
# a = 20
# n = 33
# if a == 10:
#     print("Greater than 10")
#     if a >=20: print("Greater than or equals to 20")
#     elif n == 33:
#         print("N = 33")
# else:
#     print("n is not equals to 33")

# i = 1
# while i <= 10:
#     if i % 2==0:
#         print(i)
#     # if i == 5: break

#     i+=1
# else:
#     print("Completed Loop")

# fruits = ["samsung", "Apple", "Nokia","realme"]
# for x in fruits:

    # print(x)

# for x in 'banana cherry':
#     if x == 'a':
        
#     else:
#         print(x)

# for x in range(17,171,17):
#     print(x)

# for x in range(0,6+1):
#     print(x)

# for x in range(10):
#     if x ==5: break
#     print(x)
# else:
#     print("executed finally")

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# for x in [0,1,2]:
    # pass

# def my_func():
    # print("!! Function called !!")

# my_func()

# def mailer(address):
    # print("An email has been sent to -> "+address)

# mailer("aryanvermacu.official@gmail.com")

# def fullname(f_name,l_name):
    # print(f_name+" "+l_name)
# fullname("Aryan","Verma")
# fullname("hshk")

# def my_func(*kids):
#     print("The youngest children is : "+kids[0])
#     print("The eldest children is : "+kids[2])

# my_func("kalu","goru","Taklu")

# def fun(child_1, child_2):
#     print("The child 1 is : "+child_1)
#     print("The child 2 is : "+child_2)

# fun(child_1='lalu',child_2='goru')

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# def country(home="India"):
    # print("The home country is : "+home)

# country("Cananda")

# brands = ['samsung','nokia', 'apple'.upper()]
# # print(brands)
# def printer(food):
#     for x in food:
#         print(x)
# printer(brands)

# def returner(x):
    # return x * x

# # print(returner(2000000000000000000000000000000000000000000000000000000000000000000))

# def damm():
#     pass
# # damm()

# def tri_recursion(k):
#   if(k > 0):
# #     result = k + tri_recursion(k - 1)
# #     print(result)
# #   else:
# #     result = 0
# #   return result

# # print("\n\nRecursion Example Results")
# # tri_recursion(10)

# '''Lambda function in Python'''

# # x = lambda a,b,c,d,e: a * b + c - d / e
# # y = int(x(10,11,12,13,14))
# # print(y)

# # def my_func(n):
#     # return lambda a : a * n
# # my_doubler = my_func(2)
# # print(my_doubler(11))



# '''Object oriented programming in python'''

# # class myclass:
# #     x = 'Hello world'

# # var = myclass()
# # print(var.x)

# # # class person:
# # #     def __init__(aabbcc, name , age):
# # #         aabbcc.name = name
# # #         aabbcc.age = age
    
# # #     def info(aabbcc):
# # #         print("My name is -> "+aabbcc.name+" and my age is -> "+aabbcc.age+" 😂😂😂👌")

# # # p1 = person("Aryan", '19')
# # # print(p1.info())
# # # # print(p1.name)
# # # # print(p1.age)


# # class person:
# #     def __init__(aabbcc, name , age):
# #         aabbcc.name = name
# #         aabbcc.age = age
    
# #     def info(aabbcc):
# #         print("My name is -> "+aabbcc.name+" and my age is -> "+aabbcc.age+" 😂😂😂👌")

# # p1 = person("Aryan", '19')
# # p1.age= '112.22'
# # del p1.age
# # print(p1.info())
# # # print(p1.name)
# # # print(p1.age)

# # class person :
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
    
# #     def info(self):
# #         print("The name of the person is " + self.name+ " the age of the person is "+ self.age)

# # p1 = person("aryan", "19")
# # # p1.info()

# # class students (person):
# #     def __init__(self,n):
# #         self.n = n
# #         print("Child's Init function is called !!")

# # s1 = students('hDS')

# class person :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print("The name of the person is " + self.name+ " the age of the person is "+ self.age)

# class student (person):
#     def __init__(self, name, age,year):
#         super().__init__(name, age)
#         self.graduationyear = year
    
#     def welcome(self):
#         print("Welcome", self.name, self.age, "to the class of", self.graduationyear)

# x = student("aryan","29","2024")
# x.welcome()

