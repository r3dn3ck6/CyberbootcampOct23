#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry

user=y
while [ $user = y ]
 do
 echo "Please make a selection"
 echo "1 to print hello world" 
 echo "2 ping a website or ip address"
 echo "3 to show network config"
 read input
     if [ $input = 1 ]
         then echo "Hello World!"
     elif [ $input = 2 ]
         then
            echo "Enter website or ip address to ping:"
            read address
            ping -c 5 $address
     elif [ $input = 3 ]
         then ifconfig
     else 
       echo "Invalid entry"
 fi
 echo "do you want to play again: y/n"
 read user
 done
 echo "good work"