# 💭 Duygu Analiz Notesi (Sentiment Analysis Note App)

Notlarını yaz, duygu durumunu anla! React + Python Flask + Machine Learning projesi.

## 🎯 Proje Özellikleri

- ✍️ Notlar yaz ve kaydet
- 🤖 Doğal Dil İşleme (NLP) ile otomatik duygu analizi
- 😊 Emojiler ile görsel duygu göstergesi
- 📊 İstatistik dashboard
- 🎨 Modern ve responsive UI
- ⚡ Real-time analiz

## 🛠️ Tech Stack

### Frontend
- **React** + Vite (Hızlı geliştirme)
- **Axios** (HTTP requests)
- **CSS3** (Modern styling)

### Backend
- **Python Flask** (Web framework)
- **Transformers** (Hugging Face - ML models)
- **PyTorch** (Deep learning)
- **CORS** (Cross-origin requests)

## 📦 Kurulum

### 1️⃣ Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend çalışacak: `http://localhost:5173`

### 2️⃣ Backend Setup
```bash
cd backend

# Virtual environment oluştur
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate   # macOS/Linux

# Dependencies install et
pip install -r requirements.txt

# Server başlat
python app.py
```
Backend çalışacak: `http://localhost:5000`

## 🎓 Öğrenme Hedefleri

### Frontend:
- React component yapısı
- State management (useState)
- API calls (axios)
- CSS styling & responsive design
- Form handling

### Backend:
- Flask routing ve API endpoints
- CORS ve cross-origin requests
- Machine Learning pipeline integration
- Error handling

### ML:
- Pre-trained models kullanma
- Text preprocessing
- Sentiment classification
- Confidence scores

## 📁 Proje Yapısı

```
sentiment-note-app/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── NoteForm.jsx
│   │   │   ├── NoteList.jsx
│   │   │   └── Dashboard.jsx
│   │   ├── styles/
│   │   │   ├── NoteForm.css
│   │   │   ├── NoteList.css
│   │   │   └── Dashboard.css
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

## 🚀 Başlangıç

1. **Terminal 1** - Backend başlat:
```bash
cd backend
source venv/Scripts/activate
python app.py
```

2. **Terminal 2** - Frontend başlat:
```bash
cd frontend
npm run dev
```

3. Browser'da açın: `http://localhost:5173`

## 💡 Nasıl Kullanılır?

1. Textarea'ya bir not yaz
2. "✨ Analiz Et" butonuna tıkla
3. AI duygu durumunu analiz eder
4. Sonuç: Emoji + Duygu etiketi + Güven skoru
5. Tüm notların istatistiğini Dashboard'da gör

## 🔧 API Endpoints

### POST `/api/analyze`
Metni analiz et ve duygu belirle

**Request:**
```json
{
  "text": "Bugün çok mutluyum!"
}
```

**Response:**
```json
{
  "sentiment": "positive",
  "score": 0.95,
  "label": "positive"
}
```

### GET `/api/notes`
Kaydedilen tüm notları al

**Response:**
```json
[
  {
    "id": 1234567890,
    "text": "Bugün çok mutluyum!",
    "sentiment": "positive",
    "score": 0.95,
    "timestamp": "11.05.2026 14:30"
  }
]
```

## 📚 Sonraki Adımlar

- [ ] Veritabanı entegrasyonu (SQLite/PostgreSQL)
- [ ] Not silme ve güncelleme
- [ ] Kullanıcı authentication
- [ ] Tarihe göre filtreleme
- [ ] Export to CSV
- [ ] Dark mode
- [ ] Türkçe model fine-tuning

## 🤝 Kontribüsyon

Bu bir öğrenme projesidir! İyileştirmelerle katkıda bulun.

## 📝 Lisans

MIT License
