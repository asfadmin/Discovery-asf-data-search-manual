# Search API Troubleshooting

If you are troubleshooting Search API queries, consider using asf_search. asf_search is a Python module for performing searches of the ASF catalog. More information can be found [here](/asf_search/basics).

**Trouble Area: Query returns HTTP 429 with error message**

- Reason: Query returns HTTP 429 with error message "Rate limited, please reduce your request rate to 250/minute or less"
- Remedy: There is a rate limitation on the search endpoint. Refer to [Rate limitations](/api/cookbook/#rate-limitation-on-search-endpoint) for tips on how to construct your queries. 

**Trouble Area: Windows cURL “unrecognized protocol”**

- Reason: Invisible double quotes inserted when copy/pasting examples
- Remedy: Delete the visible quotes, which will delete the invisible quotes. Then retype quotes.

**Trouble Area: Download fails with “401 Unauthorized” or “Authorization failed”**

- Reason: Missing or invalid Earthdata username/password
- Remedy: Check that you are correctly including your Earthdata username and password in your download command or config file.

**Trouble Area: Download fails with “401 Unauthorized” or “Authorization failed”**

- Reason: Special characters in Earthdata password
- Remedy: Passwords with special characters will need to be inside quotes.

**Trouble Area: Can’t authenticate**

- Reason: Missing study area or EULA
- Remedy: Log in to Earthdata and ensure your study area is set, and you have agreed to all necessary End-User License Agreements.

**Trouble Area: Search API request with ‘+’ in it fails**

- Reason: Some keyword values could contain spaces.
- Remedy: Try replacing the ‘+’ with ‘%2B’. For further details, refer to Character Encoding on the [Tools page](/api/tools).

**Trouble Area: Search API request fails**

- Reason: https is required
- Remedy: Make sure you are using https, not http.

**Trouble Area: Search API request hangs, fails, or returns an error**

- Reason: Your URL may include spaces or special characters.
- Remedy: Refer to Character Encoding on the [Tools page](/api/tools) and ensure you are encoding spaces and special characters correctly.

**Trouble Area: Search API returns Validation Error**

- Reason: The reason for the validation error is included in the returned error message.
- Remedy: Refine your keywords and values as needed. If you are unsure why you received the validation error, you may contact ASF using the info below.

**Trouble Area: Search API query does not return expected number of results**

- Reason: There is a 15 minute time limit on running Search API queries.
- Remedy: First, try the same query with "output=count". If the count is high, consider narrowing your search by using more keywords, or by using keyword “maxResults” to limit it. You may also try shortening the date range to split your search into a series of smaller searches.

**Trouble Area: Search API query with "product_list" keyword returns no results**

- Reason: Other keywords may be competing with the product_list value(s).
- Remedy: Try removing other keywords from your query. You may also try "output=count" to see how many results your query should return.

**Trouble Area: Selected output format does not include needed fields**

- Reason: Some output formats include different fields.
- Remedy: GeoJSON is the preferred default format. If a required field is not included, please contact ASF using the info below or reach the team directly at <uaf-asf-discovery@alaska.edu>

<!-- - Trouble Area: Certificate rejected
	- Reason: Third-party certificates out of date, a problem for https searches
	- Remedy: Use http OR disable certificate checks.
		- [curl](https://curl.se/docs/manpage.html) –insecure
		- [wget](https://www.gnu.org/software/wget/) –no-check-certificate
 -->
