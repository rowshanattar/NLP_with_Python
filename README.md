# NLP_with_Python

A basic NLP project using Python, Wikipedia and TextBlob.

## What it does

Give it a topic, such as a person, place or concept. The tool then:

1. Looks the topic up on Wikipedia and fetches the article summary.
2. Runs the summary through TextBlob, a natural language processing library.
3. Pulls out the **noun phrases** (for example "theoretical physicist", "quantum theory" or "special relativity") and prints them as a list.

This shows quickly what an article is about without reading the whole text.

## Project structure

- `nlplogic/corenlp.py` is the core library. It searches Wikipedia, fetches summaries and extracts noun phrases.
- `cli.py` is a command-line tool built with Python Fire. It takes any topic as an argument.
- `app.py` is a small example script that prints the noun phrases for "Albert Einstein".
- `requirements.txt` lists the Python packages the project needs.
- `Makefile` holds shortcuts for installing, testing, linting and formatting.

## Requirements

- Python 3.10 or newer
- An internet connection, because the tool queries Wikipedia

## Setup

Clone the repository and go into the project folder:

```bash
git clone https://github.com/rowshanattar/NLP_with_Python.git
cd NLP_with_Python
```

Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
```

Install the dependencies and the TextBlob language data:

```bash
make install
```

If `make` isn't available, run these instead:

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

## Usage

Get the noun phrases for any topic from the command line:

```bash
python cli.py "Albert Einstein"
python cli.py "Machine learning"
```

On macOS and Linux you can also run the tool directly:

```bash
chmod +x cli.py
./cli.py "Berlin"
```

Show the built-in help:

```bash
python cli.py --help
```

Run the example script:

```bash
python app.py
```

## Development commands

| Command       | What it does                                 |
|---------------|----------------------------------------------|
| `make install`| Installs dependencies and TextBlob corpora    |
| `make test`   | Runs the tests with pytest                    |
| `make debug`  | Checks the code for errors with pylint        |
| `make format` | Formats the code with black                   |
| `make all`    | Runs all of the above in order               |

## License

MIT. See [LICENSE](LICENSE).
