# Makefile

VENV_NAME=env

$(VENV_NAME):
	python3 -m venv $(VENV_NAME)

activate: $(VENV_NAME)
	source $(VENV_NAME)/bin/activate

install: activate
	pip install -r requirements.txt

run: install
	python main.py

clean:
	rm -rf $(VENV_NAME)

.PHONY: install run clean