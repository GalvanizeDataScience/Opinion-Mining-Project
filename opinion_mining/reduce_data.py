"""
Script for building reduced dataset. 
"""

import json
import pandas as pd

# location of the review data
IN_FNAME = '/Users/jeff/Zipfian/opinion-mining/data/yelp_phoenix_academic_dataset_2/yelp_academic_dataset_review.json'
OUT_FNAME = '/Users/jeff/Zipfian/opinion-mining/data/reduced_data.csv'
NUM_REVIEW_THRESH = 100 

print "Reading data from %s" % IN_FNAME
with open(IN_FNAME, 'r') as f:
    raw = f.readlines()

# process the data
reviews = [json.loads(r) for r in raw]
reviews_df = pd.DataFrame(reviews)
del reviews

# set of businesses with at least 100 reviews in the dset
print "Reducing data size..."
keep_biz = set(reviews_df.business_id.value_counts().index[
				reviews_df.business_id.value_counts() > NUM_REVIEW_THRESH])

# set of reviews for the businesses in the keep set
keep_df = reviews_df[reviews_df.business_id.apply(lambda x: x in keep_biz)]
del reviews_df

print "Number of businesses remaining: %d" % len(keep_biz)
print "Number of reviews remaining: %d" % len(keep_df)

keep_df.to_csv(OUT_FNAME)
print "Wrote to %s" % OUT_FNAME
