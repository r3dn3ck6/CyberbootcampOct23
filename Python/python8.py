# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"


import time

# Start code below this line:

def count_mississippi():
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1) # time.sleep(1) pauses the loop for 1 second between each number.

    print("Ready or not, here I come!")

def main():
    count_mississippi()

if __name__ == "__main__":
    main()
