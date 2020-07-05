import os
import pandas as pd
import numpy as np
from collections import Counter


def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

def fraquency(n):
    if n>10:
        return "frequent"
    elif 1< n<=10:
        return 'infrequent'
    else:
        return 'unique'

def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })

    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"

    data["length"] = data["word"].apply(len)

    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })

    return(sub_data)

"""
filename = 'hamlets.csv'

with open(filename, 'r') as f:
    hamlets = pd.read_csv(f, index_col = 0)

language, text = hamlets.iloc[0]
counted_text = count_words_fast(text)
data = pd.DataFrame(columns= ("word", "count", "length", "fraquency"))
title_num = 1
for i in counted_text.keys():
    data.loc[title_num] = i, counted_text[i], len(i), fraquency(counted_text[i])
    title_num += 1
#print(len(data[data.fraquency=='unique'].fraquency))

sub_data = pd.DataFrame(columns =('language', 'fraquency', 'mean_word_length', 'num_words'))
title_num = 1
list_of_fraq = ["frequent", 'infrequent', 'unique']
for i in list_of_fraq:
    sub_data.loc[title_num] = language, i, sum(data[data.fraquency==i].length)/len(data[data.fraquency==i].fraquency), len(data[data.fraquency==i].fraquency)
    title_num += 1
print(sub_data)
"""

filename = 'hamlets.csv'

with open(filename, 'r') as f:
    hamlets = pd.read_csv(f, index_col = 0)

grouped_data = pd.DataFrame(columns = (
    "language",
    "frequency",
    "mean_word_length",
    "num_words"
))

for i in range(len(hamlets)):
    language, text = hamlets.iloc[i]
    grouped_data = grouped_data.append(summarize_text(language, text))

print(grouped_data)

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
plt.figure(figsize = (10,10))
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
plt.savefig('homework.pdf')
