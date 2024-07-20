import random

def determine_winner(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("===================================")
    print("Game Rules:")
    print("Rock beats Scissors")
    print("Scissors beat Paper")
    print("Paper beats Rock")
    print()
    
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    play_again = True
    
    while play_again:
        print("Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        user_input = input("Enter your choice (1/2/3): ")
        
        if user_input == '1':
            user_choice = 'rock'
        elif user_input == '2':
            user_choice = 'paper'
        elif user_input == '3':
            user_choice = 'scissors'
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        computer_choice = random.choice(choices)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")
        print()
        
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False

if __name__ == "__main__":
    main()
