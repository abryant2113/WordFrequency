"""
    Script will accept a file as input and will create a bar graph displaying the N most
    frequently used words and how frequently they were used in the file.

"""

import matplotlib.pyplot as plt
import numpy as np

# grabs all of the words from the online article and saves them to a dictionary
word_dict = dict()
word_list = list()

# test lyric file
FILE_NAME = "boogiewonderland.txt"
file = open(FILE_NAME, 'r')

# reads all words from a file and appends them to a list
for line in file:
    for l in line.split():
        word_list.append(l)

# increments the frequency of each of the words in the dictionary
for words in word_list:
    if words.isalpha():
        if word_dict.get(words) is None:
            word_dict[words] = 1
        else:
            word_dict[words] += 1

# creates lists that will be used to store the objects used to populate the bar graph
objects = list()
freq = list()

# sorts the words by frequency and then appends the word and freq to lists
for w in sorted(word_dict, key=word_dict.get, reverse=True):
    if len(objects) > 40:
        break
    elif len(w) > 3:
        objects.append(w)
        freq.append(word_dict[w])

# pyplot bargraph creation
y_pos = np.arange(len(objects))
plt.bar(y_pos, freq, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation='vertical')
plt.ylabel('Word Frequency')
plt.title('Word Frequency in Song')
plt.tight_layout()
plt.show()

