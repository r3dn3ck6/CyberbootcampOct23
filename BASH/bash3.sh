#!/bin/bash
# Condtinal Statment 
# This ops challenges is about conditinal stamtment of if else statments and how they work
# We are going to take a varibale with the number and have the computer tell us if its greater than 5 less than 5 or equals 5

# In this script:

# We define a variable number with the value.
# We use an if statement to check the value of the number variable.
# The -gt flag checks if the number is greater than 5.
# The -eq flag checks if the number is equal to 5.
# If the number is greater than 5, it will execute the code inside the first if block.
# If the number is equal to 5, it will execute the code inside the elif block.
# If neither condition is met, it will execute the code inside the else block.
# You can modify the script to suit your specific needs by changing the variable value and adjusting the conditions accordingly.




# Define the variables
number=200

# Check if the number is greater than 100
if [ "$number" -gt 5 ]; then
  echo "The number is greater than 5."
elif [ "$number" -eq 5 ]; then
  echo "The number is equal to 5."
else
  echo "The number is less than 5."
fi