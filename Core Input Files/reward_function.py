
def reward_function(text: str) -> int:
    """
    Simple reward function that simulates RL by assigning scores.
    """
    score = 0

    # Heuristic rules
    if len(text) < 3000:
        score += 2  # Shorter, simpler is preferred
    if "he said" in text or "she said" in text:
        score += 1  # Dialogues detected
    if any(x in text.lower() for x in ["storm", "island", "ship"]):
        score += 1  # Key thematic words present
    if "." in text and "," in text:
        score += 2  # Good punctuation = good readability

    return score
