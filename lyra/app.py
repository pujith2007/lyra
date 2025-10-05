# app.py
from flask import Flask, request, jsonify, render_template
import requests  # to make API calls to ChatGPT / Gemini / Google services
import os

app = Flask(__name__)

# Serve the frontend
@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html is in a 'templates' folder

# Endpoint to handle chat messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    if not user_message:
        return jsonify({'reply': 'Please send a message!'}), 400

    # Example using OpenAI ChatGPT API
    # Replace 'YOUR_API_KEY' with your actual key or use environment variables
    api_key = os.environ.get('AIzaSyDWhiAKvB9d5DMzGLtnR9m_6WV2wNCOkjg', 'AIzaSyB9K2uaQE_z5Ujs5xkCaVxpUANLJmPE0rY')
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
    else:
        reply = "Sorry, I couldn't get a response from the AI service."

    return jsonify({'reply': reply})

if __name__ == "__main__":
    app.run(debug=True)
