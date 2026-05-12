# Sentiment Note 📝💭

Yazılan notların duygusal durumunu (pozitif, negatif, tarafsız) otomatik olarak analiz eden web uygulaması.

## 🎯 Proje Hakkında

Sentiment Note, doğal dil işleme (NLP) teknolojisini kullanarak kullanıcıların yazdıkları notlardaki duyguyu analiz eder. Uygulama ile notlarınızı yazabilir, her notan'ın duygu durumunu görüp, genel duygusal eğiliminizi takip edebilirsiniz.

### Özellikler

- ✨ **Gerçek Zamanlı Duygu Analizi** - Notlar yazıldığında hemen duygu analizi yapılır (92.2% doğruluk)
- 🎨 **Renkli Görselleştirme** - Her duygu türü için renk kodlanmış gösterim
- 📊 **İstatistikler Dashboard** - Tüm notlarınızın duygu dağılımını görüntüle
- 🌍 **Çok Dil Desteği** - Türkçe ve İngilizce metinler desteklenir
- 🚀 **Hızlı Yanıt Süresi** - GPU hızlandırması ile anlık analiz

## 🏗️ Teknoloji Stack

### Backend
- **Python 3.13** - Programming language
- **Flask 3.1.3** - Web framework
- **Transformers 5.8.0** - NLP modeli (Hugging Face)
- **PyTorch 2.11.0** - Deep Learning framework
- **XLM-RoBERTa** - Multilingual BERT modeli (fine-tuned)

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool & dev server
- **Axios** - HTTP client
- **CSS3** - Modern styling

## 📋 Kurulum

