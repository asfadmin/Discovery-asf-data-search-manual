# ASFProduct Class

## Description
<!-- netrc
how to build netrc file, link
OR auth with these options instead -->

## Methods

### download()

Downloads this product to the specified path and optional filename.

#### Parameters
- param path: The directory into which this product should be downloaded.
- param filename: Optional filename to use instead of the original filename of this product.
- param session: The session to use, in most cases should be authenticated beforehand

#### Return
- None

### stack()

Builds a baseline stack from this product.

#### Return
- ```ASFSearchResults(list)``` of the stack, with the addition of baseline values (temporal, perpendicular) attached to each ```ASFProduct```

### centroid()

Finds the centroid of a product.

#### Return
- ```shape(self.geometry).centroid```

<!-- Will have more than geojson export; add this when other output options available -->