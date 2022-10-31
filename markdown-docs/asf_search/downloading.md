# Downloading

## Session Authentication

asf_search supports downloading data, both from search results as provided by the search functions, and directly on product URLs. An authenticated session is generally required. asf_search uses ```Requests```. Using .netrc credentials is the preferred method for authentication. More information on .netrc authentication can be found [here](https://requests.readthedocs.io/en/latest/user/authentication/#netrc-authentication).

Example using .netrc:

	results = ....
	results.download(path='....')

If not using .netrc credentials, you may authenticate using an ```ASFSession``` object and one of the following authentication methods. ```ASFSession``` is a subclass of ```Session```. The session should be passed to whichever download method is being called, can be re-used, and is thread safe. 

- ```auth_with_creds('user', 'pass)```
- ```auth_with_token('EDL token')```
- ```auth_with_cookiejar(http.cookiejar)```

Example with manual authentication:

	results = asf_search.granule_search([...])
	session = asf_search.ASFSession().auth_with_creds('user', 'pass')
	results.download(path='/Users/SARGuru/data', session=session)

asf_search also supports downloading an arbitrary list of URLs. All of the available authentication methods are supported:

	urls = [...]
	asf_search.download_urls(urls=urls, path='/Users/SARGuru/data', session=ASFSession().auth_with_token('EDL token'))

Also note that ```ASFSearchResults.download()``` and the generic ```download_urls()``` function both accept a ```processes``` parameter which allows for parallel downloads.

## Methods
### <span style="color: #236192; font-size: 20px;">download_urls()</span>

Downloads all products from the specified URLs to the specified location.

**args**

- urls: List of URLs from which to download
- path: Local path in which to save the product
- session: The session to use, in most cases should be authenticated beforehand
- processes: Number of download processes to use. Defaults to 1 (i.e. sequential download)

### <span style="color: #236192; font-size: 20px;">download_url()</span>

Downloads a product from the specified URL to the specified location and (optional) filename.

**args**

- url: URL from which to download
- path: Local path in which to save the product
- filename: Optional filename to be used, extracted from the URL by default
- session: The session to use, in most cases should be authenticated beforehand

### <span style="color: #236192; font-size: 20px;">remotezip()</span>

Configures and returns an authenticated ```remotezip.RemoteZip``` object, allowing downloading of
specific files from a given zip archive without downloading the entire archive.

**args**

- url: URL from which to download a zip archive
- session: Authenticated ```ASFSession``` that RemoteZip will use to download from the zip product

**returns:**

- `remotezip.RemoteZip` object authenticated with the passed _ASFSession_ object

## Export Formats
asf_search provides multiple export formats, in addition to the default asf_search format. Available formats are: geojson, csv, metalink, kml, jsonlite, jsonlite2.

Examples:

	results = ....
	with open("search_results.csv", "w") as f:
		f.writelines(results.csv())

	results = ....
	with open("search_results_jsonlite.json", "w") as f:
		f.writelines(results.jsonlite())

