# MenuMind AI

## Project Structure
```
menumind/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── backend/
    ├── app.py
    └── .env
```

## Setup & Run

### 1. Install dependencies
```bash
pip install flask flask-cors openai python-dotenv
```

### 2. Add your OpenAI key (optional)
Edit `backend/.env`:
```
OPENAI_API_KEY=sk-your-key-here
```
If you skip this, the app runs in demo mode with realistic mock responses.

### 3. Start the Flask backend
```bash
cd backend
python app.py
```
Server runs at `http://127.0.0.1:5000`

### 4. Open the frontend
Open `frontend/index.html` directly in your browser.

You can also paste your API key into the sidebar field at runtime — it overrides the .env key.

## Demo Mode
No API key? No problem. Every button works and returns realistic pre-written responses so the app is fully presentable without a live OpenAI connection.
