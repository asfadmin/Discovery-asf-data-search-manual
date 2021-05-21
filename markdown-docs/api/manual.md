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

