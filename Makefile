lint:
	flake8
	find . -iname "*.py" -not -path "./.venv/*" | xargs pylint
test:
	pytest --cov=telegram_text tests/
html_docs:
	cd docs/ && $(MAKE) clean && $(MAKE) html
