import random

CHOICES = ["rock", "paper", "scissors"]

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while user_choice not in CHOICES:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(user_choice, computer_choice):
    outcomes = {
        ("rock", "scissors"): "You win!",
        ("paper", "rock"): "You win!",
        ("scissors", "paper"): "You win!",
        ("scissors", "rock"): "You lose!",
        ("rock", "paper"): "You lose!",
        ("paper", "scissors"): "You lose!",
    }
    result = outcomes.get((user_choice, computer_choice), "It's a tie!")
    return result

def play_game():
    wins, losses, ties = 0, 0, 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}\nComputer chose {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            wins += 1
        elif "lose" in result:
            losses += 1
        else:
            ties += 1

        print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

        if input("Play again? (yes/no): ").lower() != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Start the game
play_game()
