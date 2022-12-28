no: # Replace `Optional[T]` with `Union[T, None]`
	find telegram_text -iname "*.py" | xargs python -m no_optional
	find tests -iname "*.py" | xargs python -m no_optional
isort: # Sort import statements
	isort .
lint: # Check code quality
	flake8
	find telegram_text tests -iname "*.py" | xargs pylint
test: # Run tests
	pytest --cov=telegram_text tests/
html_docs: # Build html docs
	cd docs/ && $(MAKE) clean && $(MAKE) html
