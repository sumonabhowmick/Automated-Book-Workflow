# 📚 Automated Book Publication Workflow

This project automates the process of fetching, rewriting, reviewing, and publishing book chapters using AI and agentic voice control.

## 🚀 Features

- ✅ Web scraping of book chapter (from Wikisource)
- 📸 Screenshot of webpage
- 🤖 Chapter rewriting using Gemini AI
- 🧠 AI review and feedback
- ✍️ Human-in-the-loop editing (optional)
- 📦 Version tracking using ChromaDB
- 🔎 Semantic search across versions
- 🧠 Reward-based version evaluation
- 🔊 Text-to-speech voice output
- 🗣️ Voice/text agentic command interface

## 🛠️ How to Run

1. Clone the repo
2. Set up virtual environment (optional but recommended)
3. Install dependencies: pip install -r requirements.txt
4. Run each step manually or use agentic interface:
- `scrape_and_screenshot.py`
- `ai_rewrite.py`
- `ai_review.py`
- `save_versions.py`
- `semantic_search.py`
- `reward_feedback.py`
- `text_to_speech.py`
- Or launch `agentic_interface.py` to do it via commands

## 🧠 Tech Stack

- Python
- Google Gemini API
- ChromaDB (for version saving/search)
- gTTS / pyttsx3 (text-to-speech)
- speech_recognition (voice agent)
- Playwright or requests+bs4 (scraping)