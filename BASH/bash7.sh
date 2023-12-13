#!/bin/bash
# Take care to only perform this operation in user-created directories. Changing permissions in system files/directories is not advised, as this can cause malfunctions in the OS.

# Create a new bash script that performs the following:

# Prompts user for input directory path.
# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
# Navigates to the directory input by the user and changes all files inside it to the input setting.
# Prints to the screen the directory contents and the new permissions settings of everything in the directory.

echo "enter a file"
ls
read file
echo "enter permission number 777 or 770"
read Num
chmod $Num $file
echo "You granted permsion to $file"
ls -l $file

# The syntax of the given script is correct. It is a bash script that performs the following steps:

# Prints the message "enter a file" using the echo command.
# Lists the files in the current directory using the ls command.
# Reads the name of a file inputted by the user and assigns it to the variable "file" using the read command.
# Prints the message "enter permission number 777 or 770" using the echo command.
# Reads a permission number inputted by the user and assigns it to the variable "Num" using the read command.
# Changes the permission of the file specified by the user using the chmod command and the permission number stored in the variable "Num".
# Prints the message "You granted permission to [file name]" using the echo command.
# Lists the detailed information of the file specified by the user using the ls -l command.
# After running this script, it will prompt the user to enter a file name, permission number, and display the granted permission and the detailed information of the file.








# This script will prompt the user for a directory path and permissions number. 
# It will then navigate to the specified directory, change the permissions of all files and directories inside it to the provided permissions number, and finally display
# the contents of the directory along with their new permission settings.

# Save this script to a file (e.g., change_permissions.sh), make it executable (chmod +x change_permissions.sh), 
# and then run it in your terminal by typing ./change_permissions.sh.

# This script will prompt the user for a directory path and permissions number. 
# It will then navigate to the specified directory, change the permissions of all files and directories inside it to the provided 
# permissions number, and finally display the contents of the directory along with their new permission settings.

# Save this script to a file (e.g., change_permissions.sh), make it executable (chmod +x change_permissions.sh), 
# and then run it in your terminal by typing ./change_permissions.sh.


