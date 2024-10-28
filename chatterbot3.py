import fitz  # PyMuPDF
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import streamlit as st

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

pdf_path = "path_to_your_german_pdf_file.pdf"
pdf_text = extract_text_from_pdf(pdf_path)

# Assume each line in the PDF is a Q&A pair separated by a question mark
qa_pairs = [line.split("?") for line in pdf_text.split("\n") if "?" in line]
training_data = []
for pair in qa_pairs:
    if len(pair) == 2:
        question, answer = pair
        training_data.append(question.strip())
        training_data.append(answer.strip())

# Initialize ChatBot with German language support
chatbot = ChatBot('MeinBot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///german_database.sqlite3')

# Train ChatBot with ChatterBot German Corpus
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.german')

# Train ChatBot with custom German data
trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Streamlit App
st.title("Offline Chatbot auf Deutsch")
st.write("Sprich mit dem Bot:")

user_input = st.text_input("Du: ", "")
if user_input:
    response = chatbot.get_response(user_input)
    st.write(f"Bot: {response}")
