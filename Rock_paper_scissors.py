import random

def get_user_choice():
    choice = input("Enter Rock, Paper, or Scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice.")
        choice = input("Enter Rock, Paper, or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("=== Rock, Paper, Scissors Game ===")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play()
