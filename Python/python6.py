# Scenario
# A junior magician has picked a secret number. He has hidden it in a variable named secret_number.
#  He wants everyone who runs his program to play the Guess the secret number game, 
#  and guess what number he has picked for them. 
#  Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

# Your task is to help the magician complete the code in the editor in such a way so that the code:
# will ask the user to enter an integer number;
# will use a while loop;
# will check whether the number entered by the user is the same as the number picked by the magician. 
# If the number chosen by the user is different than the magician's secret number, the user should see 
# the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. 
# If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, 
# and the magician should say the following words: "Well done, muggle! You are free now."
# The magician is counting on you! Don't disappoint him.

# The magician's secret number
secret_number = 7  # You can change this number to any desired value

# Asking the user to guess the number
while True:
    user_guess = int(input("Guess the secret number: "))  # Asking for user input as an integer
    
    # Checking if the user's guess matches the secret number
    if user_guess == secret_number:
        print(f"Well done, muggle! You guessed the secret number: {secret_number}. You are free now.")
        break  # Exiting the loop if the guess is correct
    else:
        print("Ha ha! You're stuck in my loop!")  # Prompting user to try again

##################################################################################################################################
import random

R = random.randint(1, 100)

while True:
    N = int(input("Guess the secret number: "))

    if N == R:
        print("Well done, muggle! You are free now")
        break
    else:
        print("Ha ha! You're stuck in my loop!")



        
