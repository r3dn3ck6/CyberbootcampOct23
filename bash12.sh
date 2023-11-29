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

# case Statement Syntax #
# The Bash case statement takes the following form:

# case EXPRESSION in

#   PATTERN_1)
#     STATEMENTS
#     ;;

#   PATTERN_2)
#     STATEMENTS
#     ;;

#   PATTERN_N)
#     STATEMENTS
#     ;;

#   *)
#     STATEMENTS
#     ;;
# esac


# Each case statement starts with the case keyword, followed by the case expression and the in keyword. The statement ends with the esac keyword.
# You can use multiple patterns separated by the | operator. The ) operator terminates a pattern list.
# A pattern can have special characters .
# A pattern and its associated commands are known as a clause.
# Each clause must be terminated with ;;.
# The commands corresponding to the first pattern that matches the expression are executed.
# It is a common practice to use the wildcard asterisk symbol (*) as a final pattern to define the default case. This pattern will always match.
# If no pattern is matched, the return status is zero. Otherwise, the return status is the exit status of the executed commands.
# Case Statement Example
# Here is an example using the case statement in a bash script that will print the official language of a given country:

# https://linuxize.com/post/bash-case-statement/


# To make your Bash script or code case-insensitive, you can use the shopt command along with the nocaseglob option. This option affects pattern matching (e.g., using * or ? for file matching).

# Here's an example of how you can set the nocaseglob option to make your Bash code case-insensitive:

# bash
# Copy code
# shopt -s nocaseglob

# # Your case-insensitive code here

# shopt -u nocaseglob  # Disable case insensitivity if needed further in the script
# This setting will make commands like ls, rm, or any other command using file globbing patterns (*, ?, etc.) to ignore case when matching files.

# However, please note that this method only affects globbing (pattern matching) in Bash and doesn't necessarily make all comparisons in your script case-insensitive. If you want to perform case-insensitive string comparisons, you can use the nocasematch option with the shopt command:

# bash
# Copy code
# shopt -s nocasematch

# # Your case-insensitive code here

# shopt -u nocasematch  # Disable case insensitivity if needed further in the script
# This setting will enable case-insensitive matching for [[ ]] conditional expressions in Bash. For example:

# bash
# Copy code
# if [[ $var == "Hello" ]]; then
#     echo "Case-insensitive comparison succeeded"
# fi
# Remember to turn off these settings (nocaseglob and nocasematch) if you want to revert to case sensitivity in different parts of your script or for specific comparisons.