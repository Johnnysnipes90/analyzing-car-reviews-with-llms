from transformers import pipeline

sentiment_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_sentiment(text):
    result = sentiment_pipeline(text)[0]['label']
    return result