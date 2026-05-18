# FastAPI College Management API

A scalable and modular College Management API built with FastAPI, SQLAlchemy, and SQLite.

## Project Structure

```
Fastapi_basics/
├── .venv/                  # Virtual environment
├── .gitignore              # Git ignored files
├── sql_app.db              # SQLite Database (auto-created on run)
└── app/
    ├── __init__.py
    ├── main.py             # Application entry point
    ├── database.py         # SQLAlchemy config & connection
    ├── models/             # Database models
    │   ├── __init__.py
    │   ├── student.py
    │   └── course.py
    ├── schemas/            # Pydantic schemas for data validation
    │   ├── __init__.py
    │   ├── student.py
    │   └── course.py
    ├── services/           # Business logic and DB operations (CRUD)
    │   ├── __init__.py
    │   ├── student.py
    │   └── course.py
    └── api/                # API routers/endpoints
        ├── __init__.py
        ├── students.py
        └── courses.py
```

## Setup Instructions

1. **Activate the Virtual Environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

2. **Install Dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic[email]
   ```

3. **Run the Application**
   ```bash
   fastapi dev app/main.py
   ```

4. **Access the API Documentation**
   Open your browser and navigate to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
