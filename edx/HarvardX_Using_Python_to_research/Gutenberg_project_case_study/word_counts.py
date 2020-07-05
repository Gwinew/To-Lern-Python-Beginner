

def count_words(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts. Skip punctuation.
    """
    text = text.lower()
    skip = ['.', ',', ';', ':', '"', "'"]
    for ch in skip:
        text = text.replace(ch, "")

    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

from collections import Counter

def count_words_fast(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts. Skip punctuation.
    """
    text = text.lower()
    skip = ['.', ',', ';', ':', '"', "'"]
    for ch in skip:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    return word_counts
