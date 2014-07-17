#!/usr/bin/env python

"""
File that includes various features that have not yet been 
integrated into the main system, but will likely be of use later. 
"""

from __future__ import division
import re
import csv
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


class NegationSuffixerAdder():
	"""
	Class to add simple negation marking to tokenized
	text to aid in sentiment analysis. 

	A good explanation of negation marking, along with 
	details of the approach used here can be found at: 

	http://sentiment.christopherpotts.net/lingstruc.html#negation

	As defined in the link above, the basic approach is to 
	"Append a _NEG suffix to every word appearing between a 
	negation and a clause-level punctuation mark". Here, negation
	words are defined as those that match the NEGATION_RE regex, and
	clause-level punctuation marks are those that match the PUNCT_RE regex. 

	Please note that this method is due to Das & Chen (2001) and
	Pang, Lee & Vaithyanathan (2002)

	
	NOTE TO SELF: 
	This is a refactor of NegationTokenizer. Makes more sense as 
	a separate object, so that can decouple the tokenization
	process from the negation suffix addition process. 
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
		pass

	def add_negation_suffixes(self, tokens):
		"""
		INPUT: List of strings (tokenized sentence)
		OUTPUT: List of string with negation suffixes added

		Adds negation markings to a tokenized string. 
		"""

		# negation tokenization
		neg_tokens = []
		append_neg = False # stores whether to add "_NEG"
		
		for token in tokens:
			
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

class LiuFeaturizer():
	"""
	Class for scoring sentences using Bing Liu's Opinion Lexicon. 

	Source:

	Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
       Proceedings of the ACM SIGKDD International Conference on Knowledge 
       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
       Washington, USA,

    Download lexicon at: http://www.cs.uic.edu/~liub/FBS/opinion-lexicon-English.rar
	"""

	PATH_TO_LEXICONS = "/Users/jeff/Zipfian/opinion-mining/data/Lexicons"

	def __init__(self):
		"""
		Read in the lexicons. 
		"""

		pos_path = self.PATH_TO_LEXICONS + "/Liu/positive-words.txt"
		neg_path = self.PATH_TO_LEXICONS + "/Liu/negative-words.txt"

		self.pos_lex = self.read_lexicon(pos_path)
		self.neg_lex = self.read_lexicon(neg_path)


	def read_lexicon(self, path):
		'''
		INPUT: LiuFeaturizer, string (path)
		OUTPUT: set of strings

		Takes path to Liu lexicon and 
		returns set containing the full 
		content of the lexicon. 
		'''

		start_read = False
		lexicon = set() # set for quick look-up

		with open(path, 'r') as f: 
			for line in f: 
				if start_read:
					lexicon.add(line.strip())
				if line.strip() == "":
					start_read = True
		return lexicon

	def featurize(self, tokens):
		'''
		INPUT: list of strings
		OUTPUT: 

		Note: tokens should be a list of 
		lower-case string tokens, possibly
		including negation markings. 
		'''

		features = {}

		doc_len = len(tokens)
		assert doc_len > 0, "Can't featureize document with no tokens." 

		num_pos = sum([1 if tok in self.pos_lex else 0 for tok in tokens])
		num_neg = sum([1 if tok in self.neg_lex else 0 for tok in tokens])

		features['liu_pos'] = num_pos/doc_len
		features['liu_neg'] = num_neg/doc_len

		return features






