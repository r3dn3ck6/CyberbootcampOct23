#!/bin/bash
# https://ss64.com/bash/
# https://blog.ycrash.io/2021/06/28/ping-unix-linux-command-beginners-introduction-with-examples/
# https://www.neuralnine.com/code-a-ddos-script-in-python/

#Lets create a script that would work like a DDOS (Distributed Denial of Service) attack by using a while loop

#In this script we want to contiune to ping our personal pc in a infitine while loop
#Somebody that had a control of a bot net could set up this script on thousands of computer and ping sites till they are overloaded and crash


# IP = ("192.168.1..1")

for IP in "192.168.1.1"
do
  echo $IP
  ping -c 1 $IP
  sleep 5
done

# Anthonys code
x=1
while [$x =1]
do 
    ping 192.168.10.1
    echo "do you wnat to run again?"
    read $x
done



# This bash code is a simple loop that pings an IP address. Let's break down each element of the code:

# do: This keyword starts the loop execution. It signifies the beginning of the loop block.

# echo $IP: This line outputs the value of the variable IP. It prints the IP address being processed by the loop.

# ping -c 1 $IP: This line pings the IP address using the ping command with the -c 1 option. It sends a single ICMP echo request packet to the IP address.

# done: This keyword marks the end of the loop block. It signifies the completion of the loop.

# Overall, this code iterates over a specified IP address (192.168.10.1 in this case) and prints the IP address before pinging it.

/***********************************************************************************************************************************************/


# IP address of our personal computer
ip_address="192.168.10.1"

# Infinite loop
while true
do
  # Ping our personal computer with 1 packet and a timeout of 1 second
  ping -c 1 -W 1 $ip_address > /dev/null
  
  # Check the return code of the ping command
  if [ $? -eq 0 ]; then
    echo "Ping to $ip_address successful."
  else
    echo "Ping to $ip_address unsuccessful."
  fi
  
  # Sleep for 1 second before the next iteration
  sleep 1
done

# This script will continuously ping the specified IP address with 1 packet and a timeout of 1 second. 
# It then checks the return code of the ping command to determine if the ping was successful or not. 
# A success message is printed if the return code is 0, indicating a successful ping, and an unsuccessful message is printed otherwise. 
# The script will repeat this process indefinitely with a 1-second delay between each iteration.