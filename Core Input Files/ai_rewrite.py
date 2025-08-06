
import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  

model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

def rewrite_chapter():
    with open("Core Output Files/chapter_original.txt", "r", encoding="utf-8") as f:
        original_text = f.read()

    prompt = f"Rewrite the following chapter in simpler, modern English:\n\n{original_text}"

    response = model.generate_content(prompt)
    rewritten = response.text

    with open("Core Output Files/chapter_rewritten_v1.txt", "w", encoding="utf-8") as f:
        f.write(rewritten)

    print("✅ Chapter rewritten using Gemini and saved as chapter_rewritten_v1.txt")

rewrite_chapter()
