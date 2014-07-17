from __future__ import division

import pandas as pd
import numpy as np

def get_reviews_for_business(bus_id, df):
	"""
	INPUT: business id, pandas DataFrame
	OUTPUT: Series with only texts
	
	For a given business id, return the review_id and 
	text of all reviews for that business. 
	"""
	return df.text[df.business_id==bus_id]


def extract_aspects(reviews):
	"""
	INPUT: iterable of strings (pd Series, list)
	OUTPUT: list of aspects
	
	Return the aspects from the set of reviews
	"""

	# import the aspect extraction functions
	from extract_aspects import get_sentences, tokenize, pos_tag, aspects_from_tagged_sents

	# put all the sentences in all reviews in one stream
	sentences = []
	for review in reviews: 
		sentences.extend(get_sentences(review))

	# tokenize each sentence
	tokenized_sentences = [tokenize(sentence) for sentence in sentences]

	# pos tag each sentence
	tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]

	# from the pos tagged sentences, get a list of aspects
	aspects = aspects_from_tagged_sents(tagged_sentences)

	return aspects


def score_aspect(reviews, aspect):
	"""
	INPUT: iterable of reviews, iterable of aspects
	OUTPUT: score of aspect on given set of reviews
	
	For a set of reviews and corresponding aspects, 
	return the score of the aspect on the reviews
	"""

	from score_aspect import SentimentScorer, get_sentences_by_aspect

	sentiment_scorer = SentimentScorer()
	aspect_sentences = get_sentences_by_aspect(aspect, reviews)
	scores = [sentiment_scorer.score(sent) for sent in aspect_sentences]
	
	print scores
	return np.mean(scores)


def aspect_opinions(reviews):
	"""
	INPUT: a set of reviews
	OUTPUT: dictionary with aspects as keys and values as scores
	"""

	aspects = extract_aspects(reviews)
	return dict([(aspect, score_aspect(reviews, aspect)) for aspect in aspects])


def read_data():
	"""
	INPUT: None
	OUTPUT: pandas data frame from file
	"""
	return pd.read_csv('/Users/jeff/Zipfian/opinion-mining/data/high_review_restaurants.csv')


def main(): 
	"""
	The true main. 
	"""

	df = read_data()
	score = {}

	for business in businesses: 

		reviews = get_reviews_for_business(business,df)
		score[business] = aspect_opinions(reviews)

if __name__ == "__main__":
	
	df = read_data()
	score = {}

	business = 's1dex3Z3QoqiK7V-zXUgAw'

	reviews = get_reviews_for_business(business,df)
	score[business] = aspect_opinions(reviews)




