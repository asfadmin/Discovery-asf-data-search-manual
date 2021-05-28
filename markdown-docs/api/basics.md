# Search API Basics

Building a Search API query consists of 3 basic steps:

1. Use the Search API base URL: https://api.daac.asf.alaska.edu
2. Pick an endpoint. All available endpoints are listed in the [Keywords documentation](/api/keywords). The Search endpoint uses this base URL: https://api.daac.asf.alaska.edu/services/search/param
3. Build your query using [keywords](/api/keywords)

The completed URL will be in this format: https://api.daac.asf.alaska.edu/services/search/param?keyword1=value1&keyword2=value2,value3&keyword3=value4-6

Once your query is built, you may execute by copy/pasting into a browser window, a command line interface, or by using a program. More details on various options can be found in the [Search API Tools documentation](/api/tools).

**Syntax tips**

1. A "?" separates the endpoint URL from the keywords.
2. Keywords are joined by a "&". Some operating systems or programs may require a "\&"
3. There may not be any spaces or parentheses in the URL string. See below for character encoding.

**Character Encoding:**

>space
>
>replace with '%20'. Use '+'  in keyword values
>
>(
>
>replace with '%28'
>
>)
>
>replace with '%29'
>

For a complete list of URL codes, please see [URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp).

**Downloading Data**

In order to download data, you will need a NASA EOSDIS Earthdata Login account. Earthdata accounts are free. Go to [Earthdata Login — Create Profile](https://urs.earthdata.nasa.gov/users/new) to create an account.

You will be prompted to accept the ASF End-User License Agreement and set a Study Area to complete your new user setup.

**Next Steps**

See [Search API Keywords](/api/keywords) to get started on building a query, or see the [Tools page](/api/tools) for search and download examples.
