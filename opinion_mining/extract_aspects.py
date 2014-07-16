#!/usr/bin/env python

"""
File for aspect extraction functions
"""

import nltk
import sys

from opinion_mining.external.potts_tokenizer import PottsTokenizer

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
	a tokenized list. 
	"""
	pt = PottsTokenizer(preserve_case=False)
	return pt.tokenize(sentence)


def pos_tag(toked_sentence):
	"""
	INPUT: list of strings
	OUTPUT: list of tuples

	Given a tokenized sentence, return 
	a list of tuples of form (token, POS)
	where POS is the part of speech of token
	"""
	return nltk.pos_tag(toked_sentence)


def aspects_from_tagged_sents(tagged_sentences):
	"""
	INPUT: list of lists of strings
	OUTPUT: list of aspects

	Given a list of tokenized and pos_tagged sentences from reviews
	about a given restaurant, return the most common aspects
	"""
	pass


