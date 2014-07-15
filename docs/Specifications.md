
**Sentence Extractor**: Should ingest a block of text and convert it to a list of sentences. 

**Sentiment Lexicon**: Should be a CSV or TSV of form: 

- word_POS, score (+/-)

No header! For example: 

- Good_a (7.73)

POS tags: (adjective = a, aadverb = r, noun = n, verb = v)

**Classification**

Gizven a tokenized string $$$x = (w_1, w_2, …, w_n)$$$ of words, we calssify its sentiment using the following function: 

$$ \text{raw-score}(x) := \Sigma_{i=1}^n s_i$$

Where $$$s_i$$$ is the score terms from the induced lexicon. Use a simple lexical negation detector to reverse the sign of $$$s_i$$$ in cases where it is preceded by negation term like "not".

Specifications: 

- LexicalScorer(BaseEstimator)
	-  init takes pointer to lexicon file in format above








