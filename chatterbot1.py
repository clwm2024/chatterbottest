import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Initialize ChatBot
chatbot = ChatBot('MyBot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///database.sqlite3')

# Train ChatBot with ChatterBot Corpus
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english')

# Custom training data
custom_data = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm good, thank you! How can I help you today?",
    "What is your name?",
    "My name is MyBot.",
    "What can you do?",
    "I can answer your questions and have a conversation with you.",
    "Bye",
    "Goodbye! Have a nice day!"
]

# Train ChatBot with Custom Data
list_trainer = ListTrainer(chatbot)
list_trainer.train(custom_data)

# Streamlit App
st.title("Offline Chatbot")
st.write("Talk to the bot:")

user_input = st.text_input("You: ", "")
if user_input:
    response = chatbot.get_response(user_input)
    st.write(f"Bot: {response}")
