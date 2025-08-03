import os
import subprocess
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

# -----------------------------
# 🔧 CONFIG
# -----------------------------

# Text-to-speech setup
engine = pyttsx3.init()

def speak(text):
    print(f"🗣️ {text}")
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# 🎙️ VOICE RECOGNITION
# -----------------------------

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🎙️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        speak("Voice service is unavailable.")
        return ""

# -----------------------------
# 🧠 COMMAND PROCESSOR
# -----------------------------

def process_command(cmd):
    global mode

    if "scrape" in cmd or "download" in cmd:
        speak("Scraping chapter and taking screenshot.")
        subprocess.run(["python", "scrape_and_screenshot.py"])

    elif "rewrite" in cmd or "spin" in cmd:
        speak("Rewriting the chapter using Gemini.")
        subprocess.run(["python", "ai_rewrite.py"])

    elif "edit" in cmd:
        speak("Please open the file and manually edit it.")

    elif "review" in cmd:
        speak("🧠 Reviewing the chapter using AI.")
        os.system("python ai_review.py")
    

    elif "save versions" in cmd:
        speak("Saving all chapter versions to the database.")
        subprocess.run(["python", "save_versions.py"])

    elif "search" in cmd:
        speak("What are you searching for?")
        query = get_command()
        response = model.generate_content(f"Search for '{query}' in saved book versions")
        print("📚 AI says:", response.text)
        speak(response.text)
        subprocess.run(["python", "semantic_search.py"])

    elif "best version" in cmd or "which version" in cmd:
        speak("Evaluating the best version using feedback scores.")
        subprocess.run(["python", "evaluate_versions.py"])

    elif "read" in cmd or "voice" in cmd or "speak" in cmd:
        speak("Reading the final chapter aloud.")
        subprocess.run(["python", "text_to_speech.py"])

    elif "switch to text" in cmd:
        mode = "text"
        speak("Switched to text input mode.")

    elif "switch to voice" in cmd:
        mode = "voice"
        speak("Switched to voice input mode.")

    elif "exit" in cmd or "quit" in cmd:
        speak("Goodbye!")
        exit()

    else:
        speak("I don't recognize that command.")

# -----------------------------
# 🧠 MODE SETUP + INPUT
# -----------------------------

def get_command():
    if mode == "voice":
        return listen()
    else:
        return input("💬 Your command: ").lower()

# -----------------------------
# 🚀 AGENT START
# -----------------------------

if __name__ == "__main__":
    speak("Agent ready. Would you like to use voice or text commands?")
    mode = input("💬 Type 'voice' or 'text': ").strip().lower()

    if mode not in ["voice", "text"]:
        print("⚠️ Invalid input. Defaulting to text mode.")
        mode = "text"

    while True:
        command = get_command()
        if command:
            process_command(command)

