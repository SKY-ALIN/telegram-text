lint:
	flake8
	find . -iname "*.py" -not -path "./.venv/*" -not -path "./docs/*" | xargs pylint
test:
	pytest --cov=telegram_text tests/
html_docs:
	cd docs/ && $(MAKE) clean && $(MAKE) html
