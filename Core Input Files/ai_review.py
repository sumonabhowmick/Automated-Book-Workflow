import google.generativeai as genai

# Step 1: Set up Gemini
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Step 2: Load rewritten chapter
with open("chapter_rewritten_v1.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Step 3: Create prompt for review
prompt = (
    "Act like a human reviewer and evaluate this chapter. "
    "Give feedback on grammar, clarity, tone, and style. "
    "List any improvements or issues you notice:\n\n" + content
)

# Step 4: Get AI review
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
response = model.generate_content(prompt)

# Step 5: Save output
with open("chapter_review.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("✅ AI Review saved to chapter_review.txt")
