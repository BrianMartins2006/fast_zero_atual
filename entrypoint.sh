#!/bin/sh

# Aplica as migrações do Alembic
poetry run alembic upgrade head

# Inicia o servidor FastAPI
poetry run uvicorn fast_sero.app:app --host 0.0.0.0 --port 8000
