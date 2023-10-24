# ASF Search Options

## Description

This class describes a set of search parameters. While it is not required to use this class when constructing a search, it can be useful, as it provides some degree of immediate parameter validation, as well as a convenient way to manipulate and handle search options in general.

Specific search parameters are handled as object attributes. Attempting to add an attribute that is not supported will raise a KeyError. Attempting to delete an attribute will result in it being set to None. Search parameters can be set via kwargs at object instantion, or directly on an existing object using the normal mechanisms.

Converting to a `dict` will only include search options which have actually been set to a usable value. That is, any options set to `None` will be ignored.

***

## Attributes
- maxResults
- absoluteBurstID
- absoluteOrbit
- asfFrame
- beamMode
- provider
- collectionName
- maxDoppler
- minDoppler
- maxFaradayRotation
- minFaradayRotation
- flightDirection
- flightLine
- fullBurstID
- frame
- granule_list
- product_list
- intersectsWith
- lookDirection
- offNadirAngle
- platform
- polarization
- processingLevel
- relativeBurstID
- relativeOrbit
- processingDate
- start
- end
- season
- groupID
- insarStackId
- instrument
- session

***

## Methods

_ASFSearchOptions does not provide any methods intended for direct use, instead relying on a handful of dunders for the desired behavior. For clarity, these are included below._

### <span style="color: #236192; font-size: 20px;">__init__()</span>

Establishes the various attributes described above and processes any kwargs into them.

**args:**

- _**kwargs_, limited to names listed as attributes above. Anything else will raise a `KeyError`

**returns:**
None

***

### <span style="color: #236192; font-size: 20px;">__setattr__()</span>

Sets the attribute named by `key` to the specified `value` after passing it through an appropriate validator function.

Values of `None` are allowed as a way to un-set the attribute. Attempting to set a `key` not listed in the above attribute list will raise a `KeyError`

**args:**

- key: the name of the attribute to set
- value: the value to which the named attribute should be set

**returns:**
None

***

### <span style="color: #236192; font-size: 20px;">__delattr__()</span>

Clears an attribute names by `item` by way of setting it to `None`

**args:**

- item: the name of the attribute to be cleared

**returns:**
None

***

### <span style="color: #236192; font-size: 20px;">__iter__()</span>

Used when converting the ASFSearchOptions object to more fundamental objects, such as `dict`

Only includes attributes that are not `None`.

**args:**
None

**yields:**

- (key, value) pairs for each of the above attributes that are not `None`

***

