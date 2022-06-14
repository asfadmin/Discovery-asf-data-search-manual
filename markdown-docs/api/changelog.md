# What's New

## New Python module for performing searches
asf_search is a Python module for performing searches of the ASF catalog. In addition, it offers baseline functionality and download support. It is available through PyPi and Conda. More information can be found [here](/asf_search/basics).

## Multiple Endpoints Available

In addition to the Search endpoint, we have multiple endpoints available for all of your Search API needs. Below is a brief overview of what's available. More details on these endpoints and how to use them can be found on the [Keywords page](/api/keywords).


**Baseline Endpoint**

This endpoint can be used to search for baseline data using specific reference scenes.

**WKT Endpoints**

The WKT validation endpoint will validate and repair a WKT input. The GeoSpatial Files to WKT endpoint will accept a POST request with files attached. It will return the parsed WKT from the file, as well as the repaired wrapped and unwrapped WKT.

**Date Parser Endpoint**

This endpoint can be used to check how dates are parsed by the Search API.

**Mission List Endpoint**

This endpoint lists all missions (also known as campaigns or collections) for all datasets.

**Health Endpoint**

This endpoint is used to check the Search API health. It also provides information on CMR health.

## Preferred Search API Output Format

GeoJSON is the preferred Search API output format. You can specify the output format with keyword "output". If you find a required field that is not included in GeoJSON output, please contact ASF using the info below or reach the team directly at <uaf-asf-discovery@alaska.edu>.