
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

def get_user_choice():
    return input("Choose Rock, Paper, or Scissors: ")

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or
         (user_choice == "Paper" and computer_choice == "Rock") or
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    wins, losses = 0, 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "win" in result:
            wins += 1
        elif "loss" in result:
            losses += 1
        
        print(f"Wins: {wins}, Losses: {losses}")

        # While Loop
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing. Goodbye!")
            break

# Run the game
play_game()
