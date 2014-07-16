from nltk.corpus import stopwords

from lexicon_featurizers import LiuFeaturizer 
from preprocessing import NegationTokenizer


def filter_stop_words(tokens):

	stopwords = set(stopwords.words('english'))

	return filter(lambda tok: tok not in stopwords, tokens)


if __name__ == "__main__":

	lf = LiuFeaturizer()
	nt = NegationTokenizer()

