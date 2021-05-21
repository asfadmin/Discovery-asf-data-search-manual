# Search API Troubleshooting

**Trouble Area: Windows cURL “unrecognized protocol”**

- Reason: Invisible double quotes involuntarily inserted when copy/pasting examples
- Remedy: Delete the visible quotes, which will delete the invisible quotes. Then retype quotes.

**Trouble Area: Download fails with “401 Unauthorized” or “Authorization failed”**

- Reason: Missing or invalid Earthdata username/password
- Remedy: Check that you are correctly including your Earthdata username and password in your download command.

**Trouble Area: Download fails with “401 Unauthorized” or “Authorization failed”**

- Reason: Special characters in Earthdata password
- Remedy: Passwords with special characters need single quotes on Linux/Mac and double-quotes on Windows.

**Trouble Area: Cookie request to /services/authentication/ fails with “410 Gone”**

- Reason: Cookie URL has been retired
- Remedy: It’s no longer necessary to request an authorization cookie before downloading data.

**Trouble Area: Can’t authenticate**

- Reason: Missing study area or EULA
- Remedy: Log in to Earthdata and ensure your study area is set, and you have agreed to all necessary End-User License Agreements.

**Trouble Area: Wget or cURL command copied from the webpage doesn’t work**

- Reason: Copy/paste over multiple lines introduces error
- Remedy: Copy and paste one line at a time.

**Trouble Area: Wget or cURL command copied from the webpage doesn’t work**

- Reason: Quotes look the same but are interpreted differently
- Remedy: Where single quotes are present, delete and retype them in the terminal window.

<!-- I don't understand this one, there are no keywords that have a space in them. Is this still valid? -->
**Trouble Area: API request with ‘+’ in it fails**

- Reason: Some keywords are stored in the Search API as two words with a space between them, some as two words joined with a ‘+’
- Remedy: Try replacing the ‘+’ with ‘%2B’.

**Trouble Area: API request fails**

- Reason: https is required
- Remedy: Make sure you are using https, not http.

**Trouble Area: Can’t download PALSAR data**

- Reason: You must agree to the PALSAR EULA in order to download PALSAR data
- Remedy: Log in to Earthdata and agree to the End-User License Agreement, then retry downloading.

**Trouble Area: API request hangs, fails, or returns an error**

- Reason: Your URL may include spaces or special characters, especially if you are using the ‘intersectsWith’ keyword
- Remedy: Remove spaces or replace with '%20' or '+'.

**Trouble Area: API request hangs or fails**

- Reason: The search may exceed 10,000 results
- Remedy: Narrow your search by using more keywords, or use keyword “maxResults”.

**Trouble Area: API request returns process ID (PID) numbers but does not return query results**

- Reason: URLs at the command line may require the “&” to be escaped
- Remedy: Replace ampersand “&” with backslash ampersand “\&” in the URL. OR use double quotes ” ” around the URL; URLs submitted via the browser use ampersand “&” without the backslash.

**Trouble Area: Keyword not respected**

- Reason: Keywords are case sensitive
- Remedy: Ensure that your keywords are capitalized (or not) just as in the [Keyword List](/api/keywords).

**Trouble Area: Keyword not respected**

- Reason: Keyword is deprecated
- Remedy: See the [Keyword List](/api/keywords) for a list of deprecated keywords.

**Trouble Area: CSV and JSON do not contain the same output**

- Reason: The JSON output returns more fields than CSV
- Remedy: Depending on which fields you wish to see, you may select CSV or JSON output. You may also try JSONLITE output.

<!-- - Trouble Area: Certificate rejected
	- Reason: Third-party certificates out of date, a problem for https searches
	- Remedy: Use http OR disable certificate checks.
		- [curl](https://curl.se/docs/manpage.html) –insecure
		- [wget](https://www.gnu.org/software/wget/) –no-check-certificate
 -->
