import json
import re
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
import faiss

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = text.lower()  # Lowercase text
    return text

# Load documents from Scrapy output
with open('output.json', 'r') as file:
    data = json.load(file)
documents = [item['content'] for item in data]
preprocessed_documents = [preprocess_text(doc) for doc in documents]

# Create the TF-IDF model and matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_documents)

# Save the TF-IDF model and matrix
with open('tfidf_model.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f)

# Train a Word2Vec model
sentences = [doc.split() for doc in preprocessed_documents]  # Tokenization
word2vec_model = Word2Vec(sentences, vector_size=100, window=5, min_count=2, sg=1)

# Transform documents to average Word2Vec vectors
def document_vector(doc):
    words = doc.split()
    word_vectors = [word2vec_model.wv[word] for word in words if word in word2vec_model.wv.key_to_index]
    if len(word_vectors) > 0:
        return np.mean(word_vectors, axis=0)
    else:
        return np.zeros(100)

doc_vectors = np.array([document_vector(doc) for doc in preprocessed_documents])

# Index vectors using FAISS
d = 100  # Dimension of vectors
index = faiss.IndexFlatL2(d)  # Build the FAISS index
index.add(doc_vectors.astype('float32'))  # Add vectors to the index

# Save the Word2Vec model and FAISS index
word2vec_model.save("word2vec.model")
faiss.write_index(index, "faiss_index.idx")

# Function to search in the index
def search(query, use_word2vec=False):
    if use_word2vec:
        query_vector = document_vector(preprocess_text(query))
        query_vector = np.array([query_vector]).astype('float32')
        distances, indices = index.search(query_vector, k=10)  # Search the FAISS index
    else:
        query_vector = vectorizer.transform([query])
        cosine_similarities = (query_vector * tfidf_matrix.T).toarray()[0]
        indices = np.argsort(cosine_similarities)[-10:][::-1]
        distances = cosine_similarities[indices]
    return indices, distances

