# ASFProduct

## Description

This class describes a single product from the ASF archive. The class provides metadata, as well as several helpful methods for interacting with the product.

***

## Attributes
- `properties` _(dict)_: Provides product metadata such as Beam Mode, Start Time, etc.
- `geometry` _(dict)_: Describes the product's physical extents as a geojson snippet

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

- `ASFSearchResults` representation of the stack, with the addition of baseline values (temporal, perpendicular) attached to each `ASFProduct`

***

### <span style="color: #236192; font-size: 20px;">get_stack_opts()</span>

Builds search options that describe an InSAR stack based on this product. Similar to `stack()` but doesn't perform the search, simply returns `ASFSearchOptions` which can be inspected or adjusted and then passed to various search functions.

**args:**
None

**returns:**

- `ASFSearchOptions` object

***

### <span style="color: #236192; font-size: 20px;">centroid()</span>

Determines the centroid of a product.

**args:**
None

**returns:**

- `shapely.geometry.point.Point` object describing the centroid of the product

<!-- Will have more than geojson export; add this when other output options available -->
