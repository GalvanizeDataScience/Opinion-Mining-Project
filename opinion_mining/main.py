import pandas as pd


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


def score_aspect(reviews, aspects):
	"""
	INPUT: list of reviews, list of aspects
	OUTPUT: score of aspect on given set of reviews
	
	For a set of reviews and corresponding aspects, 
	return the score of the aspect on the reviews
	"""
	# return score of the aspect in the set of reviews
	pass


def aspect_opinions(reviews):
	"""
	INPUT: a set of reviews
	OUTPUT: dictionary with aspects as keys and values as scores
	"""

	aspects = extract_aspects(reviews)
	return dict([(aspect, score_aspect(aspect)) for aspect in aspects])


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

		reviews = get_reviews_for_business(business)
		score[business] = aspect_opinions(reviews)


def demo_aspect_extraction(): 
	"""
	Demos the aspect extraction component. 
	"""

	TEST_BIZ_ID = 's1dex3Z3QoqiK7V-zXUgAw'

	print "Reading data..."
	df = read_data()
	print "Done."

	BIZ_NAME = str(df[df.business_id==TEST_BIZ_ID]['name'].iloc[0])


	print "Getting reviews for %s (ID = %s)" % (BIZ_NAME, TEST_BIZ_ID)
	reviews = get_reviews_for_business(TEST_BIZ_ID, df)
	print "Done."

	print "Extracting aspects..."
	aspects = extract_aspects(reviews)
	print "Done."

	print "==========="
	print "Aspects for %s:" % BIZ_NAME
	for i,aspect in enumerate(aspects):
		print str(i) + ". " + aspect


if __name__ == "__main__":
	#main()
	demo_aspect_extraction()
	








