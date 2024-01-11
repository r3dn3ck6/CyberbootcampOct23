# Today we are going to create a random password generator using for loops and arrays in python
# Make sure to print you password to the screen
#Can you randomize your password generated

# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))

# password = []

# # Loop for generating letters
# for char in range(1, nr_letters + 1):
#     password.append(random.choice(letters))

# # Loop for generating symbols
# for char in range(1, nr_symbols + 1):
#     password.append(random.choice(symbols))

# # Loop for generating numbers
# for char in range(1, nr_numbers + 1):
#     password.append(random.choice(numbers))

# # Shuffle the password to randomize the order
# random.shuffle(password)

# # Convert the password list to a string
# final_password = ''.join(password)

# # Print the final password
# print(f"Your random password is: {final_password}")


#####################################################################

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Combine all characters into a single list
all_characters = letters + numbers + symbols

# Generate the password by randomly selecting characters
password = [random.choice(all_characters) for _ in range(nr_letters + nr_symbols + nr_numbers)]

# Shuffle the password to randomize the order
random.shuffle(password)

# Convert the password list to a string
final_password = ''.join(password)

# Print the final password
print(f"Your random password is: {final_password}")

#######################################################################################################

import random

# Define character sets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_-+=[]{}|;:,.<>?/'

# Combine all characters into a single string
all_characters = letters + numbers + symbols

# Set the length of the password
password_length = 12  # You can adjust this as needed

# Generate the password using a loop
password = ''.join(random.choice(all_characters) for _ in range(password_length))

# Print the generated password
print("Your random password is:", password)

####################################################################################

import random

# Define character sets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_-+=[]{}|;:,.<>?/'

# Combine all characters into a single string
all_characters = letters + numbers + symbols

# Set the length of the password
password_length = 12  # You can adjust this as needed

# Initialize an empty string to store the password
password = ''

# Generate the password using a loop
for _ in range(password_length):
    password += random.choice(all_characters)

# Convert the password to a list and shuffle to randomize
password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)

# Print the generated and randomized password
print("Your random password is:", final_password)
