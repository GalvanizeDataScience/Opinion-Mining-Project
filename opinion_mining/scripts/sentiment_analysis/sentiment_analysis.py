"""

Script for designing/building/testing my sentiment
analysis model. 

Final model must: 

1. Ingest a raw sentence string
	- Can assume that it is an OPINIONATED sentence
2. Return a value between +1 and -1. 
	- Or would a class be better? 


"""

### READING IN THE DATA ###

def read_rt_data(path):
    with open(path, 'r') as f: 
        raw = f.readlines()
    return raw

PATH_TO_TRAIN_DATA = '/Users/jeff/Zipfian/opinion-mining/data/SentimentTraining/rt-polaritydata/rt-polaritydata'

neg_file = "/rt-polarity.neg"
pos_file = "/rt-polarity.pos"
        
pos_snips = read_rt_data(PATH_TO_TRAIN_DATA + pos_file)
neg_snips = read_rt_data(PATH_TO_TRAIN_DATA + neg_file)

### PUTTING DATA INTO A DATA FRAME ###

def to_data_frame(sent_list, lab): 
    sent_series = pd.Series(sent_list)
    sent_df = pd.DataFrame({'sentence':sent_series})
    sent_df['label'] = lab
    return sent_df

# clean up
pos_snips = map(lambda x: x.strip(), pos_snips)
neg_snips = map(lambda x: x.strip(), neg_snips)

pos_df = to_data_frame(pos_snips, 1)
neg_df = to_data_frame(neg_snips,0)

# combine the two data frames into one
full_df = pos_df.append(neg_df, ignore_index=True)

##### FEATURIZATION ####

# sys.path.append('/Users/jeff/Zipfian/opinion-mining')
from opinion_mining.external.my_potts_tokenizer import MyPottsTokenizer

# List of tokenized sentences
tokenizer = MyPottsTokenizer(preserve_case=False)
tokenized_sentences = [tokenizer.tokenize(sent) for sent in full_df.sentence]

from sentiment_analysis_helpers import NegationSuffixAdder, StopwordFilterer

nsf = NegationSuffixAdder()
sf = StopwordFilterer()

# filter stop words and add negation suffixes
ready_to_featurize_sents = [nsf.add_negation_suffixes(sf.filter_stop_words(tkd_sent)) 
													for tkd_sent in tokenized_sentences]

def featurize(tokenized_sentence, featurizers):
	"""
	INPUT: list of strings (one document), list of featurizers
	OUTPUT: dict of form {'feature_name': feature_value} containing 

	Incoming sentences should be: 
	1. tokenized
	2. lowercased
	3. stopwords removed
	4. negation suffixes added
	"""

	feature_dict = {}

	for featurizer in featurizers:
		
		# get new set of features
		new_features = featurizer.featurize(tokenized_sentence)
		feature_dict = dict(feature_dict.items() + new_features.items())

	return feature_dict

from featurizers import LiuFeaturizer

featurizer_list = [LiuFeaturizer()]
my_features = [featurize(sent, featurizers=featurizer_list) for sent in ready_to_featurize_sents]

my_features_df = pd.DataFrame(my_features)
my_features_array = my_features_df.values # get raw values

target = full_df.label.values

##### MODELING #####

from sklearn.linear_model import LogisticRegression















