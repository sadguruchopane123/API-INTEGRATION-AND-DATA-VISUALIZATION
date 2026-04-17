"""
TASK-3: AI Chatbot with NLP
Internship: CODTECH

Description:
This chatbot uses NLP techniques (NLTK) such as tokenization,
lemmatization, and similarity matching to answer user queries.
"""

import nltk
import random
import string
import numpy as np

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download resources (run once)
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# ==============================
# 📚 KNOWLEDGE BASE (CORPUS)
# ==============================
corpus = [
    "Hello",
    "Hi",
    "How are you",
    "What is your name",
    "What is Python",
    "Tell me about internship",
    "What is machine learning",
    "What is AI",
    "Bye"
]

responses = [
    "Hello! How can I help you?",
    "Hi there!",
    "I'm doing great, thanks!",
    "I am an AI Chatbot created for CODTECH internship.",
    "Python is a popular programming language used in AI, ML, and web development.",
    "This internship helps you learn real-world coding skills.",
    "Machine Learning is a part of AI that allows systems to learn from data.",
    "AI stands for Artificial Intelligence.",
    "Goodbye! Have a nice day!"
]

# ==============================
# 🔍 PREPROCESSING FUNCTION
# ==============================
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)

    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]

    return tokens

# ==============================
# 📊 SIMILARITY FUNCTION
# ==============================
def sentence_similarity(user_input, sentence):
    user_tokens = preprocess(user_input)
    sentence_tokens = preprocess(sentence)

    all_words = list(set(user_tokens + sentence_tokens))

    user_vector = [user_tokens.count(word) for word in all_words]
    sentence_vector = [sentence_tokens.count(word) for word in all_words]

    # Cosine similarity
    dot_product = np.dot(user_vector, sentence_vector)
    magnitude = np.linalg.norm(user_vector) * np.linalg.norm(sentence_vector)

    if magnitude == 0:
        return 0
    return dot_product / magnitude

# ==============================
# 🤖 CHATBOT RESPONSE
# ==============================
def get_response(user_input):
    similarities = []

    for sentence in corpus:
        sim = sentence_similarity(user_input, sentence)
        similarities.append(sim)

    max_index = similarities.index(max(similarities))

    if similarities[max_index] > 0:
        return responses[max_index]
    else:
        return "Sorry, I didn't understand that."

# ==============================
# 🚀 MAIN CHAT LOOP
# ==============================
def chatbot():
    print("🤖 AI Chatbot Started! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break

        response = get_response(user_input)
        print("Bot:", response)

# ==============================
# ▶️ RUN
# ==============================
if __name__ == "__main__":
    chatbot()
