## 🧠 Mental Health Journal (Backend with Machine Learning)

A **Django REST Framework** backend for a Mental Health Journal web application.  
This app helps users log daily thoughts, track moods, set reminders, and analyze emotional trends using integrated **Machine Learning (ML)** features like sentiment analysis.  
Designed to be paired with a frontend (e.g., React + Ant Design), but can also be tested directly with **Postman, Insomnia, or Thunder Client**.

---

### 🚀 Features
- **User Authentication** (JWT) – register, login, token refresh
- **Journal Entries**
  - Create / read / update / delete (CRUD)
  - **Automatic sentiment analysis + mood classification** (ML)
  - Tags & categories support
- **Reminders**
  - Daily/weekly reminders with time settings
- **ML Features**
  - Sentiment analysis (TextBlob)
  - Mood scoring (positive/neutral/negative)
  - Emotion trend detection (across entries)
  - Planned: Transformer-based emotion detection (e.g., BERT)
- **Admin Panel** (Django Admin)
- **Secure API** – scoped to each logged-in user
- **CORS Support** – ready for frontend integration

---

## 🧠 ML Features in Detail
The backend currently integrates **TextBlob** for sentiment analysis:
- **Sentiment polarity** → ranges from -1 (negative) to +1 (positive)
- **Automatic mood labels** → `Positive`, `Neutral`, or `Negative`
- **Trend detection** → User mood patterns over time
