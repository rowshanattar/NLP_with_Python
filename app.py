from nlplogic import corenlp

phrases = corenlp.get_phrases("Albert Einstein")
print(f"Noun phrases for 'Albert Einstein': {phrases}")