# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# You will need to use a for loop to write this:


#Write your code below this row 👇

for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
    elif fizzbuzz % 3 == 0:
        print("fizz")
    elif fizzbuzz % 5 == 0:
        print("buzz")
    print(fizzbuzz) 

# Explanation:

# for fizzbuzz in range(101): sets up a loop that iterates through numbers from 0 to 100 (inclusive). fizzbuzz takes each value from 0 to 100 in each iteration.
## The % operator in Python is called the modulo operator. It calculates the remainder of the division between two numbers.
# The following if and elif statements inside the loop check certain conditions for each fizzbuzz value:
# if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0: checks if the number is divisible by both 3 and 5 (i.e., it's a multiple of both 3 and 5). If true, it prints "fizzbuzz".
# elif fizzbuzz % 3 == 0: checks if the number is divisible by 3 (i.e., it's a multiple of 3). If true, it prints "fizz".
# elif fizzbuzz % 5 == 0: checks if the number is divisible by 5 (i.e., it's a multiple of 5). If true, it prints "buzz".
# print(fizzbuzz) prints the current value of fizzbuzz in each iteration of the loop, regardless of whether any of the conditions above are met.
# In summary, as the loop iterates through numbers from 0 to 100, it prints:

# "fizzbuzz" for numbers divisible by both 3 and 5.
# "fizz" for numbers divisible only by 3.
# "buzz" for numbers divisible only by 5.
# The actual number if none of the above conditions are met.