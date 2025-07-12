# analyzing-car-reviews-with-llms


# 🤖 Car-ing is Sharing - NLP Chatbot Prototype

An end-to-end AI-powered chatbot prototype for *Car-ing is Sharing*, an auto dealership company, using **Large Language Models (LLMs)**.
I've been asked to prototype a chatbot app with multiple functionalities that not only assist customers but also provide support to human agents in the company.

The solution should receive textual prompts and use a variety of pre-trained Hugging Face LLMs to respond to a series of tasks, e.g. classifying the sentiment in a car’s text review, answering a customer question, summarizing or translating text, etc.

## 📌 Project Features

This solution uses Hugging Face Transformers to:

- ✅ **Classify sentiment** in car reviews
- 🌍 **Translate** English reviews to Spanish and evaluate with BLEU
- ❓ **Answer questions** from car review context
- 📝 **Summarize** lengthy car reviews

---

## 📁 Project Structure



```analyzing-car-reviews-with-llms/
│
├── data/
│   ├── car_reviews.csv
│   └── reference_translations.txt
│
├── notebooks/
│   └── 01_prototype_chatbot.ipynb
│
├── images/
│   └── car.jpeg
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/analyzing-car-reviews-with-llms.git
cd analyzing-car-reviews-with-llms
```

### 2. Set up environment

```bash
pip install -r requirements.txt
```

### 3. Run the notebook

```bash
jupyter notebook notebooks/01_prototype_chatbot.ipynb
```

## 📦 Requirements
```txt
pandas
transformers
torch
scikit-learn
evaluate
nltk
```


---

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
💼 LinkedIn :
💻 GitHub: 
