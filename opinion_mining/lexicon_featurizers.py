#!/usr/bin/env python

from __future__ import division
import re
import csv

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




# class LexicalScorer(BaseEstimator): 
# 	"""	
# 	Class that can be used to score a chunk of tokenized
# 	text based on sentiment lexicon scores of individual words.
# 	Also will produce purity rating. 
# 	"""

# 	def __init__(self, lex_fname):
# 		"""
# 		INPUTS: 

# 		- lex_fname: string, path to sentiment lexicon CSV

# 		Reads in the sentiment lexicon lookup file as a dict. 
# 		"""

# 		lex_dict = {}

# 		with open(lex_fname, 'r') as lexfile:
# 			reader = csv.reader(lexfile, delimiter=',')
# 			for row in reader: 
# 				lex_dict[str(row[0])] = int(row[1])

# 		self.lex_dict = lex_dict

# 	def get_feature_names(self):
# 		pass

# 	def fit():
# 		pass

# 	def fit_transform(self):
# 		pass

# 	def transform(self):
# 		pass





