'''Program to calculate polynomial equation of a given polynomial'''

import math
lst = []
print("\nName: Aryan verma, UID:20bcs3651")
print("Enter the coefficient to calculate the values ")
for i in range(0,4):
    a = int(input("Enter the coefficient: "))
    lst.append(a)
x = int(input("Enter the value of x: "))
sum1 = 0
j = 3
for i in range(0,3):
    while (j>0):
        sum1 = sum1 + (lst[i]*math.pow(x,j))
        break
    j = j-1

sum1 = sum1+lst[3]

print(sum1)
