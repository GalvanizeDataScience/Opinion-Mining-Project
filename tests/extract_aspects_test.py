from nose.tools import raises
from opinion_mining.extract_aspects import get_sentences

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