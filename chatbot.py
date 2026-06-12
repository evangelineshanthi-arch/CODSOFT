import random
from datetime import datetime

def chatbot_response(user_input):
    text = user_input.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return random.choice(["Hello! How can I help you today?", "Hi there!", "Hey! What's up?"])

    elif "how are you" in text:
        return "I'm doing great, thanks for asking! How about you?"

    elif "your name" in text:
        return "I'm ChatBuddy, your friendly rule-based chatbot."

    elif "time" in text:
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."

    elif "date" in text:
        today = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {today}."
    elif "ai" in text:
        return "AI stands for Artificial Intelligence."

    elif "help" in text:
        return "I can chat about greetings, my name, time, date, jokes, and more. Try asking!"

    elif "joke" in text:
        jokes = [
            "Why don't programmers like nature? It has too many bugs.",
            "Why do Java developers wear glasses? Because they don't C#.",
            "I would tell you a UDP joke, but you might not get it."
        ]
        return random.choice(jokes)

    elif any(word in text for word in ["thanks", "thank you"]):
        return "You're welcome!"

    elif any(word in text for word in ["bye", "exit", "quit"]):
        return "Goodbye! Have a great day!"

    else:
        return "I'm sorry, I didn't understand that. Could you rephrase?"


def main():
    print("ChatBuddy: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("ChatBuddy:", response)
        if any(word in user_input.lower() for word in ["bye", "exit", "quit"]):
            break


if __name__ == "__main__":
    main()