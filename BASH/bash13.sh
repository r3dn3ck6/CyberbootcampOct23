#!/bin/bash

echo "Enter a number: "
read user_input

# Check if the user input is between 2 and 5
if (( $(echo "$user_input >= 2 && $user_input <= 5" | bc -l) )); then
    echo "Valid Number"
    echo "Your number is $user_input"
else
    echo "Not valid!"
fi

# This script prompts the user to enter a number, converts the input to a floating-point number, and then checks if it falls between 2 and 5 (inclusive). 
# If the input meets this condition, it will print "Valid Number" along with the user's number. 
# Otherwise, it will print "Not valid!".

