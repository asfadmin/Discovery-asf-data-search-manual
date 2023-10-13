# Searching

Each search function returns an ```ASFSearchResults``` object:

- ```geo_search()``` Find product info over an area of interest using a WKT string
- ```granule_search()``` Find product info using a list of scene names
- ```product_search()``` Find product info using a list of product IDs
- ```stack_from_id()``` Find a baseline stack of products using a reference scene ID
- If the above search approaches do not meet your search needs, ```search()``` supports all available keywords:
    - ```search()``` Find product info using any combination combination of search parameters. See the keywords list below.

Examples of some search workflows can be found in this [sample script](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/hello_world.py). You may also reference the [Jupyter notebooks](https://github.com/asfadmin/Discovery-asf_search/tree/master/examples) for example workflows.

For more advanced usage, see sections [ASFSearchResults class](/asf_search/ASFSearchResults/) and [ASFProduct class](/asf_search/ASFProduct).

## Keywords

Keywords are used to find the desired data. Use as many or as few keywords as needed. Available keywords and descriptions are listed below. Additionally, numerous constants are provided to ease the search process. Currently, we provide constants for beam mode, flight direction, instrument, platform, polarization, and product type. You can see the full [list of constants here](https://github.com/asfadmin/Discovery-asf_search/tree/master/asf_search/constants).

### Dataset Parameters
- <span style="color: #236192; font-size: 20px;">platform</span>
    - See the [list of constants](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/PLATFORM.py)
    - Remote sensing platform that acquired the data. Sentinel-1 and ERS have multiple remote sensing platforms, and you may choose whether to specify a specific platform. You may specify a single value, or a list of values.
    - You may also get the available list of constants by using ```help(asf_search.constants.PLATFORM)```
    - Example:
        - platform=asf.PLATFORM.SENTINEL1A

- <span style="color: #236192; font-size: 20px;">instrument</span>
    - See the [list of constants](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/INSTRUMENT.py)
    - Remote sensing instrument that acquired the data. For some platforms, such as ALOS, there are multiple instruments to choose from.
    - You may also get the available list of constants by using ```help(asf_search.constants.INSTRUMENT)```
    - Example:
        - instrument=asf.INSTRUMENT.AVNIR_2

- <span style="color: #236192; font-size: 20px;">absoluteBurstID</span>
    - Used for Sentinel-1 [burst products](/datasets/using_ASF_data/#sentinel-1-bursts). Each value identifies the stack of a burst cycle, representing all products generated over a specific sub-swath. You may specify a single value, or a list of values. 
    - Example:
        - single value: absoluteBurstID='102563902'
        - list of values: absoluteBurstID=['102563902', '103558145']

- <span style="color: #236192; font-size: 20px; font-size: 20px;">absoluteOrbit</span>
    - For ALOS, ERS-1, ERS-2, JERS-1, RADARSAT-1, Sentinel-1A, and Sentinel-1B this value corresponds to the orbit count within the orbit cycle. For UAVSAR it is the [Flight ID](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.34282209.1335434931.1620087198-1930115146.1605056035). You may specify a single value, range of values, or a list of values.
    - Example:
        - single value: absoluteOrbit=25436
        - range of values: absoluteOrbit=(12005, 12008)
        - list of values: absoluteOrbit=[25436, 25450]  

- <span style="color: #236192; font-size: 20px;">asfFrame</span>
    - See also 'frame'
    - This is primarily an ASF / [JAXA](https://global.jaxa.jp/) frame reference. However, some platforms use other conventions. You may specify a single value, range of values, or a list of values.
    - Example:
        - single value: asfFrame=300
        - range of values: asfFrame=(2845, 2855)
        - list of values: asfFrame=[2800, 2845]
    - Values:
        - ERS, JERS, RADARSAT: ASF frames 0 to 900
        - ALOS PALSAR: JAXA frames 0 to 7200
        - SEASAT: ESA-like frames 208 to 3458
        - Sentinel-1: In-house values 0 to 1184

- <span style="color: #236192; font-size: 20px;">beamMode</span>
    - See the [list of constants](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/BEAMMODE.py)
    - The beam mode used to acquire the data.
    - You may also get the available list of constants by using ```help(asf_search.constants.BEAMMODE)```
    - Example:
        - beamMode=asf.BEAMMODE.POL

- <span style="color: #236192; font-size: 20px;">beamSwath</span>
    - The beam swath encompasses a look angle and beam mode. You may specify a single value, or a list of values.
    - Example:
        - single value: beamSwath='IW'
        - list of values: beamSwath=['IW','EW']

- <span style="color: #236192; font-size: 20px;">campaign</span>
    - For UAVSAR, AIRSAR, and Sentinel-1 Interferogram datasets only. Search by the campaign name. You may specify a single value.
    - For a list of available campaigns, use the ```asf_search.campaigns()``` function. You must provide the desired platform.
        - ```asf_search.campaigns(asf_search.PLATFORM.UAVSAR)```
    - Example:
        - campaign='Purace Volcano, Colombia'

- <span style="color: #236192; font-size: 20px;">maxDoppler</span>
    - Doppler provides an indication of how much the look direction deviates from the ideal perpendicular flight direction acquisition.
    - Example:
        - maxDoppler=1500 or maxDoppler=1500.5

- <span style="color: #236192; font-size: 20px;">minDoppler</span>
    - Doppler provides an indication of how much the look direction deviates from the ideal perpendicular flight direction acquisition.
    - Example:
        - minDoppler=100 or minDoppler=1500.5

- <span style="color: #236192; font-size: 20px;">maxFaradayRotation</span>
    - Rotation of the polarization plane of the radar signal impacts imagery. HH and HV signals become mixed. One-way rotations exceeding 5° are likely to significantly reduce the accuracy of geophysical parameter recovery, such as forest biomass.
    - Example:
        - maxFaradayRotation=3.5

- <span style="color: #236192; font-size: 20px;">minFaradayRotation</span>
    - Rotation of the polarization plane of the radar signal impacts imagery. HH and HV signals become mixed. One-way rotations exceeding 5° are likely to significantly reduce the accuracy of geophysical parameter recovery, such as forest biomass.
    - Example:
        - minFaradayRotation=2

- <span style="color: #236192; font-size: 20px;">flightDirection</span>
    - See the [list of constants](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/FLIGHT_DIRECTION.py)
    - Satellite orbit direction during data acquisition. You may specify a single value.
    - You may also get the available list of constants by using ```help(asf_search.constants.FLIGHT_DIRECTION)```
    - Example:
        - flightDirection=asf.FLIGHT_DIRECTION.ASCENDING

- <span style="color: #236192; font-size: 20px;">flightLine</span>
    - Specify a flightline for UAVSAR or AIRSAR. You may specify a single value.
    - Example:
        - UAVSAR: flightLine='05901'
        - AIRSAR: flightLine='gilmorecreek045-1.93044'

- <span style="color: #236192; font-size: 20px;">frame</span>
    - See also 'asfFrame'
    - ESA-referenced frames are offered to give users a universal framing convention. Each ESA frame has a corresponding ASF frame assigned. You may specify a single value, range of values, or a list of values.
    - Example:
        - single value: frame=300
        - range of values: frame=(305, 315)
        - list of values: frame=[300, 303, 305]
    - Values:
        - Any number from 0 to 7200.

- <span style="color: #236192; font-size: 20px;">fullBurstID</span>
    - Used for Sentinel-1 [burst products](/datasets/using_ASF_data/#sentinel-1-bursts). Each value represents all burst products over a single sub-swath, corresponding to a near-perfect frame-aligned stack. This value is useful for baseline stacking. You may specify a single value, or a list of values.
    - Example:
        - single value: fullBurstID='017_034465_IW2'
        - list of values: fullBurstID=['017_034465_IW2', '079_167884_IW1']

- <span style="color: #236192; font-size: 20px;">groupID</span>
    - List of specific group IDs. For some datasets, the group ID is the same as the scene name. For others, such as Sentinel-1, the group ID is unique for a group of scenes.
    - Example:
        - groupID='S1A_IWDV_0112_0118_037147_150'

- <span style="color: #236192; font-size: 20px;">lookDirection</span>
    - Left or right direction of data acquisition. You may specify a single value.
    - Example:
        - lookDirection='L'
    - Values:
        - R, RIGHT, L, LEFT

- <span style="color: #236192; font-size: 20px;">offNadirAngle</span>
    - Off-nadir angles for ALOS PALSAR. You may specify a single value, range of values, or a list of values.
    - Example:
        - single value: offNadirAngle=21.5
        - range of values: offNadirAngle=(9.7, 14)
        - list of values: offNadirAngle=[21.5, 23.1]
    - Values:
        - Most common: 21.5, 23.1, 27.1, 34.3
        - Other: 9.7, 9.9, 13.8, 14, 16.2, 17.3, 17.9, 18, 19.2, 20.5, 21.5, 23.1, 24.2, 24.6, 25.2, 25.8, 25.9, 26.2, 27.1, 28.8, 30.8, 34.3, 36.9, 38.8, 41.5, 43.4, 45.2, 46.6, 47.8, 49, 50, 50.8

- <span style="color: #236192; font-size: 20px;">polarization</span>
    - See the [list of constants](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/POLARIZATION.py)
    - A property of SAR electromagnetic waves that can be used to extract meaningful information about surface properties of the earth. You may specify a single value, or a list of values.
    - You may also get the available list of constants by using ```help(asf_search.constants.POLARIZATION)```
    - Example:
        - polarization=asf.POLARIZATION.VV

- <span style="color: #236192; font-size: 20px;">processingLevel</span>
    - See the [list of constants](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/PRODUCT_TYPE.py)
    - Level to which the data has been processed, also type of product.
    - You may also get the available list of constants by using ```help(asf_search.constants.PRODUCT_TYPE)```
    - Example:
        - processingLevel=asf.PRODUCT_TYPE.SLC

- <span style="color: #236192; font-size: 20px;">relativeBurstID</span>
    - Used for Sentinel-1 [burst products](/datasets/using_ASF_data/#sentinel-1-bursts). Each value identifies a burst cycle, and within each sub-swath these values are unique. You may specify a single value, or a list of values.
    - Example:
        - single value: relativeBurstID='367299'
        - list of values: relativeBurstID=['167877', '167882']

- <span style="color: #236192; font-size: 20px;">relativeOrbit</span>
    - Path or track of satellite during data acquisition. For UAVSAR it is the [Line ID](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.201268782.1252483948.1620685771-1930115146.1605056035). You may specify a single value, range of values, or a list of values.
    - Example:
        - single value: relativeOrbit=5905
        - range of values: relativeOrbit=(2400, 2410)
        - list of values: relativeOrbit=[500, 580]
    - Values:
        - ALOS: 1-671
        - ERS-1: 0-2410
        - ERS-2: 0-500
        - JERS-1: 0-658
        - RADARSAT-1: 0-342
        - SEASAT: 1-243
        - UAVSAR: various

### Geospatial Parameters

- <span style="color: #236192; font-size: 20px;">intersectsWith</span>
    - Search by polygon, a line segment (“linestring”), or a point defined in 2-D Well-Known Text (WKT). Each polygon must be explicitly closed, i.e. the first vertex and the last vertex of each listed polygon must be identical. Coordinate pairs for each vertex are in decimal degrees: longitude is followed by latitude.
    - Example:
        - intersectsWith='POLYGON((-152.81 58.49,-154.90 57.49,-155.08 56.30,-153.82 56.34,-151.99 57.30,-151.43 58.19,-152.81 58.49))'
        - intersectsWith='LINESTRING(-119.543 37.925, -118.443 37.7421)'
        - intersectsWith='POINT(-119.543 37.925)'

#### Shape Validation
If the AOI specified is its own Minimum Bounding Rectangle (MBR) in a mercator projection, the search results returned will instersect with the AOI in a mercator projection, regardless of width. This remains the case even if the international dateline is crossed within the AOI.

In order for an AOI to be considered its own MBR, it must meet the following criteria:

  - Each vertex shares a latitude or longitude with its neighbors
  - East/West points share longitude
  - North/South points share latitude

AOIs that do not fit this criteria will have their points connected along [great circles](https://en.wikipedia.org/wiki/Great_circle).

In addition, all AOIs are validated, and then simplified as needed. The process for this is:
 
  1. Validate the input AOI. If it is not valid, an error is displayed.
  2. Merge overlapping shapes.
  3. Convex hull.
  4. Any out-of-range index values are handled by clamping and wrapping them to the valid range of values.
  5. Simplify points based on proximity threshold. The target is fewer than 400 points.

Each of these steps is performed only when necessary to get the AOI to a single outline with fewer than 400 points. Any unnecessary steps are skipped.

**Examples of validation and simplification:**

- A self-intersecting polygon is provided: 
    - An error is displayed.
- A single outline is provided, consisting of 1000 points:
    - A simplified version of the same outline is used, consisting of fewer than 400 points.
- Multiple geometries are provided, all of them overlapping at least in part:
    - A single outline is returned, representing the outline of all the shapes combined.
- Multiple geometries are provided, at least some of them entirely non-overlapping:
    - A single outline is returned, representing the convex hull of all the shapes together.

### Temporal Parameters
- <span style="color: #236192; font-size: 20px;">processingDate</span>
    - Limit results to records that have been processed at ASF since a given date and/or time.
    - Example:
        - processingDate='2017-01-01T00:00:00UTC'

- <span style="color: #236192; font-size: 20px;">start</span>
    - Date of data acquisition. Can be used in combination with 'end'. You may enter natural language dates, or a date and/or time stamp. All times are in UTC.
    - Example:
        - start='May 30, 2019'
        - start='yesterday'
        - start='2010-10-30T11:59:59Z'
        - start='1 week ago', end='now'

- <span style="color: #236192; font-size: 20px;">end</span>
    - Date of data acquisition. Can be used in combination with 'start'. You may enter natural language dates, or a date and/or time stamp. All times are in UTC.
        - end='May 30, 2018'
        - end='today'
        - end='2021-04-30T11:59:59Z'
        - start='1 week ago', end='now'

- <span style="color: #236192; font-size: 20px;">season</span>
    - Start and end day of year for desired seasonal range. This keyword may be used in conjunction with start/end to specify a seasonal range within an overall date range. Values are based on the Julian calendar. You must specify both a season start and end date.
    - Example:
        - season=[1, 31]
        - season=[45, 67]
        - season=[360, 10]
    - Values:
        - 1 through 365

### Baseline Parameters
- <span style="color: #236192; font-size: 20px;">stack_from_id</span>
    - Input the scene name for which you wish to see baseline results.
    - stack_from_id may not be used in conjuction with other keywords.
    - Example: 
        - stack_from_id('S1A_IW_SLC__1SDV_20220215T225119_20220215T225146_041930_04FE2E_9252-SLC')
    - See the [Jupyter notebook](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/4-Baseline_Search.ipynb) for usage examples, as well as best practices.

### Results Parameters
- <span style="color: #236192; font-size: 20px;">maxResults</span>
    - Maximum number of data records to return.
    - Example:
        - maxResults=10
