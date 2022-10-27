# ASFSearchResults

## Description

This class describes a set of search results from the ASF archive. The class provides a convenient way to manage and examine search results, as well as export and download functionality.

***

## Attributes
- `searchOptions` _(ASFSearchOptions)_: The search options used to generate this set of results. May be `None` in some cases.
- `searchComplete` _(bool)_: Flag signifying `asf_search.search()` sucessfully completed gathering results from CMR. 
***

## Methods

### <span style="color: #236192; font-size: 20px;">download()</span>

Iterates over each ```ASFProduct``` and downloads them to the specified path.

**args:**

- path: The directory into which the products should be downloaded.
- session: The session to use, in most cases should be authenticated beforehand.
- processes: Number of download processes to use. Defaults to 1 (i.e. sequential download)

**returns:** None

***

### <span style="color: #236192; font-size: 20px;">geojson()</span>

`ASFSearchResults.__str__()` utilizes this method for serialization via `json.dumps()`

**args:** None

**returns:**

- `dict` describing the search results as a geojson object.

<!-- ### <span style="color: #236192; font-size: 20px;">kml()</span>

### <span style="color: #236192; font-size: 20px;">metalink()</span>

### <span style="color: #236192; font-size: 20px;">csv()</span>
 -->

### <span style="color: #236192; font-size: 20px;">raise_if_incomplete()</span>

Use to check if results returned from `asf_search.search()` are incomplete (this can happen
if an error occurs while querying CMR)

**args:** None

**returns:**

- Raises an `asf_search.exceptions.ASFSearchError` if the results are incomplete