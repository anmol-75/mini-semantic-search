import chromadb


print("DATABASE FILE IS RUNNING")


# Create a persistent ChromaDB client
client = chromadb.PersistentClient(
    path="./database/chroma_db"
)

print("ChromaDB client created")


# Create or load a collection
collection = client.get_or_create_collection(
    name="ai_documents"
)

print("Collection created")


print("Collection name:", collection.name)
print("Documents:", collection.count())