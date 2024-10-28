import random

def play_game():
    print("Welcome to the number guessing game!")
    play = input("Do you want to play the number guessing game? (yes/no): ").lower()

    if play != 'yes':
        print("Maybe next time!")
        return

    secret_number = random.randint(1, 10)
    guess = None

    while guess != secret_number:
        guess = int(input("Guess a number between 1 and 10: "))
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    print("Congratulations! You've guessed the number!")
    print("Thanks for playing!")

play_game()