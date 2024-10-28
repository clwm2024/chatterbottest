import fitz  # PyMuPDF
from transformers import pipeline

class DocumentProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = self.extract_text_from_pdf()

    def extract_text_from_pdf(self):
        doc = fitz.open(self.pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    def summarize_text(self):
        summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")
        return summarizer(self.text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

    def answer_question(self, question):
        qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")
        return qa_model(question=question, context=self.text)['answer']
