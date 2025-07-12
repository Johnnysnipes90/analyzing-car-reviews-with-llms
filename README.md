![image](../images/car.jpeg)

# 🤖 Analyzing Car Reviews with LLMs

**Car-ing is Sharing** — an auto dealership company — is leveling up its customer experience using **Large Language Models (LLMs)**.

As part of their AI/NLP team, this project prototypes a **chatbot assistant** powered by Hugging Face Transformers that can:
- Assist customers
- Support human agents
- Analyze and respond to car reviews

---

## 🔧 Features

This project demonstrates real-world applications of LLMs:

- ✅ **Sentiment Classification** – Understand customer feedback on car reviews
- 🌍 **Machine Translation (EN → ES)** – Translate reviews into Spanish and evaluate with BLEU
- ❓ **Question Answering** – Extract brand-related preferences from review content
- 📝 **Summarization** – Generate concise summaries of long car reviews

---

## 📂 Project Structure

```plaintext
analyzing-car-reviews-with-llms/
│
├── data/
│   ├── car_reviews.csv                  # Car review dataset
│   └── reference_translations.txt       # Spanish reference translations
│
├── notebooks/
│   └── 01_prototype_chatbot.ipynb       # Main LLM-powered chatbot notebook
│
├── images/
│   └── car.jpeg                         # Project image for README or UI
│
├── README.md                            # Project documentation
├── requirements.txt                     # Python dependencies
└── .gitignore                           # Ignored files and folders

```

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/analyzing-car-reviews-with-llms.git
cd analyzing-car-reviews-with-llms
```

### 2. Set up environment
Install the required libraries
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
