
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

def scrape_text():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", {"class": "mw-parser-output"})
    
    paragraphs = content.find_all("p")
    chapter_text = "\n".join(p.get_text() for p in paragraphs if p.get_text().strip())

    with open("chapter_original.txt", "w", encoding="utf-8") as f:
        f.write(chapter_text)

    print("✅ Chapter text scraped and saved as chapter_original.txt")

def take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path="chapter_screenshot.png", full_page=True)
        browser.close()

    print("📸 Screenshot saved as chapter_screenshot.png")

scrape_text()
take_screenshot()
