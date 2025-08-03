
from chromadb import PersistentClient

chroma_client = PersistentClient(path="./chroma_storage")

collection = chroma_client.get_or_create_collection(name="book_versions")

def save_version(name, path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    collection.add(
        documents=[content],
        metadatas=[{"version": name}],
        ids=[name]
    )

# Save all versions (run only once per version)
save_version("original", "chapter_original.txt")
save_version("rewritten_v1", "chapter_rewritten_v1.txt")
save_version("edited_v1", "chapter_edited_final.txt")

print("✅ All versions saved to ChromaDB.")
