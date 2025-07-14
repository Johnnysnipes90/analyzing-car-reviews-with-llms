![Car Review AI Assistant](images/car.jpeg)

# 🤖 Analyzing Car Reviews with LLMs

**Car-ing is Sharing** — a forward-thinking auto dealership company — is enhancing its customer service using **Large Language Models (LLMs)**.

As part of their AI/NLP team, this project prototypes an intelligent **AI assistant** powered by Hugging Face Transformers. It can:
- Analyze and respond to car reviews
- Assist customers via natural language understanding
- Support human agents with automation and insights

---

## 🔧 Key Features

This app demonstrates practical, production-ready use of LLMs:

- ✅ **Sentiment Classification** – Detect positive or negative feedback in car reviews  
- 🌍 **Translation (EN → ES)** – Translate customer reviews from English to Spanish with BLEU evaluation  
- ❓ **Question Answering** – Answer questions based on the context of any review  
- 📝 **Summarization** – Generate concise summaries of long car reviews  

---

## 🖥️ Live Streamlit Web App

> Easily interact with the assistant via an intuitive frontend.

To launch the app:

```bash
streamlit run app/streamlit_app.py
```

## 📂 Project Structure

```plaintext
analyzing-car-reviews-with-llms/
│
├── app/
│   └── streamlit_app.py               # Streamlit UI app
│
├── src/
│   ├── sentiment.py                   # Sentiment classifier
│   ├── translation.py                 # Translation function
│   ├── summarization.py               # Text summarization
│   └── question_answering.py          # QA module
│
├── data/
│   ├── car_reviews.csv                # Dataset of car reviews
│   └── reference_translations.txt     # Reference Spanish translations
│
├── notebooks/
│   └── 01_prototype_chatbot.ipynb     # LLM demonstration notebook
│
├── images/
│   └── car.jpeg                       # Project image (used in README/UI)
│
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
└── .gitignore                         # Ignored files and folders

```

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/analyzing-car-reviews-with-llms.git
cd analyzing-car-reviews-with-llms
```

### 2. Install Dependencies
Install the required libraries
```bash
pip install -r requirements.txt
```

### 3. Run the notebook

```bash
jupyter notebook notebooks/01_prototype_chatbot.ipynb
```

### Launch the Streamlit App
```bash
streamlit run app/streamlit_app.py
```

## 📦 Requirements
```txt
transformers
evaluate
scikit-learn
pandas
torch
nltk
streamlit

```

## ✅ requirements.txt

```txt
transformers
evaluate
scikit-learn
pandas
torch
nltk
```

## 🛑 .gitignore
```bash
__pycache__/
.ipynb_checkpoints/
.env
*.pyc
.DS_Store
```

## ✨ Author

Olalemi John Oluwatosin
💼 LinkedIn : www.linkedin.com/in/john-olalemi
💻 GitHub: github.com/Johnnysnipes90

## 🧠 Powered By
- 🤗 Hugging Face Transformers

- 🧠 Streamlit

- 🐍 Python NLP ecosystem (scikit-learn, NLTK, Evaluate)
