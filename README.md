# Mini Semantic Search

A beginner-friendly semantic search project built using Python, Sentence Transformers, and ChromaDB.

## 🚀 Project Overview

This project converts documents and user queries into numerical **embeddings** and uses a vector database to find the most semantically relevant documents.

Unlike traditional keyword search, semantic search focuses on the **meaning** of the text.

### How it works

```text
Documents
    ↓
Embedding Model
    ↓
384-dimensional Embeddings
    ↓
ChromaDB
    ↓
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Relevant Documents
```

## 🛠️ Technologies Used

- Python
- Sentence Transformers
- `all-MiniLM-L6-v2`
- ChromaDB
- JSON

## 📁 Project Structure

```text
mini-semantic-search/
│
├── data/
│   └── documents.json
│
├── database/
│   └── chroma_db/
│
├── src/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── database.py
│   ├── ingest.py
│   └── search.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔍 How the Search Works

First, the documents are converted into embeddings using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Each document becomes a **384-dimensional vector**.

For example:

```text
Document
   ↓
Embedding Model
   ↓
[0.12, -0.43, 0.67, ..., 0.05]
```

When a user enters a query, the query is also converted into a 384-dimensional vector.

ChromaDB then compares the **query vector** with the stored document vectors and returns the most similar documents.

```text
Query
  ↓
Query Embedding
  ↓
Compare with Document Embeddings
  ↓
Calculate Distance
  ↓
Rank Results
  ↓
Return Most Relevant Documents
```

## ▶️ Running the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Insert documents into ChromaDB

```bash
python src/ingest.py
```

This reads the documents from `data/documents.json`, creates embeddings, and stores them in ChromaDB.

### 3. Perform a semantic search

```bash
python src/search.py
```

The search script converts the query into an embedding and retrieves the most similar documents.

## 📚 What I Learned

This project helped me understand:

- Text embeddings
- 384-dimensional vectors
- Sentence Transformers
- Vector databases
- ChromaDB collections
- Semantic search
- Query embeddings
- Vector similarity and distance
- The basic retrieval step behind RAG systems

## 🔮 Future Improvements

- Add a frontend for user queries
- Add document chunking
- Add more documents
- Add similarity score filtering
- Add an LLM for answer generation
- Convert the project into a complete RAG application

## 👨‍💻 Author

**Anmol A**

Built as a hands-on project to understand embeddings, vector databases, semantic search, and the foundations of RAG.