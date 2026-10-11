#!/usr/bin/env python3
import fire
from nlplogic import corenlp

if __name__ == "__main__":
    fire.Fire(corenlp.get_phrases)
