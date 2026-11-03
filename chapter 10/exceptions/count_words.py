from pathlib import Path


def count_words(path):
    """Counts how many word have a document"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        #Conta o número de palavas
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has {num_words} words.")
        