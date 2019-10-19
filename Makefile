
.PHONY: fixer

fixer:
	black src
	isort -rc ./src
