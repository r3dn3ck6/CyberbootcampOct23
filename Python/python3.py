# Scenario
# Using one of the comparison operators in Python, write a simple program that takes the parameter n as input,
#  which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.


integer = int(input("Enter a Number: "))
print("Integer is: " + str(integer))  # Printing the integer entered by the user

# If statement with a logical conditional and elif
if integer > 100:
    print("True")
elif integer < 100:
    print("False")

    n = int(input("Enter a number:"))
m = 100
if n >= m:
    print("True")
else: print ("False")

#Victor's Code
n = int(input("Enter a number:"))
m = 100
if n >= m:
    print("True")
else: print ("False")