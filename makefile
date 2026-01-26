all:

.PHONY: upload

lint:
	black --check *.py

format:
	black *.py

test:
	pytest tests/test_json2qti.py

upload:
	python3 -m build
	python3 -m twine upload dist/*

clean:
	rm -rf dist __pycache__ tests/__pycache__