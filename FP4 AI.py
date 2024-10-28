# Define a dictionary with trivia questions and answers
trivia_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the smallest prime number?": "2",
    "In what year did the Titanic sink?": "1912"
}

# Function to run the trivia game
def trivia_game():
    for question, correct_answer in trivia_questions.items():
        # Display the question to the user
        print(question)
        
        # Prompt the user for their answer
        user_answer = input("Your answer: ").strip()
        
        # Check if the user's answer is correct and provide feedback
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")
    
    print("Thanks for playing!")

# Start the trivia game
trivia_game()