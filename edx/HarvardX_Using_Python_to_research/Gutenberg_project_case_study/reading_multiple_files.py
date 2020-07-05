from word_counts import *
from reading_in_a_book import read_book

def word_stats(word_counts):
    """Return number of unique words and word fraquencies."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

import os
import pandas as pd

book_dir = "./Books"
stats = pd.DataFrame(columns = ('language', 'author', 'title', 'length', 'unique'))
title_num = 1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir +"/" + language):
        for title in os.listdir(book_dir +"/" + language +"/"+ author):
            inputfile = book_dir +"/" + language +"/" +author +"/" + title
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts), num_unique
            title_num += 1


import matplotlib.pyplot as plt

plt.figure(figsize = (10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label='English', color='crimson')

subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label='French', color='forestgreen')

subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label='German', color='orange')

subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label='Portuguese', color='blueviolet')
plt.legend()
plt.xlabel('Book length')
plt.ylabel('Number of unique words')
plt.savefig('lang_plot.pdf')
