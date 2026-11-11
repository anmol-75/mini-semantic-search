import json

from embeddings import create_embedding
from database import collection


# Load documents from JSON file
with open(
    "data/documents.json",
    "r",
    encoding="utf-8"
) as file:

    documents = json.load(file)


print(f"Loaded {len(documents)} documents.")


# Process each document
for doc in documents:

    print(f"\nProcessing: {doc['title']}")

    # Convert document text into a vector embedding
    embedding = create_embedding(doc["text"])

    print(f"Embedding created with {len(embedding)} dimensions.")

    # Store the document, embedding, and metadata in ChromaDB
    collection.add(
        ids=[doc["id"]],

        documents=[doc["text"]],

        embeddings=[embedding],

        metadatas=[
            {
                "title": doc["title"],
                "category": doc["category"]
            }
        ]
    )


print("\nDocuments inserted successfully.")
print(f"Total documents in ChromaDB: {collection.count()}")