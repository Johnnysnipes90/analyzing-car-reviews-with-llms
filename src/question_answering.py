from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/minilm-uncased-squad2")

def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)['answer']
    return result
