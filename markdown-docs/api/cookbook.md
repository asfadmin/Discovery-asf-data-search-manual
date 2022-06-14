# Search API Tips & Tricks

This is a collection of some tips & tricks for the Search API!

## New Python module for performing searches
asf_search is a Python module for performing searches of the ASF catalog. In addition, it offers baseline functionality and download support. It is available through PyPi and Conda. More information can be found [here](/asf_search/basics).

## Rate Limitation on Search Endpoint
There has been a rate limitation instituted on the [search endpoint](/api/keywords/#search-endpoint). The rate limitation is per IP and is currently 250 queries per minute. Upon hitting the limit, further queries will yield a HTTP 429 with an error message. Check to see if your queries are returning a small number of results. If so, you can refine your parameters to combine result sets into larger groups and then post-process those results locally. For instance, instead of searching on a small area of interest with an individual query for each day, select a larger date range in order to create a single query, then split the results apart after they have been retrieved.

## Vertex Copy/Paste Search API URL
Have you have completed a geo search in Vertex, that you'd like to replicate in a Search API query? Click the Down Arrow under the Max Results. Choose "API URL...".

Here you can see the Search API URL you would use to replicate the search. You may change the maxResults and output format. Once you are satisfied, click the copy icon. Now you can paste the query into a browser or command line interface to execute it.

## Find the Product_List Value in Vertex
The product/file name is listed in Vertex Search Results, under the Files detail column. You can click the Copy icon to copy the File ID. You can also copy all File IDs from your Download Queue in Vertex. Once you have your desired list of files, you can find them via the Search API using the product_list keyword.

## Search Results Can Become Search Area
You can turn your search results into a search area. First, export your search results as GeoJSON or KML output format. Next, import your file into Vertex geo search. Vertex will extract the AOI from your file. If desired, you can add filters and can save your search filters or the search itself.

## Verify Your Query is Returning the Correct Number of Results
Would you like to verify that your query has returned the correct number of results? Change your output to "output=count" to verify. If the count does not match, consider narrowing your search by using more keywords, or by using keyword “maxResults” to limit it. You may also try shortening the date range to split your search into a series of smaller searches.