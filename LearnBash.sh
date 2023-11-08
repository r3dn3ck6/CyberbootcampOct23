# #!/bin/bash
# # Learning bash 
# # Use pound sign to comment out lines 

echo "Hello Class"
# # to Run bash script ./nameofscript

variable=8
echo $variable



# # Read command Allows user to input variable data
echo "Enter a number"
read Number
echo "Lets do math"
#This is a variable we call a variable by using $ + variable name
 Number1=9
echo "Please enter a number"
# # The read command here is reading the data the user plugs into the command line and will use that number as the variable later in the program
read Number1
Number2=11

# # # We can do math inside a variable by coding like the example below
total=$((Number1 * Number2))
#we can use a variable and user created text when echo stuff out also
echo $total
echo "your total is "  $total

echo $Number1
echo $Number2

# # #This is an array were we can put multiple items in a variable and call or only certain ones
# # array is variable for multiple items
myarray=("dog" "cat" "bunny")
# # When counting in an array remember that the computer starts at 0 and counts up from there like here we would have 0, 1, 2
names=("andrew" "anthony" "ashley" "Joe" "Pete" "Steve")

echo ${names[@]}
# echo ${names[2]}
echo ${names[@]: 1:4}


# if and else statments

# if [ $number > 5 ]
#      then echo "Number is greater than 5"
# elif [ $number < 5 ]
#     then echo "Number is less than 5"
# else [ $number = 5 ]
#     then echo "Number is 5"
# fi

#While loop run till acceptance not met
user=y
while [ $user = y ]
do
echo "Please make a selection"
echo "1 to print hello world" 
echo "2 ping yourself"
echo "3 to show network config"
read input
    if [ $input = 1 ]
        then echo "Hello World!"
    elif [ $input = 2 ]
        then ping -c 1 192.168.0.1
    elif [ $input = 3 ]
        then ifconfig
    else echo "Invalid entry"
fi
echo "do you want to play again: y/n"
read user
done
echo "good work"

# #functions is to be called multiple times by only using function name
echo "Enter 2 numbers to add"
read num1
read num2
function add(){
    sum=$(( $num1 + $num2 ))
    echo $sum

}
add

x=1
until [ $x -gt 6 ]
do
    echo "x is $x"
    ((x++))
done
./LearnBash.sh