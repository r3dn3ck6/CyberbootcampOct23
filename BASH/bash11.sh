#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

# Read three integers representing the sides of a triangle

echo "Enter the length of the first side:"
read side1

echo "Enter the length of the second side:"
read side2

echo "Enter the length of the third side:"
read side3

# Check if the triangle is equilateral, isosceles, or scalene

if [ $side1 -eq $side2 ] && [ $side2 -eq $side3 ]; then
    echo "EQUILATERAL"
elif [ $side1 -eq $side2 ] || [ $side1 -eq $side3 ] || [ $side2 -eq $side3 ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi

#This script prompts the user to input three integers representing the sides of a triangle, 
# checks whether the triangle is equilateral, isosceles, or scalene according to the given conditions, 
# and outputs the result accordingly.

# In Bash scripting, the -eq is a comparison operator used in conditional statements. Specifically, 
# it checks if two numbers are equal. Here's a breakdown of what it does:

# -eq is used to compare if two values are equal.
# It is primarily used for numeric comparison within Bash scripting.
# For example, in the context of your previous script, [ $side1 -eq $side2 ] is checking if the value stored in the variable $side1 
# is equal to the value stored in the variable $side2.
# If the values are indeed equal, the condition evaluates to true, and the corresponding code block associated with that condition is executed.
# It's essential to note that -eq is specifically for numeric comparison. For string or textual comparison, you'd typically use = or ==.

# Here's a list of some comparison operators used in Bash scripting:

# -eq: Equal to
# -ne: Not equal to
# -lt: Less than
# -le: Less than or equal to
# -gt: Greater than
# -ge: Greater than or equal to
# These operators are used within conditional constructs like if statements to compare values and make decisions based on those comparisons.

# In Bash scripting, && is a logical operator used for conditional execution in command lines or scripts. Specifically, && represents the logical AND operator.

# Here's how it works:

# When you use && between two commands or conditions, it means "execute the second command only if the first one succeeds (i.e., returns a zero exit status)."
# In conditional statements like if or in command sequences, && is used to connect multiple commands or conditions in a way that the subsequent command will execute only if the preceding one succeeds.
# For example:

# command1 && command2
# 
# Here, command1 will be executed first, and if it returns a successful exit status (zero), command2 will be executed. 
# If command1 fails (returns a non-zero exit status), # command2 won't be executed.

# In if statements, it can be used to combine multiple conditions. For instance:

# bash
# Copy Example:

# if [ condition1 ] && [ condition2 ]; then
#   Code to execute if both condition1 and condition2 are true
# fi
# 
# This if statement will execute the code block if both condition1 and condition2 are true.

# && helps streamline the execution flow by allowing the script or command line to proceed only when the previous command or condition executes successfully.

# LuckyLucias

# echo "Triangle Check"
# echo "please type the first integer"
# read x
# echo "Please type the second integer"
# read y
# echo "Please type the final integer"
# read z
# if [ $x -eq $y -a $y -eq $z ]
# then echo "EQUILATERAL"
# elif [ $x -ne $y -a $y -ne $z ] 
# then echo "SCALINE" 
# elif [ $x -eq $y -a $x -ne $z -o $y -eq $z -a $y -ne $x ]
# then echo "ISOSCELES"
# fi

# Dylan Williams
# #!/bin/bash
# #script ops 201 class Ops Challenge Solutions
# #Author: Dylan Williams
# #Nov 22 2023

# echo "Please enter 3 sides to a triangle."
# sleep 1
# echo "Please enter side 1 of a triangle."
# read A
# sleep 1
# echo "Please enter side 2 of a triangle."
# read B
# sleep 1
# echo "Please enter side 3 of a triangle."
# read C



# if (( $A == $B && $A == $C && $B == $C ))
#     then
#         echo "This is an Equilateral triangel"
# elif (( $A == $B && $A != $C ))
#     then
#         echo "This is an Isoceles triangle."
# elif (( $A == $C && $A != $B ))
#     then
#         echo "This is an Iscoceles triangle."
# elif (( $B == $C && $A != $B ))
#     then 
#         echo "This is an Isoceles triangle."
# else
#     echo "This is a Scalene triangle." 
# fi

Victor Nieva
# echo "Please Input 3 different values"
# read x; read y; read z

# if (( x >= 1000 || y >= 1000 || z >= 1000 || x == 0 || y == 0 || z == 0)) 
#     then echo "out of range"
#         exit
# fi

# if (( x + y <= z || y + z <= x || z + x <= y ))
#     then echo "not a triangle"
#         exit
# fi

# if (( x == y && y == z ))
#     then echo "equilateral"
# elif (( x == y || y == z || z == x ))
#     then echo "isosceles"
# else
#     echo "scalene"
# fi

