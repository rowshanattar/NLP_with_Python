install:
	python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest -vv test_*.py

debug:
	pylint --disable=R,C *.py

format:
	black *.py

all: install test debug format

