# # #How to print to screen in python 
# print("Hissss...")
# print("Hello World!")
# # #Print with no variable cause to skip a line
# print()
# print("Anthony")
# # # Starting your print statment on a new line
# print("The dog ran across the street.\nHe was chasing a car.")
# # # As you can see, the end keyword argument determines the characters the print() function sends to the output once it reaches the end of its positional arguments
# print("My name is", "Python.  ", end="")
# print("Monty Python.")
# # # Seperates each variable with declared - in this case but could use others like comma or colon
# print("My", "name", "is", "Monty", "Python.", sep="-")
# print("My", "name", "is", "Monty", "Python.", sep=";")
# # # prints out with seperation and end statement with * but does not start on new line
# print("My", "name", "is", sep="_", end="*")
# # Line 19 is a string and Line 20 is an integer 
# print("2")
# print(2)
# # This a boolean uses which is True or False in python
# print(True > False)
# print(True < False)
# number = input("Enter a number")
# print(number)

# # # #Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.
# # print("I'm\n" "Learning\n" "Python")

# # # Using python as a calculator
# # print(2+2)
# # # when both ** arguments are integers, the result is an integer, too;
# # # when at least one ** argument is a float, the result is a float, too.
# # print(2 ** 2)
# # print(2 ** 2.)
# # # An * (asterisk) sign is a multiplication operator.

# # # # A / (slash) sign is a division operator.
# # # # A division sign always lead to a float if needed or not
# # print(6 / 3)

# # # # A double // removes float and always rounds
# print(4 / 3)
# print(4 // 3)
# # # # The symobol % is called a  modulo and gives the remainder in divison
# # print(14 % 5)
# # # # 5 goes into 14 twice and gives you a remainder of 4 which is why it printed 4 to the line
# # print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# # # # This equation will complete what is in double parenthsis and then will complete left to right
# # My_Var = 5
# # #This is a variable you can use one word or multiple words with an underscore
# # print(My_Var)
# # # You can call a varibale like above
# # # You can use many variable to achieve you goal
# # Name = "Anthony"
# # print(My_Var, Name)
# # print("My Name is " + Name)
# # # You can declare the variable something else like shown below just remember the code reads line by line going down
# # Name = "Steve"
# # Last_Name = "John"
# # print(Name)
# # Name = Name + " Joe"
# # print(Name)
# # # Using math and rounding in varibales to get expected outcomes
# # # The round command rounds the nubmer to 1 2 or 3 decimal points as defined
# # kilometers = 12.252263
# # miles = 7.38515

# # miles_to_kilometers = (miles * 1.61)
# # kilometers_to_miles = (kilometers / 1.61)
# # # print(miles + kilometers)

# # print(miles, "miles is", round(miles_to_kilometers, 4), "kilometers")
# # print(kilometers, "kilometers is", round(kilometers_to_miles, 3), "miles")


# # #input allows the computer to read the user input
# # print("Tell me something")
# # anything = input()
# # print("Thanks for telling me", anything)
# # # you can use the input function to print to the terminal also and ask user for input
# # color = input("Tell me a color\n")
# # print("Is", color, "your favorite color")
# # # You can prints multiple strings or variable in one line 
# # print(anything + " wow " + color)
# # print(color * 8)
# # # convert a number into a string with
# # str(7)

# # # # a double == compares to things together in python
# print(2 == 2)
# print(1 == 2)
# # # # One will print out True and the other will print out False since its comparing the values
# # # # != is not equal to like show below
# # print(2 != 3)
# # # Could use > or < or >= or <= also to compare variables or numbers 
# # print(2 >= 1)
# # # # example with using variable
# dogs = .5
# print(dogs >= 1)
# # Basic if or else statment in python
# weather = input("Is the weather good or bad\n")
# if weather == "good":
#     print("lets go for a walk")
# else:
#     print("lets stay inside")

# income = float(input("Enter the annual income: "))
# # Using the round function in an if or else stament to round total
# if income < 85528:
# 	tax = income * 0.18 - 556.02
# else:
# 	tax = (income - 85528) * 0.32 + 14839.02

# if tax < 0.0:
# 	tax = 0.0
# # We could change the zero on the end of round to go out more decimals
# tax = round(tax, 0)
# print("The tax is:", tax)


# # While loop in python  a loop will keep running till the while is met you can have an infiinte loop
# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# The loop here counts down till the counter does not equal 0 and counts down by 1 each time it runs
# 

# Lets learn about a for loop 
# i = 0
# for i in range(2, 4):
#     print("hello")
#     pass


# while True:
#     word = input("You're stuck in an infinite loop!\nEnter the secret word to leave the loop: ")
#     if word == "chupacabra":
#         break
# print("You've successfully left the loop!")
# This is a loop with an if or else statement
#counter = 10
# while counter > 5:
#     print("Your number is two high", counter)
#     counter -= 1
# else:
#       print("Your Number is to low")
# pass
# import math
# dir(math)