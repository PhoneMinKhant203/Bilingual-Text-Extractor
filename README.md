# Bilingual-Text-Extractor
This is a simple Flask web application that extracts only the **English sentences** from a bilingual text (Burmese and English).  
It uses the **DeepSeek API** (OpenAI-compatible) to process the input text and return clean English-only output.

---

Features

- Upload or type bilingual text (Burmese-English mixed)
- Automatically extract only the English sentences
- Fast and lightweight Flask server
- Integrates with DeepSeek API via OpenAI SDK
- JSON API for easy frontend/backend integration

---

Tech Stack

- Python 3
- Flask
- DeepSeek (via OpenAI client)
- HTML/CSS (for frontend)

---

Installation

1. Clone the repository:
git clone https://github.com/PhoneMinKhant203/Bilingual-Text-Extractor.git

2. Install the required Python packages:
pip install -r requirements.txt

3. Create a .env file in the project root:
DEEPSEEK_API_KEY=your_deepseek_api_key_here

4.Run the Flask app:
python app.py
