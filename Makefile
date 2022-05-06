lint:
	flake8
	find . -iname "*.py" -not -path "./.venv/*" | xargs pylint
test:
	pytest
