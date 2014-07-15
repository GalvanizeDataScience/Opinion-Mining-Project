try:
	from setuptools import setup 
except ImportError:
	from disutils.core import setup

config = {
	'description': 'Feature-Based Sentiment Analysis on Yelp Reviews',
	'author': 'Jeff Fossett',
	'url': 'URL to get it at.',
	'download_url': 'Where to download.',
	'author_email': 'Fossj117@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['opinion_mining'],
	'scripts': [],
	'name': 'opinion_mining',
}

setup(**config)
