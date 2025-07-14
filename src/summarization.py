from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    result = summarizer(text, max_length=60, min_length=30, do_sample=False)[0]['summary_text']
    return result
