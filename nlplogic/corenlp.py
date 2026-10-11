import wikipedia
from textblob import TextBlob

wikipedia.set_user_agent("MyNLPProject/1.0 (contact)")


def search_wikipedia(query):
    """
    Search Wikipedia for a given query and return the summary of the first result.
    """
    try:
        results = wikipedia.search(query)
        return results
    except Exception as e:
        print(f"An error occurred while searching Wikipedia: {e}")
        return None


def summary_wikipedia(name):
    if name:
        return wikipedia.summary(name)
    return None


def get_text(text):
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    try:
        summary = summary_wikipedia(name)
        if summary:
            blob = get_text(summary)
            return blob.noun_phrases
        else:
            print(f"No summary found for {name}.")
            return []
    except Exception as e:
        print(f"An error occurred while getting phrases: {e}")
        return []
