from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")

def translate_text(text):
    result = translator(text)[0]['translation_text']
    return result