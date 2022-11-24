# https://www.gnu.org/software/make/manual/make.html
SHELL=bash

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: poetry-export
poetry-export:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: create-config
create-config:
	poetry run python .goblet/create_config.py
