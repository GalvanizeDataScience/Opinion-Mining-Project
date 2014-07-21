### TO-DO LIST

* [DONE] Write tests for the `extract_aspects` functions and make sure everything runs as expected.
* [DONE] Write sample for `extract_aspects`
* [DONE]Sketch out `score_aspect` functions. 
	* [DONE-but minimal]Get a sentence-level sentiment analysis model going. 
	* Write `test_score_aspect` tests. 
* Refactor code in `get_sentences_by_aspect` (in `score_aspect` file) and code in `extract_aspects` (in `main` file) ==> redundancy here. 
* `main.py` now runs, but seems to be buggy (all aspect scores are 0.0). Write tests in order to figure out where the bug is. 


Broader features to add/prioritize:
-----------------
* Improve sentiment analysis
	* Demonstrate ML chops
	* Need to do some manual tagging?
* Improve opinion sentence identification (part of aspect extraction).  

Today:

1. [DONE] Write `test_score_aspect` tests. 
	* [DONE] ensure that `main.py` works. 
2. [NOW] Get improved sentiment analysis going: 
	* Incorporate several lexicon-based 	featurizers.
	* train/evaluate on movie review 		dataset.  
	
**NOTE TO SELF**: Change `get_sentences(review)` function to `get_opinionated_sentences(review)`==> implement filtering at this step. 