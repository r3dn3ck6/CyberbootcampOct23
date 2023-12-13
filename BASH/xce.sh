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
echo "good work"c