FROM python:3.10-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml alembic.ini /app/
RUN poetry install --only main

COPY src /app/src

RUN poetry run alembic upgrade head


CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
