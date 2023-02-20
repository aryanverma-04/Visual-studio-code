'''Python program to reverse a numberber '''

print("\nAryan verma, Uid: 20bcs361")
number = int(input("Enter a number to find its reverse: "))
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print("Reversed Number: " + str(reversed_number))