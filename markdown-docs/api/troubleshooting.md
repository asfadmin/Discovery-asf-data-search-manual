# Search API Troubleshooting

**Trouble Area: Windows cURL “unrecognized protocol”**

- Reason: Invisible double quotes inserted when copy/pasting examples
- Remedy: Delete the visible quotes, which will delete the invisible quotes. Then retype quotes.

Check
**Trouble Area: Download fails with “401 Unauthorized” or “Authorization failed”**

- Reason: Missing or invalid Earthdata username/password
- Remedy: Check that you are correctly including your Earthdata username and password in your download command or config file.

Check
**Trouble Area: Download fails with “401 Unauthorized” or “Authorization failed”**

- Reason: Special characters in Earthdata password
- Remedy: Passwords with special characters need single quotes on Linux/Mac and double-quotes on Windows.

**Trouble Area: Can’t authenticate**

- Reason: Missing study area or EULA
- Remedy: Log in to Earthdata and ensure your study area is set, and you have agreed to all necessary End-User License Agreements.

<!-- I don't understand this one, there are no keywords that have a space in them. Is this still valid? -->
Values might have a space, URL encoding guide
**Trouble Area: API request with ‘+’ in it fails**

- Reason: Some keywords are stored in the Search API as two words with a space between them, some as two words joined with a ‘+’
- Remedy: Try replacing the ‘+’ with ‘%2B’.

**Trouble Area: API request fails**

- Reason: https is required
- Remedy: Make sure you are using https, not http.

Del, URL encoding
**Trouble Area: API request hangs, fails, or returns an error**

- Reason: Your URL may include spaces or special characters, especially if you are using the ‘intersectsWith’ keyword
- Remedy: Remove spaces or replace with '%20' or '+'.

15 min cap
**Trouble Area: API request not expected # results**

- Reason: The search may exceed 10,000 results
- Remedy: Narrow your search by using more keywords, or use keyword “maxResults”. You can preview the number of results by using "output=count".

**Trouble Area: Selected output format does not include needed fields**

- Reason: The JSON output returns more fields than CSV
- Remedy: GeoJSON is the preferred default format. If a required field is not included, please contact ASF using the info below or reach the team directly at uaf-asf-discovery@alaska.edu

<!-- - Trouble Area: Certificate rejected
	- Reason: Third-party certificates out of date, a problem for https searches
	- Remedy: Use http OR disable certificate checks.
		- [curl](https://curl.se/docs/manpage.html) –insecure
		- [wget](https://www.gnu.org/software/wget/) –no-check-certificate
 -->
