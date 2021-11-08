"""
This module contains methods to create text summaries
"""


from collections import Counter
from heapq import nlargest
from string import punctuation

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from utils.service_constants import SPACY_ENGLISH_MODEL


def summarize_text(doc: str) -> str:
    """
    Summarizes text
    :param doc: Doc to be summarized
    :return: Summarized doc
    """
    nlp = spacy.load(SPACY_ENGLISH_MODEL)
    doc = nlp(doc)

    keyword = []
    stopwords = list(STOP_WORDS)
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    for token in doc:
        if token.text in stopwords or token.text in punctuation:
            continue
        if token.pos_ in pos_tag:
            keyword.append(token.text)

    freq_word = Counter(keyword)
    max_freq = Counter(keyword).most_common(1)[0][1]
    for word in freq_word.keys():
        freq_word[word] = (freq_word[word] / max_freq)

    sent_strength = {}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent] += freq_word[word.text]
                else:
                    sent_strength[sent] = freq_word[word.text]

    summarized_sentences = nlargest(5, sent_strength, key=sent_strength.get)
    final_sentences = [w.text for w in summarized_sentences]
    return ' '.join(final_sentences)
