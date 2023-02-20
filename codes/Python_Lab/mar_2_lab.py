'''Lab session 20ONBIS-1_B'''

# for i in range(0,6):
#     print(i*'*', end='  ')
#     print(" ")
    

# for i in range(0, 5+1):
#     for j in range(0, i):
#         print("*", end=' ')
#     print(" ")

# for i in range(5, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

lst = []
n = input("Enter the number seprated by space: ")
lst = n.split()
print(lst)

for i in lst:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")