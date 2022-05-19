# Searching

Each search function returns an ```ASFSearchResults``` object:

- ```geo_search()``` Find product info over an area of interest using a WKT string
- ```granule_search()``` Find product info using a list of scene names
- ```product_search()``` Find product info using a list of product IDs
- ```stack_from_id()``` Find a baseline stack of products using a reference scene ID
- If the above search approaches do not meet your search needs, ```search()``` supports all available keywords:
    - ```search()``` Find product info using any combination combination of search parameters
- Additionally, numerous constants are provided to ease the search process. Currently, we provide constants for beam mode, flight direction, instrument, platform, polarization, and product type. You can see the full [list of constants here](https://github.com/asfadmin/Discovery-asf_search/tree/master/asf_search/constants).

Examples of some search workflows can be found in this [sample script](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/hello_world.py). You may also reference the [Jupyter notebooks](https://github.com/asfadmin/Discovery-asf_search/tree/master/examples) for example workflows.

For more advanced usage, see sections [ASFSearchResults class](/asf_search/ASFSearchResults/) and [ASFProduct class](/asf_search/ASFProduct).
