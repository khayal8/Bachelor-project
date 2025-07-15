import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import os

nltk.download('stopwords')

MODEL_PATH = 'spam_detector_model.pkl'
VEC_PATH = 'spam_vectorizer.pkl'

stemmer = PorterStemmer()
stopwords_set = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stopwords_set]
    return ' '.join(words)

if os.path.exists(MODEL_PATH) and os.path.exists(VEC_PATH):
    print("Loaded trained model.")
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(VEC_PATH, 'rb') as f:
        vectorizer = pickle.load(f)
else:
    print("Training new model")

    df = pd.read_csv('spam.csv', encoding='ISO-8859-1')[['v1', 'v2']]
    df.columns = ['label', 'message']
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    corpus = [preprocess_text(msg) for msg in df['message']]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    with open(VEC_PATH, 'wb') as f:
        pickle.dump(vectorizer, f)
    print("M and V saved!")


while True:
    print("\nType a message to check if it's spam (or type 'exit' to quit):")
    user_input = input(">>> ")

    if user_input.lower() == 'exit':
        print("Bye!")
        break

    cleaned = preprocess_text(user_input)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    if prediction == 1:
        print("This message is likely: SPAM")
    else:
        print("This message is likely: NOT SPAM")
