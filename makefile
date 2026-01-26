all:

.PHONY: upload

test:
	pytest test_json2qti.py

upload:
	python3 -m build
	python3 -m twine upload dist/*

clean:
	rm -rf dist