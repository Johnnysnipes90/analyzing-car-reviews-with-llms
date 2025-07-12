import streamlit as st
from transformers import pipeline
import pandas as pd

# --- Load Pipelines --- #
sentiment_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
translator_en_es = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
translator_es_en = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
qa_pipeline = pipeline("question-answering", model="deepset/minilm-uncased-squad2")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# --- App Title --- #
st.set_page_config(page_title="Car-Ing AI Assistant", page_icon="🚗")
st.title("Car-ing AI Assistant 🚗")
st.markdown("Use this AI assistant to analyze car reviews, translate content, summarize feedback, or ask questions!")

# --- Sidebar --- #
st.sidebar.title("Choose a Task")
task = st.sidebar.radio("Select a task:", ["Sentiment Analysis", "Translation", "Q&A", "Summarization", "Batch CSV Analysis"])

# --- Sentiment Analysis --- #
if task == "Sentiment Analysis":
    user_input = st.text_area("Enter a car review:")
    if st.button("Analyze Sentiment") and user_input:
        result = sentiment_pipeline(user_input)[0]
        st.write(f"**Sentiment:** {result['label']} ({round(result['score'] * 100, 2)}%)")

# --- Translation --- #
el = st.empty()
if task == "Translation":
    direction = st.radio("Translation Direction", ["English to Spanish", "Spanish to English"])
    user_input = st.text_area("Enter text to translate:")
    if st.button("Translate") and user_input:
        if direction == "English to Spanish":
            result = translator_en_es(user_input)[0]['translation_text']
        else:
            result = translator_es_en(user_input)[0]['translation_text']
        st.write(f"**Translated Text:** {result}")

# --- Q&A --- #
if task == "Q&A":
    context = st.text_area("Enter a paragraph from a car review:")
    question = st.text_input("Ask a question about the review:")
    if st.button("Get Answer") and context and question:
        result = qa_pipeline(question=question, context=context)
        st.write(f"**Answer:** {result['answer']}")

# --- Summarization --- #
if task == "Summarization":
    long_text = st.text_area("Paste a long car review to summarize:")
    if st.button("Summarize") and long_text:
        summary = summarizer(long_text, max_length=55, min_length=45, do_sample=False)[0]['summary_text']
        st.write(f"**Summary:** {summary}")

# --- Batch CSV Upload & Analysis --- #
if task == "Batch CSV Analysis":
    uploaded_file = st.file_uploader("Upload a CSV with a 'review' column:", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if 'review' not in df.columns:
            st.error("CSV must contain a 'review' column")
        else:
            if st.button("Run Sentiment Analysis on Reviews"):
                with st.spinner("Analyzing..."):
                    results = sentiment_pipeline(df['review'].tolist())
                    df['sentiment'] = [r['label'] for r in results]
                    st.success("Done!")
                    st.dataframe(df)
                    st.download_button("Download Results", df.to_csv(index=False), file_name="sentiment_results.csv")
