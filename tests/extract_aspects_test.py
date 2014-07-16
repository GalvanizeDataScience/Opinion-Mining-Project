"""

"""

from nose.tools import raises, with_setup
from opinion_mining.extract_aspects import get_sentences, tokenize, pos_tag

def test_get_sentences(): 
	"""
	Test that the get_sentences method works
	(Sentence tokenization).
	"""

	text = """
	This is a test review. I love the sushi at this place!
	It is really amazing stuff, I swear. I also enjoy the 
	service here. This is a really long and complicated sentence
	just to make sure that this is working. 
	"""

	empty = ""
	null = None

	sentences = get_sentences(text)

	assert sentences[0].strip()=="This is a test review."
	assert len(sentences)==5

@raises(TypeError)
def test_get_sentences_fail(): 
	"""
	Test that get_sentences fails
	when passed None. 
	"""

	get_sentences(None)

def test_tokenize():
	""""
	Tests to make sure that the tokenizer works
	"""
	sentence = "This is a test SENTENCE"
	tokens = tokenize(sentence)

	for tok in tokens:
		assert tok.islower()

	assert len(tokens) == 5
	assert isinstance(tokens, list)

@raises(TypeError)
def test_get_sentences_fail(): 
	"""
	Test that get_sentences fails
	when passed None. 
	"""

	tokenize(None)

def test_pos_tag(): 
	"""
	Test that pos_tag function works
	"""

	sentence = "this is a test sentence"
	tagged = pos_tag(sentence.split())

	assert isinstance(tagged, list)
	assert isinstance(tagged[0], tuple)
	assert isinstance(tagged[0][0], str)
	assert isinstance(tagged[0][1], str)

def test_aspects_from_tagged_sents():
	"""
	Not sure how to test this easily? 
	Is it necessary to write a test? Am I writing 
	too many? 
	"""
	pass




