# #!/bin/bash

# # Lets create a function in bash that adds two number together
# # Stretch goal can you do subtraction, multipliaction or division
# # You will need to declare two variables

echo "Enter 2 numbers to add"
read num1
read num2
function add(){
    sum=$(( $num1 + $num2 ))
    echo $sum

}
add

echo "Enter 2 numbers to subtract"
read num1
read num2
function difference(){
    difference=$(( $num1-$num2 ))
    echo $difference

}
difference

echo "Enter 2 numbers to divide"
read num1
read num2
#Check if denominator is not zero to avoid division by zero
if [ $num2 = 0 ] 
   then
   echo "Error: Division by zero is not allowed."
else
    function divide(){
        result=$(( $num1 / $num2))
        echo $result
}
divide


echo "Enter 2 numbers to multiply"
read num1
read num2

function multiply() {
    product=$((num1 * num2))
    echo $product
}

multiply

fi
# ./bash4.sh