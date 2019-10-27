LANGS=Python Java C JavaScript Ruby C++ Haskell Go
EXTERNAL_DATA=data/external/RosettaCodeData/
PROCESSED_DATA=data/processed/data.csv
MODEL=models/vecparams_model.pkl
.PHONY: fixer data

$(EXTERNAL_DATA):
	git submodule init
	git submodule update

$(PROCESSED_DATA): $(EXTERNAL_DATA)
	python ./langclass/data/make_dataset.py $(LANGS)

$(MODEL): data
	python -m langclass.models.train_model

data: $(PROCESSED_DATA)

train: $(MODEL)

fixer:
	black langclass/
	isort -rc ./langclass

