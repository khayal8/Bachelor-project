from flask import Flask, request, jsonify
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from flask_cors import CORS

nltk.download('stopwords')

# Load model and vectorizer
with open("spam_detector_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("spam_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

stemmer = PorterStemmer()
stopwords_set = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stopwords_set]
    return ' '.join(words)

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    cleaned = preprocess_text(data['message'])
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    return jsonify({'spam': bool(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
