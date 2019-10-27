LANGS=Python Java C JavaScript Ruby C++ Haskell Go
EXTERNAL_DATA=data/external/RosettaCodeData/README.md
PROCESSED_DATA=data/processed/data.csv
MODEL=models/vecparams_model.pkl

.PHONY: fixer data train web-develop web-deploy clean-data

$(EXTERNAL_DATA):
	git submodule init
	git submodule update

$(PROCESSED_DATA): $(EXTERNAL_DATA)
	pipenv run python ./langclass/data/make_dataset.py $(LANGS)

$(MODEL): $(PROCESSED_DATA)
	pipenv run python -m langclass.models.train_model

data: $(PROCESSED_DATA)

train: $(MODEL)

fixer:
	black langclass/
	isort -rc ./langclass

web-develop:
	pipenv run python web/app.py

web-deploy:
	pipenv run python web/app.py deploy

clean-data:
	rm -rf data/external/*
	rm -rf data/processed
