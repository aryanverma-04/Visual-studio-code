#Python program to generate Fibonacci series upto 100
a = 0 #Initialize a with 0
b = 1 #Initialize b with 1
sum = 0
print("Name: Aryan verma, UID: 20Bcs3651")
print("Fibonacci Series upto 100 is : \n")
while(sum < 100): # condiition so that number less than 100 prints
  print(sum)
  a = b
  b = sum
  sum = a + b