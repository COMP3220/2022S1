# Assignment 1 - Python for Text Processing

*Submission deadline: Friday 11th March 2022, 5pm.*

*Assessment weight: 10% of the total unit assessment.*

*Late submissions will not be accepted without an approved Special Consideration request via ask.mq.edu.au. For details, see https://students.mq.edu.au/study/assessment-exams/special-consideration.  Assessments submitted after the due date will receive a mark of **zero**.*

## Objectives of this assignment

In this assignment you will practice with the use of Python for text processing. The assignment consists of 5 independent tasks, each of which is worth 2 marks.

**The deadline of this assignment is before census date, so that it can serve as a diagnostic test and you can determine whether you want to remain in the unit or to withdraw without academic penalty.**

You are provided with a template that contains the definitions of the functions that you need to implement in each of the tasks below. The template includes simple [Python doctests](https://docs.python.org/3/library/doctest.html) that you can use to check the correctness of the code. These tests are there to help you, but note that we will use the [unittest framework](https://docs.python.org/3/library/unittest.html) with a separate set of tests when we assess your submission. It is your responsibility to run your own tests, in addition to the doctests provided.

Each function will process a document from the NLTK Gutenberg corpus. This document is specified as an input argument to the function.

## The Tasks (2 marks each)

### 1. Count words with a specific part of speech

Implement a function `count_pos` that returns the number of occurrences of words with a given part of speech. To find the part of speech, use NLTK's "Universal" tag set. To find the words of the document, use NLTK's sent_tokenize and word_tokenize.


The input arguments of the function are:

* *document*: The name of the Gutenberg document, e.g. `"austen-emma.txt"`.
* *pos*: The part of speech.

To produce the correct results, the function must do this:

* Use the NLTK libraries to find the tokens and the stems. 
* Use NLTK's sentence tokeniser before NLTK's word tokeniser.
* Use NLTK's part of speech tagger, using the "Universal" tagset.
* Use NLTK's `pos_tag_sents` instead of `pos_tag`.

### 2. Find the top stem bigrams

Implement a function `get_top_stem_bigrams` that returns the n most frequent bigrams of stems. You must return the list sorted in descending order of frequency.

The input arguments are:

* *document*: The name of the Gutenberg document, e.g. `"austen-emma.txt"`.
* *n*: The number of bigrams to return.

To produce the correct results, the function must do this:

* Use the NLTK libraries to find the tokens and the stems. 
* Use NLTK's sentence tokeniser before NLTK's word tokeniser.
* Use NLTK's Porter stemmer.
* When computing bigrams, do not consider words that are in different sentences. For example, if we have this text: "Sentence 1. And sentence 2." the bigrams are: `('Sentence','1'), ('1','.'), ('And','sentence'), ('sentence','2'), ('2','.')`. Note that the following would not be a valid bigram, since the punctuation mark and the word "And" are in different sentences: `('.','And')`.

### 3. Find words with the same stem

Implement a function `get_same_stem` that returns the list of words that have the same stem as the word given, and their frequencies. The resulting list must be sorted alphabetically. The input arguments of the function are:

* *document*: The name of the Gutenberg document, e.g. `"austen-emma.txt"`.
* *word*: The word.

To produce the correct results, the function must do this:

* First do sentence tokenisation, then word tokenisation.
* Use NLTK's Porter stemmer.

### 4. Get the most frequent word after a given part of speech.

Implement a function `most_frequent_after_pos` that returns the most frequent word after a given part of speech, and its frequency. Do not consider words that occur in the next sentence after the given part of speech. The input arguments are:

* *document*: The name of the Gutenberg document, e.g. `"austen-emma.txt"`.
* *n*: The number of words to return.

To produce the correct results, the function must do this:

* Use the NLTK libraries to find the tokens and the stems. 
* Use NLTK's sentence tokeniser before NLTK's word tokeniser.
* Use NLTK's part of speech tagger, using the "Universal" tagset.
* Use NLTK's `pos_tag_sents` instead of `pos_tag`.
* Do not consider words that occur in the next sentence after the given part of speech. For example if we have the sentences "Sentence 1. And sentence 2.", the word "And" should not be included in the counts of words following the full stop "."

### 5. Get the tf.idf of the words given in the text.

Implement a function `get_word_tfidf` that returns the tf.idf of each of the words that appear in the given text. If a word does not have tf.idf information or is zero, then do not return its tf.idf. The reference for computing tf.idf is the list of documents from the NLTK Gutenberg corpus. To compute the tf.idf, use sklearn's TfidfVectorizer with the option to remove the English stop words (stop_words='english'). The result must be a list of words sorted in alphabetical order, together with their tf.idf. The input arguments are:

* *text*: a string. Note that, for this function, the input argument is not the name of a Gutenberg document.

To produce correct results, the function must do this:

* Use Scikit-learn's `TfidfVectorizer` with the option `stop_words='english'`.
* Fit the tfidf vectorizer using the documents of the NLTK Gutenberg corpus.
* Return the words from the resulting vector of tf.idf values whose value is not zero.
* Sort the results by alphabetical order.
* Each element of the list returned is a tuple that contains the word, and its tf.idf value.


## Submission

The submission must be a single Python file. Do not submit several files or a zip file since the automarker would not know what to do with your submission. Do not submit a Jupyter notebook.

Note that the deadline is a hard deadline. Late submissions will not be accepted without an approved Special Consideration request via ask.mq.edu.au. For details, see https://students.mq.edu.au/study/assessment-exams/special-consideration.  Assessments submitted after the due date will receive a mark of **zero**.

Finally, note that **the work submitted should be your own work**. You may be tempted to search the Web for Python implementations of the questions asked in this tutorial. Be aware that:

1. If we find out that your work is copied from the Web or from other submissions, you may face disciplinary action.
2. Often, trying to adapt work from the web may be more difficult than when you try from scratch.
3. The work you find on the web may be wrong or not do exactly what is asked in this assignment.

