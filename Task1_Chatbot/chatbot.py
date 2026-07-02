print("🤖 Welcome to CodSoft Chatbot!")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")
    elif user == "hi":
        print("Bot: Hello! Nice to meet you.")
    elif user == "how are you":
        print("Bot: I am fine. Thank you!")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand.")