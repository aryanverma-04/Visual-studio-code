'''Exp 2'''

s = input("Enter the string: ")

s2 = ""
for i in range(0,len(s)):
    if i % 2==0:
        s2 += s[i] 
    else:
        pass

print("The new string is :",s2)
