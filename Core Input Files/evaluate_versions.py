
import os

def reward_function(text: str) -> int:
    """
    A better reward function to simulate RL-style scoring of rewritten chapters.
    """
    score = 0

    # ✅ Shorter content is easier to read
    if len(text) < 3000:
        score += 2
    elif len(text) < 4000:
        score += 1

    # ✅ Detect dialogues (more engaging)
    if "he said" in text.lower() or "she said" in text.lower():
        score += 1

    # ✅ Thematic keywords
    keywords = ["storm", "island", "ship", "ocean", "danger", "wind"]
    score += sum(word in text.lower() for word in keywords)

    # ✅ Sentence quality via punctuation balance
    dot_count = text.count(".")
    comma_count = text.count(",")
    if dot_count > 20 and comma_count > 10:
        score += 2
    elif dot_count > 10:
        score += 1

    # ✅ Simplicity (lower average word length)
    words = text.split()
    if words:
        avg_word_length = sum(len(w) for w in words) / len(words)
        if avg_word_length < 5:
            score += 2
        elif avg_word_length < 6:
            score += 1

    return score

# ----------------------------
# 🎯 Evaluate all versions
# ----------------------------

scores = {}

for i in range(1, 4):  # Assuming you have chapter_rewritten_v1.txt, v2, and v3
    filename = f"Core Output Files/chapter_rewritten_v{i}.txt"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            score = reward_function(content)
            print(f"🧠 Version {i} score: {score}")
            scores[filename] = score
    else:
        print(f"⚠️ {filename} not found.")

# ----------------------------
# 🏆 Save the best version
# ----------------------------

if scores:
    best_version = max(scores, key=scores.get)
    print(f"\n🏆 Best version: {best_version} (Score: {scores[best_version]})")

    with open(best_version, "r", encoding="utf-8") as f_in:
        final_text = f_in.read()

    with open("Core Output Files/chapter_final.txt", "w", encoding="utf-8") as f_out:
        f_out.write(final_text)

    print("✅ Best version saved as chapter_final.txt in Core Output Files.")
else:
    print("❌ No versions were evaluated.")
