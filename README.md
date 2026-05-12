# Sentiment Note 📝💭

A web application that automatically analyzes the emotional sentiment (positive, negative, neutral) of written notes using AI.

## 🎯 About the Project

Sentiment Note uses natural language processing (NLP) technology to analyze the emotions in notes written by users. With this application, you can write notes, view the sentiment of each note, and track your overall emotional trend.

### Features

- ✨ **Real-time Sentiment Analysis** - Get instant emotion analysis as you write (92.2% accuracy)
- 🎨 **Color-Coded Visualization** - Each emotion type is displayed with distinct colors
- 📊 **Statistics Dashboard** - View sentiment distribution across all your notes
- 🌍 **Multi-language Support** - Works with Turkish and English text
- 🚀 **Fast Response Time** - GPU-accelerated inference for instant analysis

## 🏗️ Technology Stack

### Backend
- **Python 3.13** - Programming language
- **Flask 3.1.3** - Web framework
- **Transformers 5.8.0** - NLP model library (Hugging Face)
- **PyTorch 2.11.0** - Deep Learning framework
- **XLM-RoBERTa** - Multilingual BERT model (fine-tuned)

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool & dev server
- **Axios** - HTTP client
- **CSS3** - Modern styling

## 📋 Installation

### Requirements
- Python 3.13+
- Node.js 18+
- GPU (optional but recommended - CPU may be slow)
- ~4 GB disk space (for model files)

### 1️⃣ Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server (model loads automatically)
python app.py
```

Server will run at `http://localhost:5000`

### 2️⃣ Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Application will open at `http://localhost:5173`

## 🚀 Usage

1. Open the frontend at `http://localhost:5173`
2. Write text in the note box (max 1024 characters)
3. Click the "Analyze" button
4. See the sentiment analysis result:
   - 😔 **Negative** - Negative emotion (confidence: 95.2%)
   - 😐 **Neutral** - Neutral/objective text (confidence: 84.0%)
   - 😊 **Positive** - Positive emotion (confidence: 100%)

### Example Notes

```
"Today was a wonderful day!" → Positive (92% confidence)
"Things are a bit complicated" → Neutral (80% confidence)
"I felt really disappointed" → Negative (85% confidence)
```

## 🏛️ Project Structure

```
sentiment-note-app/
├── backend/
│   ├── app.py                    # Flask backend & API
│   ├── fine_tune.py              # Model training script
│   ├── prepare_data.py           # Data preparation
│   ├── gpu_check.py              # GPU validation
│   ├── fine_tuned_model/         # Trained model (saved)
│   ├── data/
│   │   ├── sentiment_data.csv    # Full dataset (419 examples)
│   │   ├── train.csv             # Training set (293 examples)
│   │   ├── validation.csv        # Validation set (62 examples)
│   │   └── test.csv              # Test set (64 examples)
│   ├── requirements.txt           # Python dependencies
│   ├── .env                       # Environment variables
│   └── .env.example               # Example env file
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                # Main component
│   │   ├── main.jsx               # Entry point
│   │   ├── components/
│   │   │   ├── Dashboard.jsx      # Statistics dashboard
│   │   │   ├── NoteForm.jsx       # Note input form
│   │   │   └── NoteList.jsx       # Notes display
│   │   └── styles/
│   │       ├── Dashboard.css
│   │       ├── NoteForm.css
│   │       └── NoteList.css
│   ├── package.json
│   ├── vite.config.js
│   └── .env.example               # Example env file
│
└── README.md
```

## 🧠 Model Details

### Architecture
- **Base Model**: `xlm-roberta-base` (125M parameters)
- **Model Type**: Transformer-based sequence classification
- **Languages**: Turkish + English support

### Fine-tuning Dataset
- **Total Examples**: 419 (balanced)
  - Negative: 139 (33.2%)
  - Neutral: 155 (37.0%)
  - Positive: 125 (29.8%)

### Training Parameters
- **Epochs**: 15
- **Batch Size**: 4 (gradient accumulation: 4)
- **Effective Batch**: 16
- **Learning Rate**: 1e-5 (adaptive)
- **Warmup Steps**: 200
- **Optimizer**: AdamW with weight decay (0.01)
- **Class Weights**: Applied to handle class imbalance

### Test Performance

| Class | Accuracy | Test Samples |
|-------|----------|-------------|
| Negative | 95.2% | 21 |
| Neutral | 84.0% | 25 |
| Positive | 100% | 18 |
| **Overall** | **92.2%** | **64** |

## 🔧 API Endpoints

### POST `/api/analyze`
Analyze text and determine sentiment.

**Request:**
```json
{
  "text": "This is a wonderful day!"
}
```

**Response:**
```json
{
  "sentiment": "positive",
  "score": 0.918,
  "label": "positive"
}
```

**Error Response:**
```json
{
  "error": "Text too long (max 1024 chars)"
}
```

### GET `/api/notes`
Retrieve all notes.

**Response:**
```json
[
  {
    "id": 1234567890.123,
    "text": "This is a wonderful day!",
    "sentiment": "positive",
    "score": 0.918,
    "timestamp": "12/5/2026, 14:30:00"
  }
]
```

### GET `/health`
Check server status.

**Response:**
```json
{
  "status": "ok"
}
```

## 🎓 Learning Objectives

This project covers the following topics:

### Frontend Development
- React component architecture (functional components)
- State management with `useState`
- Side effects with `useEffect`
- API integration (Axios)
- Error handling and user feedback
- Responsive CSS design

### Backend Development
- Flask routing and REST API design
- CORS and security considerations
- Error handling and logging
- Environment variables management
- Model loading and inference optimization

### Machine Learning
- Pre-trained model fine-tuning
- Text preprocessing and tokenization
- Multi-class classification
- Class weights for imbalanced data handling
- Model evaluation and metrics
- GPU acceleration

### DevOps & Deployment
- Python virtual environments
- Dependency management (pip)
- Environment configuration (.env)
- Logging best practices

## 📊 Future Improvements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User accounts and authentication
- [ ] Note deletion and editing
- [ ] Filtering and search by date
- [ ] Export to CSV/JSON
- [ ] Dark mode UI
- [ ] Sentiment trend analysis
- [ ] Docker containerization
- [ ] Unit & integration tests
- [ ] CI/CD pipeline (GitHub Actions)

## 🐛 Troubleshooting

### Model loading error
```bash
# Check logs for errors
python backend/app.py 2>&1 | grep -i error

# Reinstall the model
rm -rf backend/fine_tuned_model
```

### CORS error
Check `ALLOWED_ORIGINS` in `.env` file:
```env
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Slow response time
- Check if GPU is being used: `python backend/gpu_check.py`
- Response time on CPU may be 1-2 seconds
- Response time drops significantly with CUDA-enabled GPU

### Port already in use
```bash
# Change backend port: edit port in app.py
# Change frontend port: npm run dev -- --port 3000
```

## 📚 Useful Resources

- [Hugging Face Transformers Docs](https://huggingface.co/transformers/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [XLM-RoBERTa Model Card](https://huggingface.co/xlm-roberta-base)

## 👤 Developer

**Yusuf Baslı** - 3rd Year Computer Engineering Student

## 📝 License

This project is developed for educational purposes. Licensed under MIT License.

---

**Created**: May 2026  
**Last Updated**: May 12, 2026  
**Model Accuracy**: 92.2% ✅


