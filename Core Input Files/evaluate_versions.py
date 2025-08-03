
from reward_function import reward_function

files = {
    "original": "chapter_original.txt",
    "rewritten_v1": "chapter_rewritten_v1.txt",
    "edited_v1": "chapter_edited_final.txt"
}

scores = {}

for name, path in files.items():
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        score = reward_function(content)
        scores[name] = score

# Rank versions by score
sorted_versions = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("🏆 Version Rankings (RL-style scoring):")
for version, score in sorted_versions:
    print(f"{version}: {score}")
