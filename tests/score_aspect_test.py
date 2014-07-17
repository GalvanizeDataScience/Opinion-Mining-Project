"""
Tests for the score_aspect functions
"""

from opinion_mining.score_aspect import UnsupervisedLiu, SentimentScorer, get_sentences_by_aspect

def test_sent_scorer():
	"""
	Class to test the SentimentScorer
	"""

	ss = SentimentScorer()

	tests =[
		"this is a bad test sentence",
		"bad bad bad bad bad",
		"good good good",
	]

	for test in tests:
		score = ss.score(test)
		assert isinstance(score, float)
		assert score >= -1
		assert score <= 1