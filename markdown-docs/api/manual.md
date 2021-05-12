# API User Guide

## API Basics
**Building an API command**

Build an API command: Program + URL + keywords

- Choose a program
	- Choose a command-line program to transfer data using a URL
	- Choose [cURL](https://curl.se/docs/manpage.html) or [Wget](https://www.gnu.org/software/wget/)
	- Construct command at the command line
- Use the ASF API URL
	- https://api.daac.asf.alaska.edu/services/search/param?
- Choose keywords
	- Define your search using keywords such as *asfframe*, *absoluteOrbit*, *output*. Choose keyword output's value based on intended use.
	- See the [keyword list](/api/keywords)
	- Search, visualize, or download by including the appropriate Output keyword value in the API command.

**Possible keyword values for Search**

- CSV: Used in Microsoft Excel
- JSON: Used in custom scripts, [JSON viewer](http://jsonviewer.stack.hu/)
- COUNT

**Possible keyword values for Visualize**

- KML: Used in [Google Earth](https://www.google.com/earth/versions/#download-pro) or [ArcGIS Earth](https://www.esri.com/en-us/arcgis/products/arcgis-earth/overview)
- GEOJSON: Used in custom scripts, [JSON viewer](http://jsonviewer.stack.hu/)

**Possible keyword values for Download**

- METALINK (default): This requires [aria2](https://wiki.archlinux.org/title/aria2)
- JSON: Used in custom scripts, direct download of URLs
- DOWNLOAD: Used in custom scripts, direct download of URLs

*Note: A research agreement is required for access to JERS-1 and RADARSAT-1 data. Please complete the required [Research Agreement](https://asf.alaska.edu/restricted-data-access-request), or contact user support at the link or number below.*


##Quick Guide for Power Users
**API URL**: https://api.daac.asf.alaska.edu/services/search/param?keyword=value\&…

**Keywords**: See [here](/api/keywords) for a full list of keywords.

**Output**: Default output format is METALINK; users can also specify CSV, KML, JSON, COUNT, DOWNLOAD, and GEOJSON.

**Authenticate and Download (Linux/Mac Examples):**

*Note*: Authenticate by using your [Earthdata Login account](https://urs.earthdata.nasa.gov/users/new)

**Aria2 — Download Known Granule**

      aria2c –http-auth-challenge=true –http-user=CHANGE_ME –http-passwd=’CHANGE_ME’ “https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink”

**Aria2 — Download Based on Platform and Time-Range Search**

      aria2c –http-auth-challenge=true –http-user=CHANGE_ME –http-passwd=’CHANGE_ME’ “https://api.daac.asf.alaska.edu/services/search/param?platform=Sentinel-1A&intersectsWith=point(-122.425 37.77)&start=2016-07-01T00:00:00&output=metalink”

**Wget — Download Known Metalink**

      wget -c –http-user=CHANGE_ME –http-password=’CHANGE_ME’ “https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip”

## Search, Visualize, Download

The API can be used to search, visualize, or download SAR data from the ASF data pool depending on the choice of ‘output’ keyword value. The default output is METALINK, which is useful for downloading data.

**Search and Visualize**

Searches can be done with CSV or JSON output. Note that CSV returns many more fields than JSON. Users may visualize data with KML files and Google Earth or a similar program. The API will return a maximum of 10,000 results for a given search.

**Search and Visualize via browser**

A non-command-line option is to visualize your results by pasting the URL and keywords into a browser. You’ll need to have Google Earth or another program installed. You can also do CSV, JSON, or METALINK searches via the browser and get a file returned. If you do this, use ‘&’ instead of ‘\&’. This is a great option if you are not scripting, or for smaller searches.

**API Uses and Output Keywords**

- Search
	- CSV: Used in Microsoft Excel
	- JSON: Used in custom scripts, [JSON viewer](http://jsonviewer.stack.hu/)
- Count
	- Used with command line
- Visualize
	- KML: Used in browser, [Google Earth](https://www.google.com/earth/versions/#download-pro), or [ArcGIS Earth](https://www.esri.com/en-us/arcgis/products/arcgis-earth/overview)
	- GEOJSON: Used [GEOJSON viewer](http://geojson.io/#map=2/20.0/0.0)
- Download
	- METALINK (default): This requires [aria2](https://wiki.archlinux.org/title/aria2)
	- DOWNLOAD: This requires [Python](https://www.python.org/)

### Download Setup Steps
Do these one-time setup steps prior to using the API Download Tool to download data from the ASF data pool.

**1) Get an Earthdata Login account**

A NASA EOSDIS Earthdata Login account is required for downloading data from ASF. Earthdata Login accounts are easy to register for on the [Earthdata Login — Create Profile](https://urs.earthdata.nasa.gov/users/new) page.

After creating your account, you must log into [Vertex](https://search.asf.alaska.edu/#/), accept the Terms of Service, and set your Study Area before downloading data.

**2) Install a Command-Line Download Tool**

ASF’s recommended tool for bulk downloads is the ASF [Bulk Download Python Script](https://bulk-download.asf.alaska.edu/).

[aria2](https://aria2.github.io/) can also be used for downloads.

[Wget](https://www.gnu.org/software/wget/) comes installed on most Linux distributions and is also available for [Windows, Mac, and other platforms](http://wget.addictivecode.org/FrequentlyAskedQuestions.html?action=show&redirect=Faq#download).

###Bulk Download with Aria2

The API Download Tool supports downloading API search results with aria2 in one easy command!

- Include your Earthdata username and password
- Include your API search URL and keywords
- Make sure output=metalink
- Run it!

**Linux/Mac Example — Log in, search, and download results in one command**

      aria2c --http-auth-challenge=true --http-user=CHANGE_ME --http-passwd='CHANGE_ME' "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

**Windows Example — Log in, search, and download results in one command**

      aria2c --check-certificate=false --http-auth-challenge=true --http-user=CHANGE_ME --http-passwd="CHANGE_ME" "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

Having trouble? See the Troubleshooting section for resolutions to common issues.

Additional [aria2 options available here](http://aria2.sourceforge.net/manual/en/html/aria2c.html).

###Download Without Installing Aria2

Users without access to aria2 can still download files, but it takes a few more steps:

- Run your API search with output=CSV
- Review your search results for the download URL(s) of the file(s) you want
- Download those files one at a time using Wget

**Linux/Mac Example — Download a datapool file using Wget**

      wget -c --http-user=CHANGE_ME --http-password='CHANGE_ME' "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

**Windows Example — Download a datapool file using Wget**

      wget --check-certificate=off -c --http-user=CHANGE_ME --http-password="CHANGE_ME" "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

Having trouble? See the Troubleshooting section for resolutions to common issues.

Additional Wget options at the [GNU Wget Manual](https://www.gnu.org/software/wget/manual/wget.html).

###A Note About Passwords

You can store your Earthdata username and password in a configuration file instead of including them in every download command.  This can make downloads more convenient, and hides your credentials from other users that have access to see commands being run on your system.  If you save your password in a file, make sure to set the file’s permissions so other users can’t read it!

**Linux/Mac Example — Create and use a configuration file with aria2**

      echo 'http-user=CHANGE_ME' >> aria2.conf
      echo 'http-passwd=CHANGE_ME' >> aria2.conf
      chmod 600 aria2.conf

      aria2c --conf-path=aria2.conf --http-auth-challenge=true "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

**Linux/Mac Example — Create and use a configuration file with Wget**

      echo 'http_user=CHANGE_ME' >> wget.conf
      echo 'http_password=CHANGE_ME' >> wget.conf
      chmod 600 wget.conf

      export WGETRC="wget.conf" wget -c "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

You can store other default options in your configuration file as well.  Refer to the complete documentation on configuration files for [aria2](https://aria2.github.io/manual/en/html/aria2c.html#aria2-conf) and [Wget](https://www.gnu.org/software/wget/manual/html_node/Startup-File.html#Startup-File).

##Build API Command

API commands can be incorporated into scripts or used at the command line via the Mac terminal window, Command Prompt window on Windows, or on Linux systems.

1. File-transfer program [cURL](https://curl.se/docs/manpage.html) or [Wget](https://www.gnu.org/software/wget/)
2. Base URL
3. Keywords and values

**Example**

      curl https://api.daac.asf.alaska.edu/services/search/param?platform=R1\&absoluteOrbit=25234\&output=CSV

**Windows Example**

      curl “https://api.daac.asf.alaska.edu/services/search/param?platform=R1&absoluteOrbit=25234&output=CSV” > myfilename.csv

Hint: Copying and pasting quotation marks causes errors for Windows users. Delete and re-type the quotes after pasting.

**1) Choose a File Transfer Program and options**

Both [Wget](https://www.gnu.org/software/wget/) and [cURL](https://curl.se/) are often installed on Linux systems. cURL is part of the Mac OS, and Wget can be installed. MS-Windows OS does not come with either installed, but both can be downloaded. cURL is easier to set up on a Windows machine.

**Browser Option**

Searches can be done in the browser. Paste just the URL and keywords into a browser to search, visualize, or get a metalink file for downloading data. Connect keywords with “&” when using the browser. A file is returned, or you can open results in Google Earth to visualize.

**Send all search results to a file**

Wget option ‘-O *myfilename*‘ or cURL ‘https://….   > *myfilename*‘ will send all search results into a file. To download data from ASF, use the *.metalink* extension on your filename. The metalink output is default for ASF searches, but can be explicitly called with keyword output=METALINK.

**Example — query results sent to a metalink file**

      wget -O myfilename.metalink https://api.daac.asf.alaska.edu/services/search/param?intersectsWith=point%28-119.543+37.925%29\&platform=ALOS\&output=metalink

      curl https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP021910740,ALPSRP085800750 >myfilename.metalink

**Hint**: Copy/pastes of examples that span multiple lines introduce error for Mac/Linux users. Copy and paste one line at a time.

**Windows Example**

      curl “https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP021910740,ALPSRP085800750” > myfilename.metalink

**2) Use the Base URL**

The ASF API URL is https://api.daac.asf.alaska.edu/services/search/param?

**3) Choose Keywords**

Keywords are used to find the desired data. Use as many or as few keywords as needed.

**Sample Keywords**
- asfframe
	- This is an ASF / JAXA frame reference. See also ‘frame’.
	- Values: Any number, series of numbers, or number range from 1 to 900 for ERS, RADARSAT, JERS. 0-7200 for ALOS PALSAR.

- output
	- Format of the API search results returned. If not specified, default return is METALINK for ASF API.
	- Example: output=CSV
	- Values: CSV, JSON, KML, METALINK, COUNT, DOWNLOAD, GEOJSON

- platform
	- Remote sensing platform that acquired the data.
	- Example: platform=ALOS
	- Values: A3, AI, AS, E1, E2, J1, ERS-1, ERS-2, JERS-1, R1, UA, AIRSAR, ALOS, ERS-1, ERS-2, JERS-1, RADARSAT-1, SEASAT, Sentinel-1A, UAVSAR

**Syntax hints:**

- A”?” separates the URL from the keywords.
- The keywords are joined by  “\&” for command line in Mac/Linux or “&” in browser and Windows.
- The base URL and keywords may not have any spaces.
- Some keywords contain characters that must be encoded.
- Keywords are case sensitive.

**Keyword Character Encoding:**
URLs **may not** contain spaces or parentheses. Some keywords, such as intersectsWith, have parentheses and spaces. Those characters must be encoded as shown below.

>space
>
>remove spaces in URL or use ‘%20’. Use ‘+’  in keyword values
>
>(
>
>replace with %28
>
>)
>
>replace with %29
>

For a complete list of URL codes, please see [URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp).

**Example encoding:** intersectsWith=point(-119.543 37.925)

      intersectsWith=point%28-119.543+37.925%29

Keywords  may contain a single value or a range of values, depending on the requirements of the particular keyword. For example, “frame=300,310-350” contains both a single value and a range.  The geographic area to be searched can be defined using either the older *polygon* keyword, or the newer *intersectswith*. *Intersectswith* has the advantage of allowing a line, a point, or a multi-area search in addition to a single polygon.

**4) Put it All Together — Examples**

**Mac/Linux Examples**

      Search
      curl https://api.daac.asf.alaska.edu/services/search/param?platform=r1\&asfframe=300\&output=CSV > myfilename.csv

      Visualize
      wget -O myfilename.kml https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550\&output=KML

      Download
      wget -c -O myfilename.metalink https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550\&output=METALINK

**Windows examples**

      Search
      curl  “https://api.daac.asf.alaska.edu/services/search/param?platform=r1&asfframe=300&output=CSV” > myfilename.csv

      Visualize
      url “https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550&output=KML” >myfilename.kml

      Download
      curl -L “https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550&output=METALINK” >myfilename.metalink

##Keywords

Keywords are used to find the desired data. Use as many or as few keywords as needed. Available keywords and descriptions are listed below.

**Syntax hints:**

- A "?" separates the URL from the keywords.
- The keywords are joined by  “\&” for command line, or “&” in the browser.
- The base URL and keywords may not have any spaces.
- Some keywords contain characters that must be encoded.
- Keywords are case sensitive.

**Keyword Character Encoding:**

For searches to be successful, URLs may not contain spaces or parentheses. Some keywords, such as intersectsWith, have parentheses and spaces. Therefore those characters must be encoded as shown below.

**Character Encoding**

>space
>
>remove spaces in URL or use ‘%20’. Use ‘+’  in keyword values
>
>(
>
>replace with %28
>
>)
>
>replace with %29
>
​

####Deprecated Keywords
- beam: See beamMode
- direction: See flightDirection
- format: See output
- limit: See maxResults
- lookAngle: See offNadirAngle
- minPercentCoherence: Deprecated
- minPercentTroposphere: Deprecated
- minPercentUnwrapped: Deprecated
- orbit: See absoluteOrbit
- offnadir: See offNadirAngle
- path: See relativeOrbit
- processing: See processingLevel
- slaveStart/SlaveEnd: Deprecated
- varianceTroposphere: Deprecated


####Active Keywords

- absoluteOrbit
	- For ALOS, ERS-1, ERS-2, JERS-1, and RADARSAT-1, Sentinel-1A, Sentinel-1B this value corresponds to the orbit count within the orbit cycle. For UAVSAR it is the [Flight ID](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.34282209.1335434931.1620087198-1930115146.1605056035).
	- Examples:
		- RADARSAT: absoluteOrbit=25436;
		- PALSAR: absoluteOrbit=25436-25445, 25450;
		- UAVSAR: absoluteOrbit=12006
- asfframe
	- This is primarily an ASF / [JAXA](https://global.jaxa.jp/) frame reference. However, some platforms use other conventions. See ‘frame’ for ESA-centric frame searches.
	- Values:
		- Any valid number, series of numbers, or number range for a given platform.
		- ERS, JERS, RADARSAT: ASF frames 0 to 900.
		- ALOS PALSAR: JAXA frames 0 to 7200.
		- SEASAT: ESA-like frames 0208 to 3458  (must use a leading zero for frames 208-999).
		- Sentinel-1: In-house values 0 to 1184.
	- Note:
		- Use in-range value for a successful search.
	- Examples:
		- asfframe=300 or asfframe=2845-2855 or asfframe=2800,2845-2855

- maxBaselinePerp
	- For interferometric SAR (InSAR) analysis, Perpendicular Baseline is the spatial distance between the first and second observations measured perpendicular to the satellite look direction and provides an indication of the sensitivity to topographic height.
	- Works for ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (Not Sentinel-1)
	- Example:
		- maxBaselinePerp=1500 or maxBaselinePerp=50.5

- minBaselinePerp
	- For interferometric SAR (InSAR) analysis, Perpendicular Baseline is the spatial distance between the first and second observations measured perpendicular to the satellite look direction and provides an indication of the sensitivity to topographic height.
	- Works for ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (Not Sentinel-1)
	- Example:
		- minBaselinePerp=100 or minBaselinePerp=50.5

- bbox
	- Bounding boxes define an area using two long/lat points. The Bounding box parameters are 4 comma-separated numbers: lower left longitude,latitude, and upper right longitude,latitude. Best choice for very wide search areas.
	- Example:
		- bbox=-150.2,65.0,-150.1,65.5

- beamMode
	- The beam mode used to acquire the data. See also beamSwath.
	- Example:
		- beamMode=FBS or beamMode=EW,IW or beamMode=ScanSAR+Wide (URL encoding required for space in name)
	- Platform & Values:
		- AIRSAR: 3FP, ATI, XTI
		- ALOS: FBD, FBS, PLR, WB1, WB2, DSN
		- ERS-1: Standard, STD
		- ERS-2: Standard, STD
		- JERS-1: Standard, STD
		- RADARSAT-1: Standard, STD, Fine, High, Low, Wide, Narrow, ScanSAR+Wide, ScanSAR+Narrow
		- SEASAT: Standard, STD
		- SMAP: Standard, STD
		- Sentinel-1A: EW, IW, S1, S2, S3, S4, S5, S6, WV
		- Sentinel-1B: EW, IW, S1, S2, S3, S4, S5, S6, WV
		- UAVSAR: POL, RPI

- beamSwath
	- BeamSwath encompasses a look angle and beam mode.
	- Example:
		- beamSwath=0
		- beamSwath=FN1, FN2, FN3, FN4, FN5
	- Platform & Values:
		- AIRSAR: 3FP, ATI, XTI
		- ALOS: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20
		- ERS-1: STD
		- ERS-2: STD
		- JERS-1: STD
		- RADARSAT-1: FN1, FN2, FN3, FN4, FN5, SNA, SNB, ST1, ST2, ST3, ST4, ST5, ST6, ST7, SWA, SWB, WD1, WD2, WD3, EH3, EH4, EH6, EL1
		- SEASAT: STD
		- Sentinel-1A: EW, IW, S1, S2, S3, S4, S5, S6, WV
		- Sentinel-1B: EW, IW, S1, S2, S3, S4, S5, S6, WV
		- UAVSAR: POL, RPI

- collectionName
	- For UAVSAR and AIRSAR data collections only. Search by general location, site description, or data grouping as supplied by flight agency or project.
	- Example:
		- collectionName=Haiti
		- UAVSAR: collectionName=Iceland collectionName=earthquake
		- AIRSAR: collectionName=Denali

- maxDoppler
	- Doppler provides an indication of how much the look direction deviates from the ideal perpendicular flight direction acquisition.
	- Example:
		- maxDoppler=1500 or maxDoppler=1500.5

- minDoppler
	- Doppler provides an indication of how much the look direction deviates from the ideal perpendicular flight direction acquisition.
	- Example:
		- minDoppler=100 or minDoppler=1500.5

- maxFaradayRotation
	- Rotation of the polarization plane of the radar signal impacts imagery. HH and HV signals become mixed. One-way rotations exceeding 5° are likely to significantly reduce the accuracy of geophysical parameter recovery, such as forest biomass.
	- Example:
		- maxFaradayRotation=3.5

- minFaradayRotation
	- Rotation of the polarization plane of the radar signal impacts imagery. HH and HV signals become mixed.
	- Example:
		- minFaradayRotation=2

- flightDirection
	- Satellite orbit direction during data acquisition.
	- Example:
		- flightDirection=DESCENDING
	- Values:
		- A, ASC, ASCENDING, D, DESC, DESCENDING

- flightLine
	- Specify a flightline for UAVSAR or AIRSAR.
	- Example:
		- UAVSAR: flightLine=05901
		- AIRSAR: flightLine=gilmorecreek045-1.93044

- frame
	- ESA-referenced frames are offered to give users a universal framing convention. Each ESA frame has a corresponding ASF frame assigned. See also ‘asfframe’.
	- Note: The asfframe number rather than the ESA frame number will be returned in your search metalink file.
	- Example:
		- frame=300
		- frame=300-400
		- frame=300,303,305
		- frame=300,303,305-315
	- Values:
		- Any number from 0 to 7200.

- granule_list
	- Comma-separated list of specific granules. Large lists will need to utilize a [POST request](https://en.wikipedia.org/wiki/POST_(HTTP)).
	- *Note: specifying a granule list will cause most other keywords to be ignored including output.*
	- Example:
		- granule_list=R1_12345_FN1_F001,R1_12345_FN1_F002

- maxInsarStackSize
	- An InSAR stack is composed of all SAR granules that cover the same geographic region, are from the same platform, and were acquired with the same beam mode, look angle, and bandwidth. To obtain InSAR stacks containing a certain number of SAR granules specify a min, max, or both.
	- Works for ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (Not Sentinel-1)
	- Example:
		- maxInsarStackSize=175

- minInsarStackSize
	- An InSAR stack is composed of all SAR granules that cover the same geographic region, are from the same platform, and were acquired with the same beam mode, look angle, and bandwidth. To obtain InSAR stacks containing a certain number of SAR granules specify a min, max, or both.
	- Works for ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (Not Sentinel-1)
	- Example:
		- minInsarStackSize=20

- intersectsWith
	- Search by polygon, a line segment (“linestring”), or a point defined in 2-D Well-Known Text (WKT). Each polygon must be explicitly closed, i.e. the first vertex and the last vertex of each listed polygon must be identical. Coordinate pairs for each vertex are in decimal degrees: longitude is followed by latitude.
	- Note:
		- Does not support multi-polygon, multi-line or multi-point.
 		- Polygon holes are ignored
 	- Examples (need URL encoding):
 		- intersectsWith=polygon((-119.543 37.925, -118.443 37.7421, -118.682 36.8525, -119.77 37.0352, -119.543 37.925 ))
		- intersectsWith=linestring(-119.543 37.925, -118.443 37.7421)
		- intersectsWith=point(-119.543, 37.925)
	- Properly URL encoded:
		- intersectsWith=point%28-119.543+37.925%29

- lookDirection
	- Left or right direction of data acquisition.
	- Example:
		- lookDirection=L
	- Values:
		- R, RIGHT, L, LEFT

- offNadirAngle
	- Off-nadir angles for ALOS PALSAR
	- Example:
		- offNadirAngle=21.5
		- offNadirAngle=9.7-14
		- offNadirAngle=21.5,23.1,20.5-24.2
	- Values:
		- Most common: 21.5, 23.1, 27.1, 34.3
		- Other: 9.7, 9.9, 13.8, 14, 16.2, 17.3, 17.9, 18, 19.2, 20.5, 21.5, 23.1, 24.2, 24.6, 25.2, 25.8, 25.9, 26.2, 27.1, 28.8, 30.8, 34.3, 36.9, 38.8, 41.5, 43.4, 45.2, 46.6, 47.8, 49, 50, 50.8

- output
	- Format of the API search results returned. If not specified, default return is metalink for ASF API or JSON for SSARA Federated API. MAP setting valid only for SSARA Federated API.
	- Example:
		- output=JSON
	- Values:
		- CSV, JSON, KML, METALINK, COUNT, DOWNLOAD, GEOJSON
	- New Values:
		- COUNT returns the number of search results
		- GEOJSON returns the search results in a GeoJSON format
		- DOWNLOAD returns a bulk download script that includes the scenes returned by the search. See the [Bulk Download page](https://asf.alaska.edu/how-to/data-tools/data-tools/#bulk_download) for a full description and guide on using the bulk download script.
	- Note:
		- JSON returns more fields than CSV for the same query.

- platform
	- Remote sensing platform that acquired the data. Datasets that work together, such as Sentinel 1A/1B and ERS‌-1/2 have multi-platform aliases available (specifically, S1 and ERS).
	- Example:
		- platform=ALOS
		- platform=SA, SB
		- platform=S1
	- Values:
		- ‌ALOS, A3, AIRSAR, AS, ERS, ERS‌-1, E1, ERS‌-2, E2, JERS‌-1, J1, RADARSAT‌-1, R1, SEASAT, SS, S1, Sentinel, Sentinel-1, Sentinel-1A, SA, Sentinel-1B, SB, SMAP, SP, UAVSAR, UA

- polarization
	- A property of SAR electromagnetic waves that can be used to extract meaningful information about surface properties of the earth.
	- Example:
		- polarization=VV
		- polarization=VV, HH
		- polarization=VV%2bVH
		- polarization=Dual+VV
		- *Note*: Be sure to encode the space and +
	- Values:
		- AIRSAR: FULL
		- ALOS: QUADRATURE, HH+5SCAN, HH, HH+4SCAN, VV, HH+3SCAN, FULL, HH+HV, VV+VH
		- ERS-1: VV
		- ERS-2: VV
		- JERS-1: HH
		- RADARSAT-1: HH
		- SEASAT: HH
		- Sentinel-1A: VV, VV+VH, Dual VV, VV+VH, Dual HV, HH, HH+HV, VV, Dual VH
		- Sentinel-1B: VV, VV+VH, Dual VV, VV+VH, Dual HV, HH, HH+HV, VV, Dual VH
		- UAVSAR: FULL, HH

- polygon
	- Bounding polygon in the digital long/lat format; enter coordinates in counter clockwise direction, repeat the first point at the end to close the polygon: in the format ABCDA
	- Example:
		- polygon=-155.08,65.82,-153.5,61.91,-149.50,63.07,-149.94,64.55,-153.28,64.47,-155.08,65.82

- processingLevel
	- Level to which the data has been processed, also type of product, such as browse.
	- Example:
		- processingLevel=L0,L1
	- Values:
		- AIRSAR: 3FP, ATI, LTIF, PTIF, CTIF, PSTOKES, BROWSE, DEM, CSTOKES, JPG, LSTOKES, THUMBNAIL
		- ALOS: L1.0, L1.1, L1.5, RTC_LOW_RES, RTC_HI_RES, BROWSE, THUMBNAIL, METADATA, INTERFEROMETRY
		- ERS-1: L0, L1, BROWSE, THUMBNAIL
		- ERS-2: L0, L1, BROWSE, THUMBNAIL
		- JERS-1: L0, L1, BROWSE, THUMBNAIL
		- RADARSAT-1: L0, L1, BROWSE, THUMBNAIL
		- SEASAT: L1, BROWSE, THUMBNAIL
		- Sentinel-1A: METADATA_GRD, GRD_HS, GRD_HD, GRD_MS, GRD_MD, GRD_FS, GRD_FD, SLC, RAW, OCN, METADATA_RAW, METADATA, METADATA_SLC, THUMBNAIL
		- Sentinel-1B: METADATA_GRD, GRD_HS, GRD_HD, GRD_MS, GRD_MD, GRD_FS, GRD_FD, SLC, RAW, OCN, METADATA_RAW, METADATA, METADATA_SLC, THUMBNAIL
		- SMAP: L1A_Radar_RO_QA, L1B_S0_LoRes_HDF5, L1B_S0_LoRes_QA, L1B_S0_LoRes_ISO_XML, L1A_Radar_QA, L1A_Radar_RO_ISO_XML, L1C_S0_HiRes_ISO_XML, L1C_S0_HiRes_QA, L1C_S0_HiRes_HDF5, L1A_Radar_HDF5
		- UAVSAR: KMZ, PROJECTED, PAULI, PROJECTED_ML5X5, STOKES, AMPLITUDE, BROWSE, COMPLEX, DEM_TIFF, PROJECTED_ML3X3, METADATA, AMPLITUDE_GRD, INTERFEROMETRY, INTERFEROMETRY_GRD, THUMBNAIL

- relativeOrbit
	- Path or track of satellite during data acquisition. For UAVSAR it is the [Line ID](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.201268782.1252483948.1620685771-1930115146.1605056035).
	- Example:
		- relativeOrbit=500,550-580 or UAVSAR: relativeOrbit=05905
	- Values:
		- ALOS: 1-671
		- ERS-1: 0-2410
		- ERS-2: 0-500
		- JERS-1: 0-658
		- RADARSAT-1: 0-342
		- SEASAT: 1-243
		- UAVSAR: various

- maxResults
	- Maximum number of data records to return from your query.
	- Example:
		- maxResults=10

- processingDate
	- Limit results to records that have been processed at ASF since a given date and time.
	- Example:
		- processingDate=2017-01-01T00:00:00UTC

- start and/or end acquisition time
	- Date of data acquisition
	- Natural language, Use phrases such as:
		- start=3 months and a day ago
		- start=May 30, 2018
		- end=now
	- Example:
		- platform=SB&start=1+week+ago&end=now&maxresults=2000&output=csv
	- UTC
		- Enter a start date, end date or both to form a valid range.
	- Example:
		- start=2010-10-30T11:59:59UTC\&end=2018-10-01T00:00:00UTC

- season
	- Start and end day of year for desired seasonal range. This keyword is used in conjunction with start/end to specify a seasonal range within an overall date range in choosing values in alignment with Julian calendar.
	- Example:
		- season=1,31
		- season=45,67
		- season=360,10
	- Values:
		- 1 through 365

##Troubleshooting

- Trouble Area: Windows cURL “unrecognized protocol”
	- Reason: Invisible double quotes involuntarily inserted when copy/pasting example from web page
	- Remedy: Delete the visible quotes, which will delete the invisible quotes. Then retype quotes.
- Trouble Area: Download fails with “401 Unauthorized” or “Authorization failed”
	- Reason: Missing or invalid Earthdata username/password
	- Remedy: Check that you are correctly including your Earthdata username and password in your download command.  See search for examples.
- Trouble Area: Download fails with “401 Unauthorized” or “Authorization failed”
	- Reason: Special characters in Earthdata password
	- Remedy: Passwords with special characters need single quotes on Linux/Mac and double-quotes on Windows.  See search for examples.
- Trouble Area: Cookie request to /services/authentication/ fails with “410 Gone”
	- Reason: Cookie URL has been retired
	- Remedy: It’s no longer necessary to request an authorization cookie before downloading data.  See search for examples.
- Trouble Area: Can’t authenticate
	- Reason: You must agree to the new Terms of Service and set your Study area
	- Remedy: Log in to Vertex, accept the TOS, and set your Study Area.
- Trouble Area: Wget or cURL command copied from the webpage doesn’t work
	- Reason: Copy/paste over multiple lines introduces error
	- Remedy: Copy and paste one line, then the next line.
- Trouble Area: Wget or cURL command copied from the webpage doesn’t work
	- Reason: Quotes look the same but are interpreted differently
	- Remedy: Where single quotes are present, delete and retype them in the terminal window.
- Trouble Area: API request with ‘+’ in it fails
	- Reason: Some keywords are stored in the database as two words with a space between them, some as two words joined with a ‘+’.
	- Remedy: Try your API request with a ‘+’. if that doesn’t work, replace the ‘+’ with ‘%2B’. One of them will work.
- Trouble Area: API request fails
	- Reason: https is now required
	- Remedy: Make sure you are using https, not http.
- Trouble Area: Can’t download PALSAR data
	- Reason: You must agree to the PALSAR EULA in order to download PALSAR data
	- Remedy: Log in to Vertex and agree to the End User License Agreement, then retry downloading.
- Trouble Area: API request hangs, fails, or returns an error
	- Reason: Your URL may include spaces or special characters, especially if you are using the ‘intersectsWith’ keyword
	- Remedy: Remove spaces or replace with %20 or +
- Trouble Area: API request hangs or fails
	- Reason: Search may exceed 10,000 results
	- Remedy: Narrow search using more keywords to return fewer results or use keyword “maxResults”.
- Trouble Area: API request returns process ID (PID) numbers but does not return query results
	- Reason: URLs at the command line may require the “&” to be escaped
	- Remedy: Replace ampersand “&” with backslash ampersand “\&” in the URL. OR use double quotes ” ” around the URL; URLs submitted via the browser use ampersand “&” without the backslash.
- Trouble Area: Keyword not respected
	- Reason: Keywords are case sensitive
	- Remedy: Ensure that your keywords are capitalized (or not) just as in the Keyword List.
- Trouble Area: Keyword not respected
	- Reason: Keyword is deprecated
	- Remedy: See the keyword list for a list of deprecated keywords.
- Trouble Area: Certificate rejected
	- Reason: Third-party certificates out of date, a problem for https searches
	- Remedy: Use http OR disable certificate checks.
		- [curl](https://curl.se/docs/manpage.html) –insecure
		- [wget](https://www.gnu.org/software/wget/) –no-check-certificate
- Trouble Area: CSV vs JSON
	- Reason: The JSON output returns more fields than CSV
	- Remedy: It’s a feature. ASF may expand CSV output in the future. Meanwhile, use JSON to get the most information returned.

