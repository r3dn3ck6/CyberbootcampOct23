# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time

#Start code below this line:

def count_mississippi():
    for count_down range(5, 0, -1) # is the variable that takes on the values from the range(5, 0, -1) sequence. The range(5, 0, -1) generates a sequence of numbers starting from 5 (inclusive), down to 1 (exclusive), with a step of -1. So, during each iteration of the loop, i takes on values 5, 4, 3, 2, and 1, respectively.
    print(count_down) 
    time.sleep(1) #time.sleep(1) is the loop to count down to 5 to 1, each number pausing for 1 sec between.
    
    print("Ready or not, here I come!")




    def main():
        count_mississippi()
    main()


