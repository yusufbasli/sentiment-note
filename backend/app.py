from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

sentiment_pipeline = None

def load_model():
    global sentiment_pipeline
    if sentiment_pipeline is None:
        print("🤖 Sentiment Analysis modeli yükleniyor...")
        sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="xlm-roberta-base",
            device=-1
        )
        print("✅ Model yüklendi!")

notes_storage = []

@app.route('/api/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.json
        text = data.get('text', '')

        if not text:
            return jsonify({'error': 'Text gerekli'}), 400

        load_model()

        result = sentiment_pipeline(text[:512])[0]

        label = result['label'].lower()
        score = result['score']

        sentiment_map = {
            'negative': 'negative',
            'positive': 'positive',
            'neutral': 'neutral'
        }

        sentiment = sentiment_map.get(label, 'neutral')

        return jsonify({
            'sentiment': sentiment,
            'score': score,
            'label': label
        })

    except Exception as e:
        print(f"Hata: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify(notes_storage)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    print("🚀 Duygu Analiz Backend başlatılıyor...")
    print("📍 http://localhost:5000")
    app.run(debug=True, port=5000)
