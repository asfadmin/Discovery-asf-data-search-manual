# asf_search Basics

## Overview

asf_search is a Python module for performing searches of the ASF catalog. In addition, it offers baseline functionality and download support. It is available through PyPi and Conda.

	import asf_search as asf

	results = asf.granule_search(['ALPSRS279162400', 'ALPSRS279162200'])
	print(results)

	wkt = 'POLYGON((-135.7 58.2,-136.6 58.1,-135.8 56.9,-134.6 56.1,-134.9 58.0,-135.7 58.2))'
	results = asf.geo_search(platform=[asf.PLATFORM.SENTINEL1], intersectsWith=wkt, maxResults=10)
	print(results)

For an introductory walkthrough of asf_search, see the [Jupyter Notebooks](https://github.com/asfadmin/Discovery-asf_search/tree/master/examples).

## Installation
In order to easily manage dependencies, we recommend using dedicated project environments via [Anaconda/Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) or [Python virtual environments](https://docs.python.org/3/tutorial/venv.html).

asf_search can be installed into a conda environment with

	conda install -c conda-forge asf_search

or into a virtual environment with

	python -m pip install asf_search

## Usage
Programmatically searching for ASF data is made simple with asf_search. Several search functions are provided. Each search function returns an ```ASFSearchResults``` object:

- ```geo_search()``` Find product info over an area of interest using a WKT string
- ```granule_search()``` Find product info using a list of scene names
- ```product_search()``` Find product info using a list of product IDs
- ```stack_from_id()``` Find a baseline stack of products using a reference scene
- If the above search approaches do not meet your search needs, ```search()``` supports all available keywords:
	- ```search()``` Find product info using any combination of search parameters
- Additionally, numerous constants are provided to ease the search process. Currently, we provide constants for beam mode, flight direction, instrument, platform, polarization, and product type. You can see the full [list of constants here](https://github.com/asfadmin/Discovery-asf_search/tree/master/asf_search/constants).

Additionally, asf_search supports downloading data, both from search results as provided by the above search functions, and directly on product URLs. An authenticated session is generally required. More information on available authentication methods can be found [here](https://requests.readthedocs.io/en/latest/user/authentication/). You may also authenticate using an ```ASFSession``` object and one of the following authentication methods. ```ASFSession``` is a subclass of ```Session```.

- ```auth_with_creds('user', 'pass)```
- ```auth_with_token('EDL token')```
- ```auth_with_cookiejar(http.cookiejar)```

If not using .netrc credentials, that session should be passed to whichever download method is being called, can be re-used, and is thread safe.

Example using .netrc:

	results = ....
	results.download(path='....')

Example with manual authentication:

	results = asf_search.granule_search([...])
	session = asf_search.ASFSession().auth_with_creds('user', 'pass')
	results.download(path='/Users/SARGuru/data', session=session)

Alternately, asf_search supports downloading an arbitrary list of URLs. All of the available authentication methods are supported:

	urls = [...]
	asf_search.download_urls(urls=urls, path='/Users/SARGuru/data', session=ASFSession().auth_with_token('EDL token'))

Also note that ```ASFSearchResults.download()``` and the generic ```download_urls()``` function both accept a ```processes``` parameter which allows for parallel downloads.

Further examples of all of the above can be found in this [sample script](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/hello_world.py)