import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.sentiment import classify_sentiment
from src.translation import translate_text
from src.summarization import summarize_text
from src.question_answering import answer_question

# ---------- Page Config ----------
st.set_page_config(
    page_title="Car Review AI Assistant",
    page_icon="🚗",
    layout="centered"
)

# ---------- Custom Styling ----------
st.markdown("""
    <style>
        html, body {
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #f9f9f9;
            padding: 1rem;
            border-radius: 0.5rem;
        }
        .stButton>button {
            background-color: #0066cc;
            color: white;
            font-weight: bold;
            padding: 0.6em 1em;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #004c99;
        }
        .css-1cpxqw2 {
            padding: 1rem 2rem;
        }
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown("<h1 style='text-align: center; color: #333;'>🚗 Car Review AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #888;'>Powered by Hugging Face Transformers & Streamlit</h5>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; color: #555; font-size: 15px;'>
This assistant uses <strong>state-of-the-art LLMs</strong> to help classify, translate, summarize, and answer questions from car reviews.
</p>
""", unsafe_allow_html=True)

st.write("---")


# ---------- Sidebar ----------
st.sidebar.image("images/car.jpeg", use_container_width=True)
st.sidebar.header("🛠️ Select Task")
task = st.sidebar.radio("What do you want to do?", [
    "Sentiment Analysis",
    "Translation (EN to ES)",
    "Question Answering",
    "Summarization"
])

# ---------- Input Area ----------
st.markdown("### ✍️ Enter Review Text or Context")
text_input = st.text_area(
    label="Text Input",
    height=200,
    placeholder="Type your car review or context here...",
    label_visibility="collapsed"
)

# ---------- Task Blocks ----------
if task == "Sentiment Analysis":
    st.markdown("#### 🔍 Sentiment Classification")
    if st.button("Classify Sentiment"):
        if text_input.strip():
            label = classify_sentiment(text_input)
            st.success(f"Predicted Sentiment: **{label}**")
        else:
            st.warning("Please enter some review text.")

elif task == "Translation (EN to ES)":
    st.markdown("#### 🌐 English to Spanish Translation")
    if st.button("Translate"):
        if text_input.strip():
            translated = translate_text(text_input)
            st.info(f"**Translated:** {translated}")
        else:
            st.warning("Please enter text to translate.")

elif task == "Question Answering":
    st.markdown("#### ❓ Ask a Question Based on Context")
    question = st.text_input("Enter your question here")
    if st.button("Answer Question"):
        if text_input.strip() and question.strip():
            answer = answer_question(question, text_input)
            st.success(f"💬 Answer: {answer}")
        else:
            st.warning("Enter both a context and a question.")

elif task == "Summarization":
    st.markdown("#### 📝 Summarize the Review Text")
    if st.button("Summarize"):
        if text_input.strip():
            summary = summarize_text(text_input)
            st.info(f"📰 Summary: {summary}")
        else:
            st.warning("Please enter a review to summarize.")

# ---------- Footer ----------
st.write("---")
st.markdown(
    "<div style='text-align: center; color: #aaa; font-size: 0.9rem;'>"
    "Developed by John Olalemi • Powered by 🤗 Hugging Face & 🧠 Streamlit"
    "</div>",
    unsafe_allow_html=True
)