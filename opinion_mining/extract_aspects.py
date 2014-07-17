#!/usr/bin/env python

"""
File for aspect extraction functions
"""

import nltk
import sys

from collections import Counter
from nltk.corpus import stopwords

from external.potts_tokenizer import PottsTokenizer

def get_sentences(review):
	"""
	INPUT: full text of a review
	OUTPUT: a list of sentences

	Given the text of a review, return a list of sentences. 
	"""

	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	
	if isinstance(review, str):
		return sent_detector.tokenize(review)
	else: 
		raise TypeError('Sentence tokenizer got type %s, expected string' % type(review))


def tokenize(sentence):
	"""
	INPUT: string (full sentence)
	OUTPUT: list of strings

	Given a sentence in string form, return 
	a tokenized list of lowercased words. 
	"""

	pt = PottsTokenizer(preserve_case=False)
	if isinstance(sentence, str):
		return pt.tokenize(sentence)
	else: 
		raise TypeError('Tokenize got type %s, expected string' % type(sentence))


def pos_tag(toked_sentence):
	"""
	INPUT: list of strings
	OUTPUT: list of tuples

	Given a tokenized sentence, return 
	a list of tuples of form (token, POS)
	where POS is the part of speech of token
	"""
	return nltk.pos_tag(toked_sentence)


def pos_tag_stanford(toked_sentence):
	"""
	INPUT: list of strings
	OUTPUT: list of tuples

	Given a tokenized sentence, return 
	a list of tuples of form (token, POS)
	where POS is the part of speech of token
	"""

	from nltk.tag.stanford import POSTagger
	st = POSTagger('/Users/jeff/Zipfian/opinion-mining/references/resources/stanford-pos/stanford-postagger-2014-06-16/models/english-bidirectional-distsim.tagger', 
               '/Users/jeff/Zipfian/opinion-mining/references/resources/stanford-pos/stanford-postagger-2014-06-16/stanford-postagger.jar')

	return st.tag(toked_sentence)


def aspects_from_tagged_sents(tagged_sentences):
	"""
	INPUT: list of lists of strings
	OUTPUT: list of aspects

	Given a list of tokenized and pos_tagged sentences from reviews
	about a given restaurant, return the most common aspects
	"""

	STOPWORDS = set(stopwords.words('english'))

	# find the most common nouns in the sentences
	noun_counter = Counter()

	for sent in tagged_sentences:
		for word, pos in sent: 
			if pos=='NNP' or pos=='NN' and word not in STOPWORDS:
				noun_counter[word] += 1

	# list of tuples of form (noun, count)
	return [noun for noun, _ in noun_counter.most_common(10)]
		







