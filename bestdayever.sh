#  The Bash Butler Script
# bestdayever.sh
# $ bash -c "source hello.sh; hello" Hello, World! $ . hello.sh; hello Hello, World!
# Script = "bestdayever.sh"
# Have your script "greet" you with these 3 messages
# 1 Good morning Josh!!
# 1 sleep
# Your're looking good today Josh!!
# 1 Sleep
# You have the best beard I've ever seen Josh!!
# Make my script executable

# !/bin/bash
echo "Good Morning Josh!!"

Sleep 1

echc "You're looking good today Josh!!"

Sleep 1

echo "You have the best beard I've ever seen Josh!!"
getrichquick.sh
chmod +x bestdayever.sh

Name =$1
compliment=$2

user=$(whoami)
date=$(date)
whereami=$(pwd)

echo "What is your name"
sleep 1
echo Good Morning $name
sleep 1
echo "You are the best $compliment" I've ever seen $name!!"
Sleep 2
echo "You are currently logged in as $user and you are in the directory $whereami. Also today is: $date"