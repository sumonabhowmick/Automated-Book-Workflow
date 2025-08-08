
def reward_function(text: str) -> int:
    score = 0
    word_count = len(text.split())

    # 1. Prefer conciseness
    if word_count < 600:
        score += 2
    elif word_count < 800:
        score += 1

    # 2. Look for dialogue
    dialogue_count = text.lower().count("he said") + text.lower().count("she said")
    if dialogue_count >= 2:
        score += 2
    elif dialogue_count == 1:
        score += 1

    # 3. Thematic words
    themes = ["storm", "island", "ship", "canoe", "war"]
    score += sum(1 for word in themes if word in text.lower())

    # 4. Readability via punctuation
    if text.count(".") > 20:
        score += 2
    elif text.count(".") > 10:
        score += 1

    if text.count(",") > 15:
        score += 1

    # 5. Bonus for emotional words
    if any(word in text.lower() for word in ["love", "fear", "hope", "hate"]):
        score += 1

    return score


