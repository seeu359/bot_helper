lint:
	poetry run flake8

sort:
	poetry run isort .

run:
	poetry run bot

test:
	poetry run pytest

build:
	docker-compose up -d --build

migration:
	docker exec helper_bot alembic revision --autogenerate
	docker exec helper_bot alembic upgrade head

restart:
	docker restart helper_bot