#!/usr/bin/env python

import csv
from sklearn.base import BaseEstimator

class LexicalScorer(BaseEstimator): 
	"""	
	Class that can be used to score a chunk of tokenized
	text based on sentiment lexicon scores of individual words.
	Also will produce purity rating. 
	"""

	def __init__(self, lex_fname):
		"""
		INPUTS: 

		- lex_fname: string, path to sentiment lexicon CSV

		Reads in the sentiment lexicon lookup file as a dict. 
		"""

		lex_dict = {}

		with open(lex_fname, 'r') as lexfile:
			reader = csv.reader(lexfile, delimiter=',')
			for row in reader: 
				lex_dict[str(row[0])] = int(row[1])

		self.lex_dict = lex_dict

	def get_feature_names(self):
		pass

	def fit():
		pass

	def fit_transform(self):
		pass

	def transform(self):
		pass

