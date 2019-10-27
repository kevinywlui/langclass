LANGS=Python Java C JavaScript Ruby C++ Haskell Go
EXTERNAL_DATA=data/external/RosettaCodeData/
PROCESSED_DATA=data/processed/data.csv
.PHONY: fixer data

$(EXTERNAL_DATA):
	git submodule init
	git submodule update

$(PROCESSED_DATA): $(EXTERNAL_DATA)
	python ./langclass/data/make_dataset.py $(LANGS)

data: $(PROCESSED_DATA)
	

fixer:
	black langclass/
	isort -rc ./langclass

