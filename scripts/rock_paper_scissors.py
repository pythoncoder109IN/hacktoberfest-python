import random

def get_user_choice():
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1/2/3): ").strip()
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice, try again!")
        return get_user_choice()
    
    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    return choices[choice]

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        return "🎉 You win!"
    else:
        return "😢 Computer wins!"

def play_game():
    print("===== Rock Paper Scissors Game =====")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\n🧍 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")
        print(f"\nResult: {decide_winner(user_choice, computer_choice)}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\n👋 Thanks for playing! Goodbye!\n")
            break

if __name__ == "__main__":
    play_game()
