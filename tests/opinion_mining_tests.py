from nose.tools import *
import opinion_mining

from opinion_mining.unused import TokenProcessor, NegationSuffixerAdder
from opinion_mining.external.my_potts_tokenizer import MyPottsTokenizer


def setup():
	pass

def teardown():
	pass  

def test_basic():
    print "I RAN!"

def test_negation_tokenizer():
	"""
	Test the negation tokenizer is working.
	"""

	sentence = "The food is not very good. Or is it?"
	tokenizer = MyPottsTokenizer()
	neg_suffer = NegationSuffixerAdder()

	tokenized_sent = tokenizer.tokenize(sentence)
	neg_suffed_sent = neg_suffer.add_negation_suffixes(tokenized_sent)

	assert not neg_suffed_sent[3].endswith("_NEG")
	assert neg_suffed_sent[4].endswith("_NEG")
	assert neg_suffed_sent[5].endswith("_NEG")
	assert not neg_suffed_sent[6].endswith("_NEG")

def test_token_processor(): 
	"""
	Test the token processor
	"""
	sentence = "The food is not very good. Or is it?"
	tokenizer = MyPottsTokenizer()
	tokenized_sent = tokenizer.tokenize(sentence)

	tp = TokenProcessor()
	
	processed_tokens = tp.filter_stop_words(tp.lower_case(tokenized_sent))

	for tok in processed_tokens:
		if tok.isalnum():	
			assert tok.islower()
		assert tok is not ''
		assert tok is not None

	assert 'not' not in tp.STOPWORDS
	assert 'is' not in processed_tokens
	assert 'or' not in processed_tokens