### Gereksinimler
- Python 3.13+
- Node.js 18+
- GPU (opsiyonel, ama tavsiye edilir - CPU'da yavaş olabilir)
- ~4 GB disk alanı (model dosyaları)

### 1️⃣ Backend Setup

```bash
cd backend

# Virtual environment oluştur
python -m venv venv

# Virtual environment'ı aktifleştir
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Gereksinimleri yükle
pip install -r requirements.txt

# Server'ı başlat (model otomatik yüklenir)
python app.py
```

Server `http://localhost:5000` adresinde çalışacak.

### 2️⃣ Frontend Setup

```bash
cd frontend

# Bağımlılıkları yükle
npm install

# Development sunucusunu başlat
npm run dev
```

Uygulama `http://localhost:5173` adresinde açılacak.

## 🚀 Kullanım

1. Frontend'i aç: `http://localhost:5173`
2. Not kutusuna bir metin yaz (max 1024 karakter)
3. "Analyze" butonuna tıkla
4. Duygu analizi sonucunu gör:
   - 😔 **Negative** - Olumsuz duygu (confidence: 95.2%)
   - 😐 **Neutral** - Yansız/nötr metin (confidence: 84.0%)
   - 😊 **Positive** - Olumlu duygu (confidence: 100%)

### Örnek Notlar

```
"Bugün çok güzel bir gün geçirdim" → Positive (92% confidence)
"İşler biraz karışık" → Neutral (80% confidence)
"Hayal kırıklığı yaşadım" → Negative (85% confidence)
```

## 🏛️ Proje Yapısı

```
sentiment-note-app/
├── backend/
│   ├── app.py                    # Flask backend & API
│   ├── fine_tune.py              # Model eğitim script'i
│   ├── prepare_data.py           # Veri hazırlama
│   ├── gpu_check.py              # GPU kontrol
│   ├── fine_tuned_model/         # Eğitilmiş model (saved)
│   ├── data/
│   │   ├── sentiment_data.csv    # Tüm veri (419 örnek)
│   │   ├── train.csv             # Eğitim seti (293 örnek)
│   │   ├── validation.csv        # Doğrulama seti (62 örnek)
│   │   └── test.csv              # Test seti (64 örnek)
│   ├── requirements.txt           # Python bağımlılıkları
│   ├── .env                       # Ortam değişkenleri
│   └── .env.example               # Örnek env dosyası
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                # Ana bileşen
│   │   ├── main.jsx               # Entry point
│   │   ├── components/
│   │   │   ├── Dashboard.jsx      # İstatistik dashboard
│   │   │   ├── NoteForm.jsx       # Not yazma formu
│   │   │   └── NoteList.jsx       # Notlar listesi
│   │   └── styles/
│   │       ├── Dashboard.css
│   │       ├── NoteForm.css
│   │       └── NoteList.css
│   ├── package.json
│   ├── vite.config.js
│   └── .env.example               # Örnek env dosyası
│
└── README.md
```

## 🧠 Model Detayları

### Mimari
- **Base Model**: `xlm-roberta-base` (125M parametreler)
- **Model Type**: Transformer-based sequence classification
- **Languages**: Turkish + English support

### Fine-tuning Veri Seti
- **Toplam Örnek**: 419 (dengeli)
  - Negatif: 139 (33.2%)
  - Tarafsız: 155 (37.0%)
  - Pozitif: 125 (29.8%)

### Eğitim Parametreleri
- **Epoch**: 15
- **Batch Size**: 4 (gradient accumulation: 4)
- **Effective Batch**: 16
- **Learning Rate**: 1e-5 (adaptive)
- **Warmup Steps**: 200
- **Optimizer**: AdamW with weight decay (0.01)
- **Class Weights**: Dengesiz sınıfları ağırlıklandır

### Test Performansı

| Sınıf | Doğruluk | Test Sayısı |
|-------|----------|------------|
| Negatif | 95.2% | 21 |
| Tarafsız | 84.0% | 25 |
| Pozitif | 100% | 18 |
| **Genel** | **92.2%** | **64** |

## 🔧 API Endpoints

### POST `/api/analyze`
Metni analiz et ve duyguyu belirle.

**Request:**
```json
{
  "text": "Bugün çok güzel bir gün geçirdim"
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

**Hata Response:**
```json
{
  "error": "Text too long (max 1024 chars)"
}
```

### GET `/api/notes`
Tüm notları getir.

**Response:**
```json
[
  {
    "id": 1234567890.123,
    "text": "Bugün çok güzel bir gün geçirdim",
    "sentiment": "positive",
    "score": 0.918,
    "timestamp": "12/5/2026, 14:30:00"
  }
]
```

### GET `/health`
Sunucu durumunu kontrol et.

**Response:**
```json
{
  "status": "ok"
}
```

## 🎓 Öğrenme Hedefleri

Bu proje aşağıdaki konuları kapsamaktadır:

### Frontend Geliştirme
- React bileşen mimarisi (functional components)
- State management with `useState`
- Side effects with `useEffect`
- API entegrasyonu (Axios)
- Error handling ve user feedback
- Responsive CSS design

### Backend Geliştirme
- Flask routing ve REST API design
- CORS ve security considerations
- Error handling ve logging
- Environment variables yönetimi
- Model loading ve inference optimization

### Machine Learning
- Pre-trained model fine-tuning
- Text preprocessing ve tokenization
- Multi-class classification
- Class weights ile imbalanced data handling
- Model evaluation ve metrics
- GPU acceleration

### DevOps & Deployment
- Python virtual environments
- Dependency management (pip)
- Environment configuration (.env)
- Logging best practices

## 📊 Gelecek İyileştirmeler

- [ ] Veritabanı entegrasyonu (SQLite/PostgreSQL)
- [ ] Kullanıcı hesapları ve kimlik doğrulama
- [ ] Not silme ve düzenleme
- [ ] Tarihe göre filtreleme ve arama
- [ ] Export to CSV/JSON
- [ ] Dark mode UI
- [ ] Daha fazla dil desteği
- [ ] Sentiment trend analizi
- [ ] Docker containerization
- [ ] Unit & integration testler
- [ ] CI/CD pipeline (GitHub Actions)

## 🐛 Sorun Giderme

### Model yükleme hatası
```bash
# Logs'ı kontrol et
python backend/app.py 2>&1 | grep -i error

# Model'ü yeniden indir
rm -rf backend/fine_tuned_model
```

### CORS hatası
`.env` dosyasında `ALLOWED_ORIGINS` kontrol et:
```env
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Yavaş yanıt süresi
- GPU'nun kullanılıp kullanılmadığını kontrol et: `python backend/gpu_check.py`
- CPU'da çalışıyorsa yanıt süresi 1-2 saniye arasında olabilir
- CUDA yüklü GPU varsa önemli ölçüde hızlanır

### PORT zaten kullanılıyor
```bash
# Backend port değiştir: app.py içinde 5000 yerine başka port ayarla
# Frontend port değiştir: npm run dev -- --port 3000
```

## 📚 Yararlı Kaynaklar

- [Hugging Face Transformers Docs](https://huggingface.co/transformers/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [XLM-RoBERTa Model Card](https://huggingface.co/xlm-roberta-base)

## 👤 Geliştirici

**Yusuf Başlı** - 3. Sınıf Bilgisayar Mühendisliği Öğrencisi

## 📝 Lisans

Bu proje eğitim amaçlı olarak geliştirilmiştir. MIT License altında açıktır.

---

**Yapıldığı Tarih**: Mayıs 2026  
**Son Güncelleme**: 12 Mayıs 2026  
**Model Doğruluk**: 92.2% ✅

