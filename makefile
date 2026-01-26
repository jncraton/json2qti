all:

.PHONY: upload

lint:
	pipx run --spec black==26.1.0 black --check *.py

test:
	pytest tests/test_json2qti.py

upload:
	python3 -m build
	python3 -m twine upload dist/*

clean:
	rm -rf dist __pycache__ tests/__pycache__