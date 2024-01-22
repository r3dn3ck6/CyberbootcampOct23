
# In the game of Rock, Paper, Scissors, there are three possible moves for both the user and the computer: Rock, Paper, and Scissors. This leads to a total of 
# 3×3=9 possible combinations when the user plays against the computer:

# User: Rock,  Computer: Rock
# User: Paper, Computer: Paper
# User: Scissors, Computer: Scissors

# User: Rock, Computer: Paper
# User: Rock, Computer: Scissors
# User: Paper, Computer: Rock
# User: Paper, Computer: Scissors
# User: Scissors, Computer: Rock
# User: Scissors, Computer: Paper

# Each combination results in a different outcome for the game, and each move has a specific interaction with the other moves: 
# Rock crushes Scissors, Scissors cuts Paper, and Paper covers Rock.

import random

while True:
    options = ["Rock", "Paper", "Scissors"]

    user_choice = input("Choose Rock, Paper, or Scissors: ")

    computer_choice = random.choice(options)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("Computer wins!")

    # While Loop
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing. Goodbye!")
        break
