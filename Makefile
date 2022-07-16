dev:
	poetry install
	poetry run pre-commit install
	poetry run pre-commit run --all-files

format:
	poetry run isort get_repo tests
	poetry run blue get_repo tests

lint: format
	poetry run flake8 get_repo/* tests/*

test:
	poetry run pytest

security-baseline:
		poetry run bandit -r get_repo

complexity-baseline:
	$(info Maintenability index)
	poetry run radon mi get_repo
	$(info Cyclomatic complexity index)
	poetry run xenon --max-absolute C --max-modules A --max-average A get_repo

patch:
	poetry run bumpver update --patch
