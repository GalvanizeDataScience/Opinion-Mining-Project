"""
File for aspect scoring functions
"""

from __future__ import division
from external.my_potts_tokenizer import MyPottsTokenizer

class UnsupervisedLiu(): 
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


	def predict(self, tokenized_sent):
		'''
		INPUT: list of strings
		OUTPUT: 

		Note: tokens should be a list of 
		lower-case string tokens, possibly
		including negation markings. 
		'''

		#features = {}

		doc_len = len(tokenized_sent)
		assert doc_len > 0, "Can't featurize document with no tokens." 

		num_pos = sum([1 if tok in self.pos_lex else 0 for tok in tokenized_sent])
		num_neg = sum([1 if tok in self.neg_lex else 0 for tok in tokenized_sent])

		#features['liu_pos'] = num_pos/doc_len
		#features['liu_neg'] = num_neg/doc_len

		score = (num_pos - num_neg)/doc_len		
		return score
		#return 1 if score > 0.5 else 0


class SentimentScorer(): 
	"""
	Class to score the sentiment of a sentence
	(from a pre-trained model). 
	"""

	def __init__(self):
		# unpickle the model
		# self.model = unpickle(model.pickle)
		self.model = UnsupervisedLiu()

	def score(self, sentence):
		"""
		INPUT: SentimentScorer, string or list of strings
		OUTPUT: int in {-1, 0, +1}
		
		Given a sentence (tokenized or not), return a sentiment score
		for it. 
		"""
	
		# SKETCH: 
		
		if isinstance(sentence, str):
			sentence = self.featurize(sentence)
		elif not isinstance(sentence, list):
			raise TypeError, "SentimentScorer.score got %s, expected string or list" % type(sentence)

		score = self.model.predict(sentence)
		return score

	def featurize(self, sentence):
		"""
		INPUT: SentimentScorer, string
		OUTPUT: 

		Given a sentence, return a featurized version
		that can be consumed by the self.model's predict method. 
		"""
		pt = MyPottsTokenizer(preserve_case=False)
		return pt.tokenize(sentence)


def get_sentences_by_aspect(aspect, reviews):
	"""
	INPUT: string (aspect), iterable of strings (full reviews)
	OUTPUT: iterable of strings

	Given an aspect and a list of reviews, return a list 
	sof all sentences that mention that aspect.  
	"""

	# THIS CODE IS TOTALLY COPIED FROM MAIN FILE function 'extract_aspects' 
	# TODO: REFACTOR THIS IN AN INTELLIGENT WAY. 

	from extract_aspects import get_sentences, tokenize, pos_tag, aspects_from_tagged_sents
	
	# get 
	#sentences = []
	#for review in reviews: 
	#	sentences.extend(get_sentences(review))

	# tokenize each sentence
	tokenized_sentences = [tokenize(sentence) for sentence in sentences
							for sentences in get_sentences(review)]

	return [sent for sent in tokenized_sentences if aspect in sent]


def demo_score_aspect():
	"""
	Demo the score aspect functionality
	"""

	ss = SentimentScorer()
	
	pos_sent = "This is a good, positive sentence"
	neg_sent = "This is a bad, negative sentence"

	print "Score for '%s' is %f" % (pos_sent, ss.score(pos_sent))
	print "Score for '%s' is %f" % (neg_sent, ss.score(neg_sent))


if __name__ == "__main__":
	demo_score_aspect()
	




