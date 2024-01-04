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


#The line if __name__ == "__main__": in Python is a common idiom used to check whether the current script is being run as the main program
#    or if it's being imported as a module into another script.
#When a Python file is executed as the main program (i.e., directly invoked from the command line or run by an IDE), 
    #Python sets the special variable __name__ to "__main__". On the other hand, when a Python file is imported as a module into another script,
#    the __name__ variable is set to the name of that module.
#So, the line if __name__ == "__main__": checks if the current script is the main program being executed. If it is, it executes the code block that follows. This allows you to define some code that should only run if the file is executed directly, not when it's imported as a module.
#For example:

#python Code:
# def main():
    # Your main code here

# if __name__ == "__main__":
#    main()  # Execute main function if this script is run as the main program

#In this case, the main() function will be called only when the Python script is run directly (as the main program). 
#   If the script is imported as a module into another script, the main() function won't be executed automatically. 
#   This separation allows for better organization and reusability of code.







