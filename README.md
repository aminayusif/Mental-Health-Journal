## 🧠 Mental Health Journal (Backend with Machine Learning)

This project is a Mental Health Journal application that consists of a Django backend and a React frontend. The application helps users log daily thoughts, track moods, set reminders, and analyze emotional trends using integrated **Machine Learning (ML)** features like sentiment analysis.  
Designed to be paired with a frontend (e.g., React + Ant Design), but can also be tested directly with **Postman, Insomnia, or Thunder Client**.


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

### 🧠 ML Features in Detail
The backend currently integrates **TextBlob** for sentiment analysis:
- **Sentiment polarity** → ranges from -1 (negative) to +1 (positive)
- **Automatic mood labels** → `Positive`, `Neutral`, or `Negative`
- **Trend detection** → User mood patterns over time


### Project Structure

```
mental-health-journal
├── backend
│   ├── manage.py
│   ├── journal_api
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── journal
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   └── README.md
├── frontend
│   ├── src
│   │   ├── App.js
│   │   ├── components
│   │   │   └── JournalEntry.js
│   │   └── pages
│   │       └── Home.js
│   ├── package.json
│   └── README.md
└── README.md
```

### Backend Setup

1. Navigate to the `backend` directory.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
4. Install the required packages:
   ```
   pip install django djangorestframework
   ```
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install the required packages:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

### Usage

- Access the backend API at `http://localhost:8000/api/`.
- Access the frontend application at `http://localhost:3000/`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.