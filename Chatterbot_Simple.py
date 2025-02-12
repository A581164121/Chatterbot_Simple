from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot("SmartBot")

# Train the chatbot with English corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

print("Chatbot is ready! Type something to start chatting.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot.get_response(user_input)
    print("Chatbot:", response)