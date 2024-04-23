import json
import numpy as np
import re
import pickle
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Preprocess Text Function
def preprocess_text(text):
    text = re.sub(r'<[^>]*>', '', text)  # Remove HTML tags
    text = re.sub(r'[\W]+', ' ', text.lower())  # Remove non-words and convert to lower case
    return text

# Load and preprocess the documents, assuming each document includes 'content' and 'url'
with open('output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
documents = [{'content': preprocess_text(item['content']), 'url': item.get('url', 'No URL provided')} for item in data]

# Create the TF-IDF model and matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([doc['content'] for doc in documents])

# Save the objects for later use in the Flask app
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f)

# Search Function
def search(query, top_k=10):
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('tfidf_matrix.pkl', 'rb') as f:
        matrix = pickle.load(f)

    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, matrix).flatten()
    top_indices = np.argsort(similarity)[-top_k:][::-1]
    
    results = [{'index': int(idx), 'url': documents[idx]['url'], 'score': float(similarity[idx])} for idx in top_indices]
    return results

# Home Page Route
@app.route('/')
def home():
    return '''
    <h1>Search from WiKi</h1>
    <p>Please type the thing you wanted to search!!</p>
    <form action="/search" method="post">
        <input type="text" name="query" placeholder="Enter search query" required>
        <input type="submit" value="Search">
    </form>
    '''

# Search Endpoint
@app.route('/search', methods=['POST', 'GET'])
def handle_search():
    try:
        if request.method == 'POST':
            data = request.get_json() if request.is_json else request.form
            query = data['query']
        elif request.method == 'GET':
            query = request.args.get('query', '')

        if not query:
            return jsonify({'error': 'Empty query provided'}), 400
        
        results = search(query)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run Flask Application
if __name__ == '__main__':
    app.run(debug=True)
