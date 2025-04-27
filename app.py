from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI 

app = Flask(__name__)
load_dotenv()

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')

# Initialize OpenAI client with DeepSeek base URL
deepseek = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"   
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_english():
    try:
        data = request.get_json()
        bilingual_text = data.get('text', '')
        
        if not bilingual_text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Prepare prompt for DeepSeek
        prompt = f"""Extract only the English sentences from the following bilingual (Burmese and English) text. 
        Return just the English sentences, nothing else. Don't include any Burmese text in the output.
        
        Input text:
        {bilingual_text}
        
        English sentences only:"""
        
        # Call DeepSeek API
        response = deepseek.chat.completions.create(
            model="deepseek-chat", 
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=7000,
            stream=False,
            temperature=0.7

        )
        
        # Extract the English text from the response
        english_text = response.choices[0].message.content 
        
        return jsonify({'english_text': english_text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)