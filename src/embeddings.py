from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text: str):
    embedding = model.encode(text)

    return embedding


if __name__ == "__main__":
    text = "Machine learning allows computers to learn from data."

    embedding = create_embedding(text)

    print("Text:")
    print(text)

    print("\nEmbedding:")
    print(embedding)

    print("\nNumber of dimensions:")
    print(len(embedding))