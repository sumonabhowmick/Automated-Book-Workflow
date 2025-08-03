
from chromadb import PersistentClient

chroma_client = PersistentClient(path="./chroma_storage")

collection = chroma_client.get_or_create_collection(name="book_versions")

query = input("🔎 Enter your search query: ")

results = collection.query(
    query_texts=[query],
    n_results=3
)

for i, doc in enumerate(results['documents'][0]):
    print(f"\nResult {i+1}:\n{doc[:400]}...\n")
