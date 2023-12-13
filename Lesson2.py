#  # List in python also none as arrays in other language are used to hold muplitple items under one variable
# numbers = [10, 5, 7, 2, 1]

# print("Original list contents:", numbers)
# # Printing original list contents.

# numbers[0] = 111
# print("New list contents: ", numbers)
# # Current list contents.
# # copies value of 5th number to second
# numbers[1] = numbers[4]
# print("New list contents: ", numbers)
# print("list length ",len(numbers))
# # # Using del to remove value from list
# del(numbers[1])
# print("New list contents: ", numbers)
# # # Use a negatvive number to count list backwards
# print(numbers[-1])
# print(numbers[-2])
# # # add new values to end of list with append
# numbers.append(12)
# print("New list contents: ", numbers)
# # # Use insert to add value to certain place in list
# numbers.insert(2,23)
# print("New list contents: ", numbers)


# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in my_list:
#     total += i

# print(total)
# # Use the sort command to make list numbers be in order or reverse to go the other way
# my_list.sort()
# print(my_list)

# my_list.reverse()
# print(my_list)

# del my_list[1]
# print(my_list)
# #print how many variables are in list with len command
# print(len(my_list))
# # This for loop will print the longest number in the list
# my_list = [10, 1, 8, 3, 5]
# largest = my_list[0]
# for i in my_list:
#     if i > largest:
#         largest = i
# print(largest)


# functions in python 
# def addition():
#     print("Enter a value")
#     a = int(input())
#     print("Enter another value")
#     b = int(input())
  
#     print(a + b)
# addition()


# I can call this addition function anywhere any my code after this point and it will run lines 55 through 61
# def name(first, last):
#     print("Hello my name is", first, last)

# name("anthony", "ingargiola")
# name("Micheal", "Scott")
# name(first = input("Enter first name "),last = input("Enter last name "))
# using a variable inside of a function

# def my_function():
#     var = 2
#     print("Do I know that variable?", var)


# var = 1
# my_function()
# print(var)

# # global names the variable any where on the script not just in the single funciton 
# def my_functions():
#     global var
#     var = 2
#     print("Do I know that variable?", var)


# var = 1
# my_functions()
# print(var)
# # Using math in function with variable

# def savings(earnings,):
#     return earnings * .2

# print("You should save", savings(50000))