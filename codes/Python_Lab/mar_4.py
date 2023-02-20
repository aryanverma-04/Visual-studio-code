# from cmath import sqrt
# import math
# print(sqrt(16))

def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


x = int(input("Enter a number:"))

result = fact(x)

print("Factorial is:", result)