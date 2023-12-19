# Objectives

# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# Use the python os function to print the following commands below.  These are bash commands and we are going to run them through a python script.
# Add description printed to the terminal of what is about to run



# whoami
# ip a
# lshw -short
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Instead of os.system() function, utilize the subprocess module instead. Refer to python.org for how this can be achieved.



# This will not run on windows needs to be mac or linux due to os being bash

# import subprocess
# import osins


# Define the commands
 #   "whoami", #displays a username associated wwith the effective userID
  #  "ip a", #his command is used to show or manipulate routing, devices, and tunnels. 
   # "lshw -short" #a small tool to provide detailed information on the hardware configuration of the machine.


################################################################################################################################################################


##This script will execute the specified bash commands (whoami, ip a, and lshw -short) using the os.system() function in Python. 
##It will print a description before running each command and then execute it in the terminal.


import os

# Define the commands
commands = [
    "whoami",
    "ip a",
    "lshw -short"
]

# Iterate through commands
for command in commands:
    print(f"Running command: {command}")
    os.system(command)
    print("\n")





##However, as mentioned in your stretch goals, using the subprocess module is a more
##recommended and versatile way to execute shell commands in Python. 
##Here's an example using subprocess:


import subprocess

# Define the commands
commands = [
    "whoami",
    "ip a",
    "lshw -short"
]

# Iterate through commands
for command in commands:
    print(f"Running command: {command}")
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if output:
        print(output.decode())
    if error:
        print(error.decode())
    print("\n")


    ##############################################################################################################################################################


import subprocess


##This code snippet imports the subprocess module and executes the ls command (listing files and directories) on Unix-like systems. 
##This is a basic demonstration of using the subprocess.run() function to execute a command. 
##You can replace ls with any command that is valid for your system.


# Run a simple command (for example, 'ls' on Unix-like systems)
subprocess.run(["ls"])

###################################################################################################################################################################


##The os module in Python is used for interacting with the operating system. In this example, it retrieves the current working directory using os.getcwd() 
##and lists files in the current directory using os.listdir(). 
##You can perform various other operations on the file system using the functions available in the os module.

import os

# Example usage of the os module
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Listing files in the current directory
files_in_directory = os.listdir()
print(f"Files in current directory: {files_in_directory}")

#########################################

#Classmates Example:

n="ls"
a="whoami"
b="ifconfig"

subprocess.run(n, '-1')
print (print this ls)
Print()
    subprocess.run(a)
print(print this whoami)
print()
    subprocess.run(b)
print(print this ifconfig)
print()
###############################################################################################################################################################

#Chloe's Example:

import subprocess
import os
computer = "whoami"
network = "ifconfig"
lsa = "lshw -short"
mac = "sysctl -a"
print("Who am I")
os.system(computer)
print("Network configurations")
subprocess.run(network)
print("Hardware")
os.system(mac)
#os.system(lsa)

