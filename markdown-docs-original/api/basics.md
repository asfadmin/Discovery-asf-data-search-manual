# Search API Basics

Building a Search API query consists of 3 basic steps:

1. Use the Search API base URL: https://api.daac.asf.alaska.edu
2. Pick an endpoint. All available endpoints are listed in the [Keywords documentation](/api/keywords). The Search endpoint uses this base URL: https://api.daac.asf.alaska.edu/services/search/param
3. Build your query using [keywords](/api/keywords)

The completed URL will be in this format: https://api.daac.asf.alaska.edu/services/search/param?keyword1=value1&keyword2=value2,value3&keyword3=value4-6

Once your query is built, you may execute by copy/pasting into a browser window, a command line interface, or by using a program. More details on various options and some syntax tips can be found in the [Search API Tools documentation](/api/tools).

**Downloading Data**

In order to download data, you will need a NASA EOSDIS Earthdata Login account. Earthdata accounts are free. Go to [Earthdata Login — Create Profile](https://urs.earthdata.nasa.gov/users/new) to create an account.

You will be prompted to accept the ASF End-User License Agreement and set a Study Area to complete your new user setup.

*Note: A research agreement is required for access to JERS-1 and RADARSAT-1 data. Please complete the required [Research Agreement](https://asf.alaska.edu/restricted-data-access-request), or contact user support at the email or number below.*

**Next Steps**

See [Search API Keywords](/api/keywords) to get started on building a query, or see the [Tools page](/api/tools) for some examples.

Alternatively, you may wish to use asf_search, a Python module for performing searches of the ASF catalog. It also offers baseline functionality and download support. Additionally, numerous constants are provided to ease the search process. It is available through PyPi and Conda. More information can be found [here](/asf_search/basics).
