# 🚀 Tech Signal Engine

Tech Signal Engine is a lightweight backend system that collects, processes, and normalizes signals from multiple sources like GitHub Trending and RSS feeds.

---

## 📌 Features

- GitHub Trending data extraction
- RSS feed parsing and normalization
- Simple AI processing layer for signal formatting
- Clean modular backend structure
- FastAPI-ready architecture (optional extension)

---

## 🏗️ Project Structure

- app/ → Core application logic
- tests/ → Unit tests for sources
- ai_engine.py → Signal processing logic
- rss.py → RSS feed handler
- github_detect.py → GitHub trending extractor

---

## ⚙️ Tech Stack

- Python 3.11+
- Requests / BeautifulSoup
- FastAPI (future extension)
- PyTest

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app/main.py
