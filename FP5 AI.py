# Define functions to change text color using ANSI escape codes
def red_text(text):
    return f"\033[91m{text}\033[0m"

def blue_text(text):
    return f"\033[94m{text}\033[0m"

def green_text(text):
    return f"\033[92m{text}\033[0m"

def yellow_text(text):
    return f"\033[93m{text}\033[0m"

def brown_text(text):
    return f"\033[33m{text}\033[0m"

# Main program logic
def main():
    # Test each function by calling them and printing the text in the corresponding color
    print(red_text("This is red text"))
    print(blue_text("This is blue text"))
    print(green_text("This is green text"))
    print(yellow_text("This is yellow text"))
    print(brown_text("This is brown text"))

    # User input prompt
    color = input("Choose a color (red, blue, green, yellow, brown): ").strip().lower()
    user_text = input("Enter the text you want to display: ")

    # Dictionary to map color choices to functions
    color_functions = {
        "red": red_text,
        "blue": blue_text,
        "green": green_text,
        "yellow": yellow_text,
        "brown": brown_text
    }

    # Get the appropriate function based on user's color choice and display the formatted text
    if color in color_functions:
        print(color_functions[color](user_text))
    else:
        print("Invalid color choice!")

# Run the main program
main()