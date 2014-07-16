#!/usr/bin/env python

import re
from potts_tokenizer import Tokenizer

from nltk.corpus import stopwords


class TokenProcessor():
	"""
	Class to handle all of the preprocessing steps on 
	a tokenized document. 
	"""

	# Make NLTK's stopwords list more sentiment-aware
	DELETE = {'should', 'don', 'again', 'not'}
	STOPWORDS = set(stopwords.words('english')).difference(DELETE)

	def __init__(self):
		pass

	def lower_case(self, tokens):
		"""Convert to lower case"""
		return [t.lower() for t in tokens]

	def filter_stop_words(self, tokens):
		"""Remove stop words"""
		return [t for t in tokens if t not in self.STOPWORDS]


class NegationTokenizer():
	"""
	Wrapper for Potts tokenizer that also includes
	support for simple negation marking to aid in
	sentiment analysis. 

	A good explanation of negation marking, along with 
	details of the approximation approach used here can 
	be found at: 

	http://sentiment.christopherpotts.net/lingstruc.html#negation

	As defined in the link above, the basic approach is to 
	"Append a _NEG suffix to every word appearing between a 
	negation and a clause-level punctuation mark". Here, negation
	words are defined as those that match the NEGATIONS regex, and
	clause-level punctuation marks are those that match the PUNCTS regex. 

	Please note that this method is due to Das & Chen (2001) and
	Pang, Lee & Vaithyanathan (2002)
	"""

	# Regex credit: Chris Potts

	# regex to match negation tokens
	NEGATION_RE = re.compile("""(?x)(?:
    ^(?:never|no|nothing|nowhere|noone|none|not|
        havent|hasnt|hadnt|cant|couldnt|shouldnt|
        wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint
	 )$
	)
	|
	n't""")

	# regex to match punctuation tokens
	PUNCT_RE = re.compile("^[.:;!?]$")

	def __init__(self):
		"""
		Initialize Potts tokenizer
		"""

		self.tokenizer = Tokenizer()
		
	def tokenize(self, s):
		"""
		INPUT: string s to be tokenized
		OUTPUT: list of strings (negation tokenized text)

		Do the tokenization (with negation marking).
		"""

		# strip, lowercase, and tokenize
		raw_tokens = self.tokenizer.tokenize(s.strip().lower())

		# negation tokenization
		neg_tokens = []
		append_neg = False # stores whether to add "_NEG"
	
		# logic to decide whether to append "_NEG" suffix
		for token in raw_tokens:
			
			# if we see clause-level punctuation, 
			# stop appending suffix
			if self.PUNCT_RE.match(token):
				append_neg = False

			# Do or do not append suffix, depending
			# on state of 'append_neg'
			if append_neg: 
				neg_tokens.append(token + "_NEG")
			else:
				neg_tokens.append(token)	
			
			# if we see negation word, 
			# start appending suffix
			if self.NEGATION_RE.match(token):
				append_neg = True

		return neg_tokens








