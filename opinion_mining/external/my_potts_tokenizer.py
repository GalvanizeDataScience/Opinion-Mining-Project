from potts_tokenizer import PottsTokenizer


class MyPottsTokenizer(PottsTokenizer):
	"""
	Class to improve potts tokenizer to handle 
	NoneTypes. 
	"""


	def tokenize(self, s):
		"""
		Override the PottsTokenizer 'tokenize'
		method to ensure it better handles
		incorrect types 
		"""

		if isinstance(s, str):
			return super(MyPottsTokenizer, self).tokenize(s)
		else:
			raise TypeError, "Tokenizer got %s, expected str" % type(s)
