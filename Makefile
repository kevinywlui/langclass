LANGS=Python Java C JavaScript Ruby C++ Haskell Go
.PHONY: fixer data

data:
	python ./src/data/make_dataset.py $(LANGS)

fixer:
	black src
	isort -rc ./src
