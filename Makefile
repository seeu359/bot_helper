lint:
	poetry run flake8

sort:
	poetry run isort .

run:
	poetry run bot

test:
	poetry run pytest