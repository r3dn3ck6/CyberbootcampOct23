#!/bin/bash
# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is

#until Loop

x=0
until [ $x -gt 10 ]
do
    echo "x is $x"
    ((x++))
done

# This script initializes a variable x with a value of 0 and runs an until loop until the value of x is greater than 10. 
# Inside the loop, it echoes the current value of x and then increments it by 1 using ((x++)).