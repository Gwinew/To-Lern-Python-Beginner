# Docstrings

# Literal strings which document functions, modules and classes.
# They must be the first statement in the blocks for these constructs.

# Sphinx
"""Retrieve and print words from a URL.

Usage:

    python3 words.py <URL>
"""         # After import this module we can use help(docstrings) to see this instruction.

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.

     Args:
         url: The URL of a UTF-8 text document.

     Returns:
         A list of strings containing the words from
         the document.
    """                             # We use this sentence in help(fetch_words) after importing
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words=line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    """Print items one per line.

        Args:
            An iterable series of printable items.
    """
    for item in items:
        print(item)



def main(url):
    """Print each word from a text document from at a URL.

        Args:
            url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])





