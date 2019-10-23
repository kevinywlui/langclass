LANGS=Python Java C JavaScript Ruby C++ Haskell Go
.PHONY: fixer data data_external

data_external:
	git submodule init
	git submodule update

data: data_external
	python ./src/data/make_dataset.py $(LANGS)

fixer:
	black src
	isort -rc ./src
