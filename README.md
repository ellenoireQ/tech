# Technical test

## How to run
## Backend

```bash
# Install dependencies (dari root project)
pip install -e .
pip install -r requirements.txt

# Jalankan server
cd backend
uvicorn main:app --reload
```

Server berjalan di `http://localhost:8000`

---

## Frontend

```bash
cd frontend
npm install
npm run dev
```

App berjalan di `http://localhost:3000`
