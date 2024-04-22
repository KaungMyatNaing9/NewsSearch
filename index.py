import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re
from flask import Flask, request, jsonify

def preprocess_text(text):
    # Simple text cleaning and normalization
    text = re.sub(r'<[^>]*>', '', text)  # Remove HTML tags
    text = re.sub(r'[\W]+', ' ', text.lower())  # Remove non-words and convert to lower case
    return text

# Load and preprocess the documents
with open('output.json', 'r') as file:
    data = json.load(file)
documents = [preprocess_text(item['content']) for item in data]

# Create the TF-IDF model and matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Save the objects for later use in the Flask app
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f)

def search(query, top_k=5):
    # Load saved model and matrix
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('tfidf_matrix.pkl', 'rb') as f:
        matrix = pickle.load(f)

    # Transform the query to the same dimension as the TF-IDF matrix
    query_vec = vectorizer.transform([query])
    # Calculate cosine similarity
    similarity = cosine_similarity(query_vec, matrix).flatten()

    # Get top K indices sorted by highest similarity scores
    top_indices = np.argsort(similarity)[-top_k:][::-1]
    results = [{'index': int(idx), 'score': float(similarity[idx])} for idx in top_indices]

    return results

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def handle_search():
    try:
        data = request.get_json()
        query = data['query']
        if not query:
            return jsonify({'error': 'Empty query provided'}), 400
        
        results = search(query)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)