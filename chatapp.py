import streamlit as st
from docproc import DocumentProcessor

st.title("Offline PDF Chatbot")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    pdf_path = f"./temp_{uploaded_file.name}"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    doc_processor = DocumentProcessor(pdf_path)

    st.header("PDF Content Summary")
    if st.button("Summarize PDF"):
        summary = doc_processor.summarize_text()
        st.write(summary)

    st.header("Ask a Question")
    question = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        answer = doc_processor.answer_question(question)
        st.write(answer)
