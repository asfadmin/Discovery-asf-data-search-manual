# ASFSearchResults

## Description

This class describes a set of search results from the ASF archive. The class provides a convenient way to manage and examine search results, as well as export and download functionality.

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

**args:** None

**returns:**

- `dict` describing the product as a geojson snippet. `ASFProduct.__str__()` utilizes this method for serialization.

<!-- ### <span style="color: #236192; font-size: 20px;">kml()</span>

### <span style="color: #236192; font-size: 20px;">metalink()</span>

### <span style="color: #236192; font-size: 20px;">csv()</span>
 -->