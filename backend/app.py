from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import os
from dotenv import load_dotenv
import sys
import torch
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if sys.stdout.encoding != 'utf-8':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

allowed_origins = os.getenv('ALLOWED_ORIGINS', 'http://localhost:5173,http://localhost:3000').split(',')
CORS(app, origins=allowed_origins)

sentiment_pipeline = None
MODEL_PATH = os.getenv('MODEL_PATH', './fine_tuned_model')

def load_model():
    global sentiment_pipeline
    if sentiment_pipeline is None:
        logger.info("Model loading...")
        try:
            device = 0 if torch.cuda.is_available() else -1
            sentiment_pipeline = pipeline(
                "sentiment-analysis",
                model=MODEL_PATH,
                device=device
            )
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Model loading failed: {e}")
            raise

notes_storage = []

@app.route('/api/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400

        text = data.get('text', '').strip()
        if not text:
            return jsonify({'error': 'Text required'}), 400

        if len(text) > 1024:
            return jsonify({'error': 'Text too long (max 1024 chars)'}), 400

        load_model()
        result = sentiment_pipeline(text[:512])[0]
        label = result['label'].lower()
        score = float(result['score'])

        sentiment_map = {
            'negative': 'negative',
            'positive': 'positive',
            'neutral': 'neutral',
            'label_0': 'negative',
            'label_1': 'neutral',
            'label_2': 'positive'
        }

        sentiment = sentiment_map.get(label, 'neutral')

        return jsonify({
            'sentiment': sentiment,
            'score': score,
            'label': label
        })

    except ValueError as e:
        logger.warning(f"Invalid input: {e}")
        return jsonify({'error': 'Invalid input'}), 400
    except RuntimeError as e:
        logger.error(f"Model error: {e}")
        return jsonify({'error': 'Analysis failed'}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {type(e).__name__}")
        return jsonify({'error': 'Server error'}), 500

@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify(notes_storage)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    logger.info("Starting Sentiment Analysis Backend...")
    logger.info(f"http://localhost:5000")
    app.run(debug=debug_mode, port=5000)
