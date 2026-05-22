# ToDo App (FastAPI)

Simple To Do application built with FastAPI. Features:

- User registration and JWT authentication
- Two roles: normal users and admin
- Users can create/delete their own todos
- Users can share todos with other users (search users before sharing)
- Users can search their todos and view paginated lists
- Admins can delete any user and any todo (admins cannot create todos)
- ToDo list responses include a `shared` flag

Quick start

1. Create a virtualenv and activate it.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
uvicorn todo_app.main:app --reload
```

4. Open the interactive docs at `http://127.0.0.1:8000/docs`.

Notes

- The default database is SQLite (`todo.db` in the project root).
- Change `SECRET_KEY` in `todo_app/auth.py` for production.
