# Downloading

## Session Authentication

asf_search supports downloading data, both from search results as provided by the search functions, and directly on product URLs. An authenticated session is generally required. If a .netrc file is available, those credentials will be used implicity and no direct session handling is required. More information on .netrc files can be found [here](https://www.gnu.org/software/inetutils/manual/html_node/The-_002enetrc-file.html). Otherwise, authenticate using an ```ASFSession``` object and one of the following authentication methods:

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
