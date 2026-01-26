all:

.PHONY: upload

upload:
	python3 -m build
	python3 -m twine upload dist/*
