
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini 2.5 Pro model
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

def rewrite_chapter():
    with open("Core Output Files/chapter_original.txt", "r", encoding="utf-8") as f:
        original_text = f.read()

    # Generate 3 different rewrites
    for i in range(1, 4):
        prompt = f"Rewrite version {i} of the following chapter in simpler, modern English:\n\n{original_text}"
        response = model.generate_content(prompt)
        rewritten = response.text

        output_path = f"Core Output Files/chapter_rewritten_v{i}.txt"
        with open(output_path, "w", encoding="utf-8") as f_out:
            f_out.write(rewritten)

        print(f"✅ Rewritten version {i} saved as chapter_rewritten_v{i}.txt")

rewrite_chapter()

