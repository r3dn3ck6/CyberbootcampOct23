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
#############################################################################################################################



# Magician's secret number
secret_number = 7

# Ask the user to enter an integer number
print("Guess the magician's number! Enter an integer:")

# Using a while loop to repeatedly ask the user for input
while True:
    user_number = int(input())  # Get user input and convert it to an integer
    
    # Check whether the user's number matches the magician's number
    if user_number == secret_number:
        print("Well done, muggle! You are free now.")
        break  # Break out of the loop when the number matches
        
    # If the numbers don't match, prompt the user to try again
    print("Ha ha! You're stuck in my loop! Try again. Enter another number:")

