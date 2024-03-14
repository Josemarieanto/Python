
import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!", 1
    else:
        return "You lose!", 0

def play_game():
    user_score = 0
    computer_score = 0

    print("Let's play Rock, Paper, Scissors!")

    for _ in range(5):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")

        result, points = determine_winner(user_choice, computer_choice)
        print(result)

        user_score += points
        computer_score += points

    print("\nGame over!")
    print(f"Your final score: {user_score}")
    print(f"Computer's final score: {computer_score}")

if __name__ == "__main__":
    play_game()
