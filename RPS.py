import random
def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    return user_choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))
# Play the game
play_game()
