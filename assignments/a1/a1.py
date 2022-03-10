import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
nltk.download('punkt')
nltk.download('gutenberg')
from sklearn.feature_extraction.text import TfidfVectorizer
import collections

# Task 1 (2 marks)
def count_pos(document, pos):
    """Return the number of occurrences of words with a given part of speech. To find the part of speech, use 
    NLTK's "Universal" tag set. To find the words of the document, use NLTK's sent_tokenize and word_tokenize.
    >>> count_pos('austen-emma.txt', 'NOUN')
    31998
    >>> count_pos('austen-sense.txt', 'VERB')
    25074
    """

    rawf = nltk.corpus.gutenberg.raw(document)
    sentens = [nltk.word_tokenize(s) for s in nltk.sent_tokenize(rawf)]
    tagged = nltk.pos_tag_sents(sentens,tagset="universal")
    pos_c = []
    for sentense in tagged:
        for words in sentense:
            pos_c.append(words[1])
    counter = collections.Counter(pos_c)
    store_c = counter.most_common()
    for r in store_c:
        if r[0]==pos:
            return r[1]
    return 0
    

# Task 2 (2 marks)
def get_top_stem_bigrams(document, n):
    """Return the n most frequent bigrams of stems. Return the list sorted in descending order of frequency.
    The stems of words in different sentences cannot form a bigram. To stem a word, use NLTK's Porter stemmer.
    To find the words of the document, use NLTK's sent_tokenize and word_tokenize.
    >>> get_top_stem_bigrams('austen-emma.txt', 3)
    [(',', 'and'), ('.', "''"), (';', 'and')]
    >>> get_top_stem_bigrams('austen-sense.txt',4)
    [(',', 'and'), ('.', "''"), (';', 'and'), (',', "''")]
    """
    nltk.download('averaged_perceptron_tagger')
    nltk.download('universal_tagset')
    raw = nltk.corpus.gutenberg.raw(document)
    sents = [nltk.word_tokenize(s) for s in nltk.sent_tokenize(raw)]
    stemmer = nltk.PorterStemmer()
    stems = []
    for s in sents:
        for w in s:
            stems.append(stemmer.stem(w))
    bigrams = nltk.bigrams(stems)
    bigrams_counter = collections.Counter(bigrams)
    nbig = []
    for ans in bigrams_counter.most_common(n):
        nbig.append(ans[0])
    
    return nbig



# Task 3 (2 marks)
def get_same_stem(document, word):
    """Return the list of words that have the same stem as the word given, and their frequencies. 
    To find the stem, use NLTK's Porter stemmer. To find the words of the document, use NLTK's 
    sent_tokenize and word_tokenize. The resulting list must be sorted alphabetically.
    >>> get_same_stem('austen-emma.txt','respect')[:5]
    [('Respect', 2), ('respect', 41), ('respectability', 1), ('respectable', 20), ('respectably', 1)]
    >>> get_same_stem('austen-sense.txt','respect')[:5]
    [('respect', 22), ('respectability', 1), ('respectable', 14), ('respectably', 1), ('respected', 3)]
    """
    rawf = nltk.corpus.gutenberg.raw(document)
    sentens = [nltk.word_tokenize(s) for s in nltk.sent_tokenize(rawf)]
    stemmer = nltk.PorterStemmer()
    stem = []
    for sen in sentens:
        for words in sen:
            stemmed = stemmer.stem(words)
            if stemmed==word:
                stem.append(words)

    counter_sort = sorted(collections.Counter(stem).items())
    return counter_sort

# Task 4 (2 marks)
def most_frequent_after_pos(document, pos):
    """Return the most frequent word after a given part of speech, and its frequency. Do not consider words
    that occur in the next sentence after the given part of speech.
    To find the part of speech, use NLTK's "Universal" tagset.
    >>> most_frequent_after_pos('austen-emma.txt','VERB')
    [('not', 1932)]
    >>> most_frequent_after_pos('austen-sense.txt','NOUN')
    [(',', 5310)]
    """
    nltk.download('averaged_perceptron_tagger')
    nltk.download('universal_tagset')
    rawf = nltk.corpus.gutenberg.raw(document)
    sentens = [nltk.word_tokenize(s) for s in nltk.sent_tokenize(rawf)]
    taggeds = nltk.pos_tag_sents(sentens,tagset="universal")
    filtered_pos = []
    for s in taggeds:
        bigrams = nltk.bigrams(s)
        filtered_pos += [w2 for (w1,v1), (w2,v2) in bigrams if v1==pos]
    c = collections.Counter(filtered_pos)
    return c.most_common(1)

# Task 5 (2 marks)
def get_word_tfidf(text):
    """Return the tf.idf of the words given in the text. If a word does not have tf.idf information or is zero, 
    then do not return its tf.idf. The reference for computing tf.idf is the list of documents from the NLTK 
    Gutenberg corpus. To compute the tf.idf, use sklearn's TfidfVectorizer with the option to remove the English 
    stop words (stop_words='english'). The result must be a list of words sorted in alphabetical order, together 
    with their tf.idf.
    >>> get_word_tfidf('Emma is a respectable person')
    [('emma', 0.8310852062844262), ('person', 0.3245184217533661), ('respectable', 0.4516471784898886)]
    >>> get_word_tfidf('Brutus is a honourable person')
    [('brutus', 0.8405129362379974), ('honourable', 0.4310718596448824), ('person', 0.32819971943754456)]
    """
    import pandas as pd
    from nltk.corpus import stopwords
    TfidfVectorizer=TfidfVectorizer(use_idf=True)

    sentences = []
    for i in text.index:
        sentences.append(text.index[i])
    
    tfIdf = TfidfVectorizer.fit_transform(sentences)
  
    return []

# DO NOT MODIFY THE CODE BELOW
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
