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