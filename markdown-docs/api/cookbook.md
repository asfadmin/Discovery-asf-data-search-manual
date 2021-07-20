# Search API Tips & Tricks

This is a collection of some tips & tricks for the Search API!

## Vertex Copy/Paste Search API URL
Have you have completed a geo search in Vertex, that you'd like to replicate in a Search API query? Click the Down Arrow under the Max Results. Choose "API URL...".

Here you can see the Search API URL you would use to replicate the search. You may change the maxResults and output format. Once you are satisfied, click the copy icon. Now you can paste the query into a browser or command line interface to execute it.

## Find the Product_List Value in Vertex
The product/file name is listed in Vertex Search Results, under the Files detail column. You can click the Copy icon to copy the File ID. You can also copy all File IDs from your Download Queue in Vertex. Once you have your desired list of files, you can find them via the Search API using the product_list keyword.

## Search Results Can Become Search Area
You can turn your search results into a search area. First, export your search results as GeoJSON or KML output format. Next, import your file into Vertex geo search. Vertex will extract the AOI from your file. If desired, you can add filters and can save your search filters or the search itself.