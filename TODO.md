### TO-DO LIST

* [DONE] Write tests for the `extract_aspects` functions and make sure everything runs as expected.
* [DONE] Write sample for `extract_aspects`
* Sketch out `score_aspect` functions. 
	* Get a sentence-level sentiment analysis model going. 
	* Write `test_score_aspect` tests. 
* Refactor code in `get_sentences_by_aspect` (in `score_aspect` file) and code in `extract_aspects` (in `main` file) ==> redundancy here. 
* `main.py` now runs, but seems to be buggy (all aspect scores are 0.0). Write tests in order to figure out where the bug is. 