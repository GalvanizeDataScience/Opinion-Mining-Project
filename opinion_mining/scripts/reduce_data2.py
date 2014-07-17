"""
This file reads in the following Yelp datasets:

- review data set
- business data set

It then merges the two datasets and retains only Restaurants
that have a large number of reviews. It then writes the resulting
DataFrame to disk for later consumption
"""

import json
import pandas as pd

PATH = '/Users/jeff/Zipfian/opinion-mining/data/yelp_phoenix_academic_dataset_2/'

def read_from_json(fpath):
	"""
	INPUT: string (file path)
	OUTPUT: pandas DataFrame
	"""

	print "Reading data from %s ..." % fpath
	with open(fpath, 'r') as f:
		df = pd.DataFrame([json.loads(r) for r in f.readlines()])

	print "Done."
	return df


if __name__ == "__main__":

	NUM_REVIEW_THRESH = 300 
	OUT_FNAME = '/Users/jeff/Zipfian/opinion-mining/data/high_review_restaurants.csv'

	review_path = PATH + 'yelp_academic_dataset_review.json'
	business_path = PATH + 'yelp_academic_dataset_business.json'

	# read the two data frames
	review_df = read_from_json(review_path)
	business_df = read_from_json(business_path)

	# PROCESS BUSINESS DATA FRAME
	keeps = ['name', 'attributes', 'stars', 'categories', 'review_count', 'business_id']
	business_df = business_df[keeps]

	# clean json
	business_df.categories = business_df.categories.apply(lambda categories: set(categories))

	# keep only restaurants
	restaurants = business_df[business_df.categories.apply(
						lambda categories: 'Restaurants' in categories)].copy()
	del business_df

	# keep only restaurants with many reviews
	high_review_restaurants = restaurants[restaurants.review_count > 300].copy()
	del restaurants

	# rename a column
	high_review_restaurants['overall_stars'] = high_review_restaurants['stars']
	del high_review_restaurants['stars']

	# MERGE THE TWO DATASETS
	merged_reviews = review_df.merge(high_review_restaurants, on='business_id', how='inner')

	#### TESTING ####
	for category_set in merged_reviews.categories:
		assert 'Restaurants' in category_set

	#merged_reviews.categories.apply(lambda x: assert 'Restaurants' in x) #all restaurants
	#################

	# Write to csv
	merged_reviews.to_csv(OUT_FNAME, encoding='utf-8')




