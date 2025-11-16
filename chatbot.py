import sys
from datetime import datetime
import random # Import for jokes and random responses

# Define a dictionary of keywords/patterns and their responses.
# Keywords are in lowercase to simplify matching.
# Responses can be static strings or functions (using lambda) for dynamic content.
RESPONSE_PATTERNS = {
    # Greetings
    ("hello", "hi", "hey"): "Hi there! I'm an enhanced rule-based bot.",

    # State/Feeling
    ("how are you", "how are you doing", "what's up"): "I'm fine, thanks for asking! I'm just here to chat.",
    
    # Identity
    ("name", "who are you"): "I don't have a name, but you can call me Bot.",
    
    # Gratitude
    ("thank you", "thanks"): "You're welcome! How else can I assist?",

    # Date/Time (Dynamic Response)
    ("time", "date", "today"): lambda: f"The current date and time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.",

    # Weather (Simple Rule) - NEW
    ("weather", "is it raining", "sunshine"): "I can't check the real weather, but let's say it's always a good day to chat!",

    # Simple Joke (Random selection) - NEW
    ("joke", "tell me something funny"): lambda: random.choice([
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
        "What do you call a fish with no eyes? Fsh!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]),

    # Basic Facts (Knowledge) - NEW
    ("capital of france", "paris"): "The capital of France is Paris. It's famous for the Eiffel Tower.",
    ("python language", "what is python"): "Python is a popular, high-level programming language used for web development, data analysis, and more.",
    
    # Exit
    ("bye", "goodbye"): "Goodbye!"
}


def get_response(user_input):
    """
    Determines the chatbot's response based on dictionary-based pattern matching.

    Args:
        user_input (str): The cleaned text entered by the user.

    Returns:
        str: The corresponding reply from the chatbot.
    """
    processed_input = user_input.lower().strip()

    # Iterate through patterns to find a match
    for keywords, response in RESPONSE_PATTERNS.items():
        # Ensure keywords is iterable
        if isinstance(keywords, str):
            keywords = (keywords,)

        for keyword in keywords:
            if keyword in processed_input:
                # If the response is a function (like for dynamic date/time or jokes), call it.
                if callable(response):
                    return response()
                # Otherwise, return the static string response.
                return response
    
    # Default response for anything not recognized
    return "I'm not sure how to respond to that. Try asking about the 'time', 'weather', or 'joke'."


def chat_loop():
    """
    The main loop that handles user interaction and continuous chatting.
    """
    print("--- Welcome to the Enhanced Rule-Based Chatbot ---")
    print("Try asking about the 'time', 'weather', or a 'joke'!")
    print("Type 'bye' or 'exit' to end the conversation.\n")
    
    while True:
        try:
            # Get user input
            user_input = input("You: ")
            
            # Check for immediate exit commands
            if user_input.lower().strip() in ["exit", "quit"]:
                print("Bot: Goodbye! Have a great day!")
                break
            
            # Get the bot's response
            response = get_response(user_input)
            
            # Print the response
            print(f"Bot: {response}")

            # Check for the 'Goodbye!' reply from the response patterns to break the loop gracefully
            if response == "Goodbye!":
                break

        except EOFError:
            # Handles cases where input stream ends (e.g., Ctrl+D)
            print("\nBot: Goodbye!")
            break
        except Exception as e:
            # General error handling
            print(f"An unexpected error occurred: {e}")
            break


if __name__ == "__main__":
    chat_loop()
