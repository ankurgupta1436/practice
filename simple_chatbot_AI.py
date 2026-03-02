# Simple AI Chatbot

print("🤖 Simple Chatbot (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hi there!")
    elif "how are you" in user:
        print("Bot: I'm just code, but I'm doing great!")
    elif "your name" in user:
        print("Bot: I'm a simple Python chatbot.")
    elif "bye" in user:
        print("Bot: Goodbye! 👋")
        break
    else:
        print("Bot: I don't understand that yet.")