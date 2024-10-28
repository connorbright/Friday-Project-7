import random

def generate_powerball_numbers():
    print("Welcome to the PowerBall number generator!")
    
    # Generate the first five numbers (white balls)
    white_ball_1 = random.randint(1, 69)
    white_ball_2 = random.randint(1, 69)
    white_ball_3 = random.randint(1, 69)
    white_ball_4 = random.randint(1, 69)
    white_ball_5 = random.randint(1, 69)
    
    # Generate the PowerBall number (red ball)
    red_ball = random.randint(1, 26)
    
    # Print the generated numbers with the required spaces
    print(f"{white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5}   {red_ball}")
    
    print("Good luck, and goodbye!")

# Call the function to generate and print the numbers
generate_powerball_numbers()