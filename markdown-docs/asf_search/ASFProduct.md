# ASFProduct Class

## Description

This class describes a single product from the ASF archive. The class provides metadata, as well as several helpful methods for interacting with the product.

***

## Attributes
- `properties (dict)`: Provides product metadata such as Beam Mode, Start Time, etc.
- `geometry (dict)`: Describes the product's physical extents as a geojson snippet

<!-- netrc
how to build netrc file, link
OR auth with these options instead -->

***

## Methods

### geojson()

#### Parameters
None

#### Returns
`dict` describing the product as a geojson snippet. `ASFProduct.__str__()` utilizes this method for serialization.
***
### download(path, _filename=None, session=None_)

Downloads this product to the specified path and optional filename.

#### Parameters
- path: The directory into which this product should be downloaded.
- filename _(optional)_: Filename to use instead of the original filename of this product.
- session _(optional)_: The session to use, in most cases should be authenticated beforehand. If no session is provided, a blank (unauthenticated) session will be used.

#### Returns
- None
***
### stack()

Builds a baseline stack from this product.

#### Parameters
None

#### Returns
- `ASFSearchResults` representation of the stack, with the addition of baseline values (temporal, perpendicular) attached to each `ASFProduct`
***
### centroid()

Determines the centroid of a product.

#### Parameters
None

#### Returns
- `shapely.geometry.point.Point` object describing the centroid of the product

<!-- Will have more than geojson export; add this when other output options available -->