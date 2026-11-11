from embeddings import create_embedding
from database import collection

query = "How do computers learn from data?"

print("search query:")
print (query)

query_embedding = create_embedding(query)

print("\nQuery embedding created.")
print("Number of dimentions :",len(query_embedding))

results = collection.query(
    query_embeddings = [query_embedding],
    n_results = 3
)

print("\nSearch result :")
print("=" * 60)

for i in range(len(results["ids"][0])):
    
    print(f"\nResult {i + 1}")

    print("ID:")
    print(results["ids"][0][i])

    print("\nDocument:")
    print(results["documents"][0][i])

    print("\nMetadata:")
    print(results["metadatas"][0][i])

    print("\nDistance:")
    print(results["distances"][0][i])

    print("-" * 60)