import random

def get_user_choice():
    user_choice = int(input("Enter your choice (0 for rock, 1 for paper, or 2 for scissors): "))
    while user_choice not in [0,1,2]:
        print("Invalid choice. Please enter 0 for rock, 1 for paper, or 2 for scissors.")
        user_choice = int(input("Enter your choice (0 for rock, 1 for paper, or 2 for scissors): "))
    return user_choice

def get_computer_choice():
    return random.choice([0,1,2])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0,0
    elif (
        (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1)
    ):
        return "You win!", 1,0
    else:
        return "You lose!", 0,1

def print_score_box(user_score, computer_score):
    print("|----------------------------------------|")

    print("|               SCOREBOARD               |")

    print("|----------------------------------------|")
    print("|     You            |       Computer    |")
    print("|----------------------------------------|")
    print(f"|      {user_score}             |       {computer_score}           |")
    print("|----------------------------------------|")

def play_game():
    user_score = 0
    computer_score = 0

    print("Let's play Rock, Paper, Scissors!")

    for round_num in range(1, 6):
        print("\nRound: ",round_num)
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        if user_choice == 0:
            print("You chose rock." )
        elif user_choice == 1:
            print("you chose paper.") 
        else:
            print("you chose scissors. ")
        
        if computer_choice == 0:
            print("computer chose rock." )
        elif computer_choice == 1:
            print("computer chose paper.") 
        else:
            print("computer chose scissors. ")

        result, user_points, computer_points = determine_winner(user_choice, computer_choice)
        print(result)

        user_score += user_points
        computer_score += computer_points

        print_score_box(user_score, computer_score)

    print("\nGame over!")
    print("Your total score: ",user_score)
    print("Computer's total score: ",computer_score)

    if user_score == computer_score:
        print("\nMatch tie!")
    elif user_score > computer_score:
        print("\nOverall winner is You!")
    else:
        print("\nOverall winner is Computer!")

if __name__ == "__main__":
    play_game()

play_again = input("\nDo you want to play again?[y/n]")
if play_again == "y":
    play_game()
else:
    exit()
