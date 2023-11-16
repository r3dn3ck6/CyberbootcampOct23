#!/bin/bash
# Install whois on your Ubuntu

# Installing whois on Ubuntu or Debian Linux
# Open the terminal application.
# Update your .deb repos by running: $ sudo apt update.
# Apply any pending security or apps updates to your Linux box: $ sudo apt upgrade. ...
# Then install the whois client on Debian or Ubuntu Linux using the apt command or apt-get command:
# https://linuxhint.com/install-whois-ubuntu/

# The syntax is echo "$(function_name_here)" or 
# printf "Random text here %s\n" "$(function_name_here)". 
# https://www.cyberciti.biz/faq/unixlinux-bash-shell-script-function-call-in-echo-command/

# Add to your bash script a sixth option that calls a function to:

# Take a user input string. Presumably the string is a domain name such as Google.com.
# Run whois against a user input string.
# Run dig against the user input string.
# Run host against the user input string.
# Run nslookup against the user input string.
# Output the results to a single .txt file and open it with your favorite text editor.
# #What does the read command do?
# #The read command takes the user input and splits the string into fields, assigning each new word to an argument. 
# #If there are fewer variables than words, read stores the remaining terms into the final variable. 
# #Specifying the argument names is optional.

# For this challenge you must use at least one variable and one function.

# sudo apt update
# sudo apt-upgrade
# sudo apt-whois
# ssudo apt-get install whois
# sudo dig google.com
# sudo host google.com
# sudo nslookup google.com
# sudo history

#blake fritz's code with class-->
echo "Enter a website"
read website

function gather_info () {
    whois $website >> whois.txt
    echo "----" >> whois.txt
    dig $website >> whois.txt
    echo "----" >> whois.txt
    host $website >> whois.txt
    echo "----" >> whois.txt
    nslookup $website >> whois.txt
    echo "----" >> whois.txt
}

gather_info
cat whois.txt


#!/bin/bash

function perform_whois() {
    read -p "#website:" domain
    echo "Running whois against $domain..."
    whois "$domain" >> output.txt  # Append output to the file
}

# Function to perform dig
functions perform_dig() {
    read -p "#website:"  domain
    echo "Running dig against $domain..."
    dig $domain >> output.txt
}

# Function to perform host
perform_host() {
    read -p "#website:"  domain
    echo "Running host against $domain..."
    host $domain >> output.txt
}

# Function to perform nslookup
perform_nslookup() {
    read -p "#website:"  domain
    echo "Running nslookup against $domain..."
    nslookup $domain >> output.txt
}

# Function to handle the sixth option
option_six() {
    perform_whois
    perform_dig
    perform_host
    perform_nslookup
    echo "Results saved to output.txt"
    $EDITOR output.txt  # Opens the file with your favorite text editor, change $EDITOR to your preferred editor command
}

# Main menu options
echo "Select an option:"
echo "1. Perform whois"
echo "2. Perform dig"
echo "3. Perform host"
echo "4. Perform nslookup"
echo "5. Exit"
echo "6. Perform all and open results"

read option

case $option in
    1) perform_whois;;
    2) perform_dig;;
    3) perform_host;;
    4) perform_nslookup;;
    5) exit;;
    6) option_six;;
    *) echo "Invalid option";;
esac
