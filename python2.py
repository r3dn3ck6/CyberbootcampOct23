# Objectives
# Create if statements using these logical conditionals below.
# Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

# Define variables
a = 20
b = 30

# If statement with a logical conditional and elif
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")


# Create an if statement that includes both elif and else to execute when both if and elif are not met.
    # Take user input and convert it to an integer; The input() function allows user input;
    # https://www.w3schools.com/python/ref_func_input.asp

integer = int(input("Enter a Number: "))
print("Integer is: " + str(integer))  # Printing the integer entered by the user

# If statement with a logical conditional and elif
if integer > 15:
    print("Integer is greater than 15")
elif integer > 5:
    print("Integer is greater than 5 but not greater than 15")
else:
    print("Integer is 5 or less")


    

# Stretch Goals (Optional Objectives)


# Pursue stretch goals if you are a more advanced user or have remaining lab time.



# Create an if statement with two conditions by using and between conditions.




# Create an if statement with two conditions by using or between conditions.




# Create a nested if statement.




# Create an if statement that includes pass to avoid errors.
