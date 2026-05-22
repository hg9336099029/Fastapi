Proposed folder structure for the FastAPI project

Top-level
- app/                  # application package
  - main.py             # app startup, router includes
  - database.py
  - middleware/          # request/response logging and exception handlers
    - __init__.py
  - core/
    - config.py
    - security.py
    - pagination.py     # central pagination helper
  - api/                 # standard name for routers
    - auth.py
    - admin.py
  - memory/              # in-memory demo endpoints (was `mem`)
    - routers.py
    - schemas/
    - services/
  - sql_app/
    - api/
    - models/
    - schemas/
    - services/

Why this structure
- Keep cross-cutting concerns (middleware, exceptions, pagination) in `app/` so they are easy to register from `main.py`.
- `core/` holds small reusable utilities (security, config, helpers).
- `routers/` groups API surface per role or logical area.

Notes
 - Admin-only paginated endpoints live in `app/api/admin.py` and use `app/core/pagination.py`.
 - In-memory demo endpoints live in `app/memory/` (previously `app/mem/`).
 - Middleware and exceptions are registered from `app/main.py` through the `register_` functions.
