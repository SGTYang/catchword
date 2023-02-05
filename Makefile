install:
		pip install --upgrade pip &&\
				pip install -r requirements.txt

test:
		python -m pytest

format:
		black *.py

lint:
		pylint catchword

all: install lint test