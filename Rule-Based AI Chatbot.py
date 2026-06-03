from datetime import datetime
print("-------------------------------------")
print("Welcome to Rule-Based AI Chatbot.")
print("-------------------------------------")
print("Type 'bye' if you want to end chat.\n")


name=input("what is your name:")
print(f"Bot: Hello {name}! how can i help you.\n")

while True:

    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking")

    elif user == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user == "Who develop you" or user == "who made you":
        print("Bot: I am developed by Sarth Patel.")
    
    elif user == "what can you do":
        print("Bot: I can answer simple questions and chat with you.")

    elif user == "tell me a joke":
        print("Bot: Why did the computer get cold? Because it forgot to close Windows!")

    elif user == "i am sad":
        print("Bot: Don't worry, everything will be okay.")

    elif user == "Tell me current time." or user == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    elif user == "Tell me current date." or user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I can't understand that.")