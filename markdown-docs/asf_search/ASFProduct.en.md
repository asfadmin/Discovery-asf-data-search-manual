# ASFProduct

## Description

This class describes a single product from the ASF archive. The class provides metadata, as well as several helpful methods for interacting with the product.

***

## Attributes
- `properties` _(dict)_: Provides product metadata such as Beam Mode, Start Time, etc.
- `geometry` _(dict)_: Describes the product's physical extents as a geojson snippet.
- `baseline` _dict_: The product's baseline related fields, if available in CMR.
- `umm` _(dict)_: the raw umm json response from CMR used to populate `properties`, `geometry`, `baseline`, and `meta`.
- `meta` _(dict)_: the metadata json returned from CMR.
<!-- netrc
how to build netrc file, link
OR auth with these options instead -->

***

## Methods

### <span style="color: #236192; font-size: 20px;">geojson()</span>

`ASFProduct.__str__()` utilizes this method for serialization via `json.dumps()`

**args:**
None

**returns:**

- `dict` describing the product as a geojson snippet.

***

### <span style="color: #236192; font-size: 20px;">download(path, _filename=None, session=None_)</span>

Downloads this product to the specified path and optional filename.

**args:**

- path: The directory into which this product should be downloaded.
- filename _(optional)_: Filename to use instead of the original filename of this product.
- session _(optional)_: The session to use, in most cases should be authenticated beforehand. If no session is provided, a blank (unauthenticated) session will be used.
- fileType _(optional)_: Used to download Burst XML metadata. Specify ````fileType=asf.FileDownloadType.ADDITIONAL_FILES```` to download the XML metadata. To download both .tiff and .xml files for bursts, use ````asf.FileDownloadType.ALL_FILES````
	- Example: ````burst_results.download(session=session, path="./", fileType=asf.FileDownloadType.ADDITIONAL_FILES)````
	- Note: The Burst XML Metadata is a virtually generated file, and therefore does not have its own unique filename. The XML Metadata can only be found via the burst scene name.

**returns:**
None

***

### <span style="color: #236192; font-size: 20px;">stack()</span>

Builds a baseline stack using this product as a reference

**args:**

- cmr_provider _(optional)_: Custom provider name to constrain CMR results to, for more info on how this is used, see [CMR documentation](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html#c-provider)
- session _(optional)_: A Session to be used when performing the search. For most uses, can be ignored. Used when searching for a dataset, provider, etc. that requires authentication. See [ASFSession](/asf_search/ASFSession) for more details.
- host _(optional)_: SearchAPI host, defaults to Production SearchAPI. This option is intended for dev/test purposes and can generally be ignored.

**returns:**

- ```ASFSearchResults``` representation of the stack, with the addition of baseline values (temporal, perpendicular) attached to each `ASFProduct`

***

### <span style="color: #236192; font-size: 20px;">get_stack_opts()</span>

Builds search options that describe an InSAR stack based on this product. Similar to `stack()` but doesn't perform the search, simply returns ```ASFSearchOptions``` which can be inspected or adjusted and then passed to various search functions.

**args:**
None

**returns:**

- ```ASFSearchOptions``` object

***

### <span style="color: #236192; font-size: 20px;">centroid()</span>

Determines the centroid of a product.

**args:**
None

**returns:**

- ```shapely.geometry.point.Point``` object describing the centroid of the product

<!-- Will have more than geojson export; add this when other output options available -->

### <span style="color: #236192; font-size: 20px;">remotezip()</span>

Returns a configured RemoteZip object, which allows downloading selected parts of a product's zip archive.
For more information on how to use remotezip with asf-search, see the `Downloading Single Products` section of [the example jupyter notebook](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/5-Download.ipynb). For more information on the open-source remotezip package, check out <a target="_blank" href="https://github.com/gtsystem/python-remotezip">the remotezip project repo</a>.

**args:**

- `session` _ASFSession_: An authenticated _ASFSession_ object that will be used to download the product

**returns:**

- ```remotezip.RemoteZip``` object authenticated with the passed _ASFSession_ object
