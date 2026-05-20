# FastAPI Auth + RBAC Example

This small example demonstrates JWT authentication and role-based access control (RBAC) implemented with FastAPI.

Repository structure:

- app/core: configuration and JWT/password helpers
- app/models: simple Pydantic user models
- app/schemas: request/response schemas
- app/services: service-layer logic (user store, auth)
- app/routers: API endpoints (auth, student, admin)

Prerequisites:

- Python 3.8+

Install:

```
pip install -r requirements.txt
```

Run (development):

```
uvicorn app.main:app --reload
```

API endpoints (examples):

- Register user

	POST /auth/register
	JSON body:
	```
	{ "username": "alice", "password": "secret", "role": "student" }
	```

- Login

	POST /auth/login
	JSON body:
	```
	{ "username": "alice", "password": "secret" }
	```
	Response:
	```
	{ "access_token": "<jwt>", "token_type": "bearer" }
	```

- Protected routes

	Use header:
	```
	Authorization: Bearer <access_token>
	```

	- GET /students/me — any authenticated user
	- GET /students/only-students — only users with role `student`
	- GET /admin/dashboard — only users with role `admin`

Environment:

- Copy `.env.example` (not included) or set `SECRET_KEY` in environment variables. The default in `app/core/config.py` is for development only — replace it with a secure random key in production.

Notes:

- The example uses an in-memory user store in `app/services/user_service.py`. Swap to a database (e.g., SQLAlchemy + SQLite/Postgres) for persistence.
- Passwords are hashed with `bcrypt` via `passlib`.
- Tokens include `sub` (username) and `role` claims.

Files of interest: app/core/security.py, app/services/*, app/routers/*

