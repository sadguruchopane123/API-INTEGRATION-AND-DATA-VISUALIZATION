"""
TASK-4: Machine Learning Model Implementation
Internship: CODTECH

Description:
This script builds a predictive model using Scikit-learn
to classify messages as Spam or Not Spam (Ham).
It includes data creation, preprocessing, training,
testing, and evaluation.
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# ==============================
# 📊 CREATE DATASET
# ==============================
def create_dataset():
    print("Creating dataset...")

    data = {
        "text": [
            "Win money now",
            "Hello friend how are you",
            "Limited offer buy now",
            "Meeting at 5 pm",
            "Congratulations you won prize",
            "Let's study together",
            "Get free coupons",
            "Call me later",
            "Earn money fast",
            "Good morning"
        ],
        "label": [
            "spam",
            "ham",
            "spam",
            "ham",
            "spam",
            "ham",
            "spam",
            "ham",
            "spam",
            "ham"
        ]
    }

    df = pd.DataFrame(data)
    print("✅ Dataset created")
    return df

# ==============================
# 🔄 PREPROCESS DATA
# ==============================
def preprocess_data(df):
    print("Preprocessing data...")

    df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})

    X = df['text']
    y = df['label_num']

    return train_test_split(X, y, test_size=0.3, random_state=42)

# ==============================
# 🧠 TRAIN MODEL
# ==============================
def train_model(X_train, y_train):
    print("Training model...")

    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)

    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    print("✅ Model trained")
    return model, vectorizer

# ==============================
# 📈 EVALUATE MODEL
# ==============================
def evaluate_model(model, vectorizer, X_test, y_test):
    print("Evaluating model...")

    X_test_vec = vectorizer.transform(X_test)
    y_pred = model.predict(X_test_vec)

    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

# ==============================
# 🔍 TEST CUSTOM INPUT
# ==============================
def test_custom_input(model, vectorizer):
    print("\nTesting custom input...")

    sample = ["Win a free iPhone now"]
    sample_vec = vectorizer.transform(sample)

    prediction = model.predict(sample_vec)

    if prediction[0] == 1:
        print("Prediction: Spam")
    else:
        print("Prediction: Not Spam")

# ==============================
# 🚀 MAIN FUNCTION
# ==============================
def main():
    df = create_dataset()

    X_train, X_test, y_train, y_test = preprocess_data(df)

    model, vectorizer = train_model(X_train, y_train)

    evaluate_model(model, vectorizer, X_test, y_test)

    test_custom_input(model, vectorizer)

    print("\n🎉 Task-4 Completed Successfully!")

# ==============================
# ▶️ RUN
# ==============================
if __name__ == "__main__":
    main()
