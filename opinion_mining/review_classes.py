import nltk

from nltk.tag.stanford import POSTagger
from external.my_potts_tokenizer import MyPottsTokenizer


class ReviewSet(object):
	"""
	Class to store the full corpus of reviews about 
	a particular restaurant and orchestrate restaurant-level
	computations. 

	Calling 'get_aspect_summary' generates the final aspect-based sentiment summary
	for this set of reviews. 

	NOTE: ONE REVIEWSET = ONE RESTAURANT
	"""

	def __init__(self, review_df):
		"""
		INPUT: pandas DataFrame with each row a review, and columns:
			- business_id: id of the business (must be all same)
			- review_id: id of the review
			- stars: number of stars reviewer gave
			- text: raw text of the review
			- user_id: id of the user who made review
			- name: name of the restaurant
			- categories: set of categories for restaurant
			- overall_stars: overall rating of this restaurant
		
		Takes raw DataFrame of reviews about a particular restaurant (where
		each row corresponds to a particular review of the restaurant, and 
			1. Stores all the metadata associated with the restaurant
			2. Converts the reviews (rows) into Review objects. 

		"""

		# Ensure only got data about *one* business
		assert len(review_df.business_id.unique()) == 1, "Must pass data for a single business to ReviewSet"

		# Get/Store restaurant-level info
		self.business_id = str(review_df.business_id.iloc[0]) # string 
		self.business_name = str(review_df.name.iloc[0]) # string
		self.overall_stars = int(review_df.overall_stars.iloc[0]) # int
		#self.categories = self.parse_categories(review_df.categories.iloc[0]) # TODO

		# Create the set of reviews for this restaurant
		self.reviews = [Review(dict(review_row)) for _,review_row in review_df.iterrows()]

	def __iter__(self):
		"""
		INPUT: ReviewSet
		OUTPUT: an iterator over the set of reviews for this restaurant. 
		
		Iterator over reviews in this ReviewSet to allow the use of "for review in ReviewSet"
		"""
		return self.reviews.__iter__()

	def __str__(self):
		"""
		INPUT: ReviewSet
		OUTPUT: string

		Return a string representation of this ReviewSet
		"""
		return self.business_name

	def get_aspect_summary(self):
		"""
		INPUT: ReviewSet
		OUTPUT: dict mapping aspects to dicts with pos/neg keys and lists of pos/neg
		sentences as values. 

		High level method to return the final aspect-based 
		summarization output, to be fed into front-end. 
		"""
		
		aspects = self.extract_aspects()
		return dict([aspect, self.score_aspect(aspect) for aspect in aspects])

	def extract_aspects(self):
		"""
		INPUT: ReviewSet
		OUTPUT: List of strings (aspects)

		Returns a list of the aspects that are 
		most often commented on in this ReviewSet 
		"""
		pass


	def score_aspect(self, aspect):
		"""
		INPUT: ReviewSet, string (aspect)
		OUTPUT: dict with keys 'pos' and 'neg' which 
		map to a list of positive sentences (strings) and
		a list of negative sentences (strings) correspondingly. 
		"""
		pass 



class Review(object):
	"""
	Class to store review-level data. 

	Implements sentence tokenization, and stores metadata 
	about this review (e.g. who was the reviewer, how many 
	stars did they give, etc.)

	Question: should this also store a pointer to its ReviewSet? 
	"""

	# Tokenizer for converting a review to a list of sentences. 
	SENT_TOKENIZER = nltk.data.load('tokenizers/punkt/english.pickle')

	def __init__(self, review_dict):
		"""
		INPUT: dict corresponding to one row of pd DataFrame of reviews (data for one review) 

		- Maps metadata to class attributes. 
		- Converts raw text into a list of sentences w/tokenizer. 
		"""

		self.user_id = review_dict['user_id']
		self.stars = review_dict['stars']
		self.text = review_dict['text']		

		self.sentences = self.sentence_tokenize(self.text)

	def sentence_tokenize(self, review_text):
		"""
		INPUT: String (full raw text of review)
		OUTPUT: List of strings (Individual sentences)

		Convert the raw text of a review to a list of sentences. 
		"""	
		return Review.SENT_TOKENIZER.tokenize(review_text)

	def __iter__(self):
		"""
		INPUT: Review object
		OUTPUT: Iterator over the sentences in this review. 

		Returns an iterator over the sentences in this review. 
		"""
		return self.sentences.__iter__()


class Sentence(object):
	"""
	Class corresponding to a sentence in a review. 
	"""

	# Tokenizer for converting a 
	WORD_TOKENIZER = MyPottsTokenizer(preserve_case=False)
	
	STANFORD_POS_TAGGER = POSTagger(
				'/Users/jeff/Zipfian/opinion-mining/references/resources/stanford-pos/stanford-postagger-2014-06-16/models/english-bidirectional-distsim.tagger', 
	           '/Users/jeff/Zipfian/opinion-mining/references/resources/stanford-pos/stanford-postagger-2014-06-16/stanford-postagger.jar')

	def __init__(self, sent_text):

		self.raw_text = sent_text
		
		self.tokenized_sent = self.word_tokenize(sent_text)
		
		self.pos_sent = self.pos_tag(self.tokenized_sent)
		#self.pos_sent = self.pos_tag_stanford(self.tokenized_sent) #use stanford

	def word_tokenize(self, sent_text):
		"""
		INPUT: Raw text of a sentence
		OUTPUT: List of strings corresponding to words in sentence
		"""

		return Sentence.WORD_TOKENIZER.tokenize(sent_text)

	def pos_tag(self, tokenized_sent):
		"""
		INPUT: List of strings (tokenized sentence)
		OUTPUT: List of tuples of form: (STRING, POS)
		
		Given a tokenized sentence, return 
		a list of tuples of form (token, POS)
		where POS is the part of speech of token using
		the standard NLTK POS tagger. 
		"""

		return nltk.pos_tag(tokenized_sent)

	def pos_tag_stanford(self, tokenized_sent):
		"""
		INPUT: list of strings
		OUTPUT: list of tuples of form: (STRING, STRING)

		Given a tokenized sentence, return 
		a list of tuples of form (token, POS)
		where POS is the part of speech of token using 
		the Stanford POS tagger. 
		"""

		return Sentence.STANFORD_POS_TAGGER.tag(tokenized_sent)

	def __str__(self):
		return self.raw_text


if __name__ == "__main__":
	from main import read_data, get_reviews_for_business

	business = 's1dex3Z3QoqiK7V-zXUgAw'

	df = read_data()
	review_set = ReviewSet(get_reviews_for_business(business,df))

	output = review_set.get_aspect_summary()
	print output





