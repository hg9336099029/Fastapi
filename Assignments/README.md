Merged assignments (1, 2 and 3)

This project combines:
- Assignment 1: in-memory students, courses, enrollments
- Assignment 2: SQLAlchemy-backed students and courses
- Assignment 3: simple JWT authentication (in-memory users)

Run from the `merged_assignment` folder:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
