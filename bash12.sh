#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated

#!/bin/bash

echo "How is your day today? (good/bad)"
read response

case $response in
    good)
        echo "That's great to hear! Keep up the good mood!"
        ;;
    bad)
        echo "I'm sorry to hear that. Hopefully, things get better soon."
        ;;
    *)
        echo "Sorry, I didn't understand your response."
        ;;
esac

# Explanation:

# echo "How is your day today? (good/bad)": Displays a prompt to ask the user about their day.
# read response: Reads the user's input and stores it in the response variable.
# case $response in: Begins the case statement and checks the value of the response variable.
# good) and bad): These are the cases the script checks for.
# echo "That's great to hear! Keep up the good mood!": If the response is "good," this message is displayed.
# echo "I'm sorry to hear that. Hopefully, things get better soon.": If the response is "bad," this message is displayed.
# *): This is the default case, which catches any input that doesn't match "good" or "bad".
# echo "Sorry, I didn't understand your response.": Displays a message for any input other than "good" or "bad".
# ;;: Ends each case in the case statement.
# esac: Ends the case statement.
# This script uses the case statement in Bash to provide different responses based on the user's input regarding how their day is going.




