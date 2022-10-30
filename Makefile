refactor:
	find telegram_text tests -iname "*.py" | xargs python -m no_optional
	isort telegram_text tests --profile black
lint:
	flake8
	find telegram_text tests -iname "*.py" | xargs pylint
test:
	pytest --cov=telegram_text tests/
html_docs:
	cd docs/ && $(MAKE) clean && $(MAKE) html
