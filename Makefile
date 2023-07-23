-include .env
export

app.run:
	@poetry run uvicorn src.main:app --reload

db.run:
	@docker-compose up -d db

db.makemigrations:
	@poetry run alembic revision --autogenerate -m "${message}"

db.migrate:
	@poetry run alembic upgrade head