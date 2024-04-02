import random
def user( ):
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
def computer( ):
    return random.choice(['rock', 'paper', 'scissors'])
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
def play_game( ):
    print("\nWELCOME TO ROCK, PAPER, SCISSORS!")
    while True:
        user_choice = user( )
        computer_choice = computer( )
        print(f"You chose {user_choice}.\n Computer chose {computer_choice}.")
        print(winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != 'yes':
            print("THANKS FOR PLAYING!")
            break
if __name__ == "__main__":
    play_game()
