import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ")
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return f"You win! {user.capitalize()} beats {computer}."
    else:
        return f"You lose! {computer.capitalize()} beats {user}."

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    result = determine_winner(user_choice.lower(), computer_choice)  # Lowercasing user_choice for consistency
    print(result)

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':  # Lowercasing play_again for consistency
        print("Thanks for playing. Goodbye!")
        break
