# 🚀 Sentiment Analysis Note App - Hızlı Başlangıç

## 📍 Proje Konumu
```
C:\Users\Yusuf\sentiment-note-app
```

## ⚡ Çalıştırma (2 Terminal gerekli)

### Terminal 1: Backend Başlat
```bash
cd C:\Users\Yusuf\sentiment-note-app\backend
source venv/Scripts/activate
python app.py
```
✅ Backend çalışacak: http://localhost:5000

### Terminal 2: Frontend Başlat
```bash
cd C:\Users\Yusuf\sentiment-note-app\frontend
npm run dev
```
✅ Frontend çalışacak: http://localhost:5173

## 🎯 Kullanmaya Başla
1. Browser'da http://localhost:5173 aç
2. Textarea'ya bir not yaz
3. "✨ Analiz Et" butonuna tıkla
4. AI duygu analizi yapacak!

## 📁 Proje Yapısı
```
sentiment-note-app/
├── 📂 frontend/          (React + Vite)
│   ├── src/components/   (NoteForm, NoteList, Dashboard)
│   ├── src/styles/       (CSS dosyaları)
│   ├── package.json
│   └── vite.config.js
│
├── 📂 backend/           (Python Flask + ML)
│   ├── app.py           (Flask API)
│   ├── venv/            (Virtual environment)
│   ├── requirements.txt
│   └── .env
│
├── README.md
├── .gitignore
└── QUICKSTART.md (bu dosya)
```

## 🎓 Öğrenecekleriniz

### Frontend (React)
- Component yapısı
- Hooks (useState, useEffect)
- API calls (axios)
- Modern CSS styling
- Form handling

### Backend (Python)
- Flask web framework
- CORS middleware
- REST API endpoints
- Error handling

### ML (Transformers)
- Pre-trained models
- NLP pipeline
- Sentiment analysis
- Confidence scores

## 🔧 Troubleshooting

### Backend port 5000 already in use?
```bash
# Windows'da
lsof -i :5000
kill -9 <PID>

# Ya da port değiştir (app.py satır 60'ı düzenle)
```

### Frontend dependencies eksik?
```bash
cd frontend
rm -rf node_modules
npm install
```

### Model indirilmiyor?
First time run modeli indirecek (~500MB). İnternet bağlantısı gerekli.

## 📚 Sonraki Ders Konuları

1. **Database Integration**
   - SQLite ya da PostgreSQL
   - Not kalıcı depolama

2. **Authentication**
   - JWT tokens
   - User login/register

3. **Advanced Features**
   - Dark mode
   - Export to CSV
   - Date filtering
   - Advanced analytics

4. **Deployment**
   - Vercel (Frontend)
   - Render / Railway (Backend)
   - Docker containerization

## 🎉 Başarılı!
Tebrikler! ML + React + Python full-stack proje kurmayı başardın.
Şimdi öğrenmeye ve geliştirmeye başla! 🚀
