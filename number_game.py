import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts_left = 7
    attempts_made = 0
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {attempts_left} attempts.")
    
    while attempts_left > 0:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts_made += 1
            attempts_left -= 1
            
            # Check the guess
            if guess < secret_number:
                print(f"Too low! You have {attempts_left} attempts left.")
            elif guess > secret_number:
                print(f"Too high! You have {attempts_left} attempts left.")
            else:
                print(f"Congratulations! You guessed the number in {attempts_made} attempts!")
                return
                
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Game over! The number was {secret_number}.")

if __name__ == "__main__":
    play_game()
    
    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
        play_game()