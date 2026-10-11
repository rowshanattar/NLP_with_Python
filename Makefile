install:
	python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
	python -m textblob.download_corpora
	python -m nltk.downloader punkt_tab averaged_perceptron_tagger_eng

test:
	python -m pytest -vv test_*.py

lint:
	pylint --disable=R,C *.py

format:
	black *.py nlplogic

all: install test lint format

