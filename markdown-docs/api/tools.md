# Search API Tools

Searches may be executed in a variety of ways, depending on your needs. On this page, you will find syntax & character encoding tips, and further information on some of the ways to run Search API queries.

## Syntax and Character Encoding

**Syntax tips**

1. A "?" separates the endpoint URL from the keywords.
2. Keywords are joined by a "&". Some operating systems or programs may require a "\&"
3. There may not be any spaces or parentheses in the URL string. See below for how to encode these characters.

**Character Encoding:**

>space
>
>replace with '%20'. Use '+'  in keyword values
>
>(
>
>replace with '%28'
>
>)
>
>replace with '%29'
>

For a complete list of URL codes, please see [URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp).

**Escaping Characters**

If you are running Search API queries via command line, you may need to escape characters. Escaping a character tells the command line interface to interpret the character literally. Some characters that need to be escaped include spaces and ampersands (&).

For more information on escaping characters, please see the [Bash Scripting Guide](https://tldp.org/LDP/abs/html/escapingsection.html). For Windows users, more information can be found [here](https://ss64.com/nt/syntax-esc.html).

## Program Details

You may use a program to assist you with Search API queries. This section will provide some details on a few of the programs you can use to write & run Search API queries and some example commands for each.

- [aria2](https://wiki.archlinux.org/title/aria2)
- [Wget](https://www.gnu.org/software/wget/)
- [cURL](https://curl.se/docs/manpage.html)

Both [Wget](http://wget.addictivecode.org/FrequentlyAskedQuestions.html?action=show&redirect=Faq#download) and [cURL](https://curl.se/) are often installed on Linux systems. cURL is part of the Mac OS, and Wget can be installed. Microsoft Windows OS does not come with either installed, but both can be downloaded. cURL is easier to set up on a Windows machine. [aria2](https://aria2.github.io/) can be installed on Windows, Mac, or Linux systems.

### Examples using aria2

aria2c can be used to download results from the Search API with a single command. You will need to include your Earthdata username and password, all desired keywords & values, and ensure that output=metalink.

**Aria2 — Linux/Mac Example - Download Known Scene**

      aria2c --http-auth-challenge=true --http-user=CHANGE_ME --http-passwd='CHANGE_ME' "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

**Aria2 — Windows Example - Download Known Scene**

      aria2c --check-certificate=false --http-auth-challenge=true --http-user=CHANGE_ME --http-passwd="CHANGE_ME" "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

**Aria2 — Download Based on Platform and Time-Range Search**

      aria2c --http-auth-challenge=true --http-user=CHANGE_ME --http-passwd='CHANGE_ME' "https://api.daac.asf.alaska.edu/services/search/param?platform=Sentinel-1A&intersectsWith=point(-122.425 37.77)&start=2016-07-01T00:00:00&output=metalink"

You can store your login credentials in a config file, instead of including them in every download command.

**aria2 - Linux/Mac Example — Create and use a configuration file**

      echo 'http-user=CHANGE_ME' >> aria2.conf
      echo 'http-passwd=CHANGE_ME' >> aria2.conf
      chmod 600 aria2.conf

      aria2c --conf-path=aria2.conf --http-auth-challenge=true "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

Additional aria2 options are available in the [aria2 manual](http://aria2.sourceforge.net/manual/en/html/aria2c.html).

Refer to the complete documentation on [configuration files for aria2](https://aria2.github.io/manual/en/html/aria2c.html#aria2-conf).

### Examples using Wget

Once you have the download URL, you can download files individually using Wget. You can find the download URL for your desired results by first using outputs csv, json, metalink, or geojson.

**Wget - Linux/Mac Example — Download a file**

      wget -c --http-user=CHANGE_ME --http-password='CHANGE_ME' "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

**Wget - Windows Example — Download a file**

      wget --check-certificate=off -c --http-user=CHANGE_ME --http-password="CHANGE_ME" "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

      wget -c --http-user=CHANGE_ME --http-password="CHANGE_ME" "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

You can store your login credentials in a config file, instead of including them in every download command.

**Wget - Linux/Mac Example — Create and use a configuration file**

      echo 'http_user=CHANGE_ME' >> wget.conf
      echo 'http_password=CHANGE_ME' >> wget.conf
      chmod 600 wget.conf

      export WGETRC="wget.conf"
      wget -c "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

You can also send results to a file on your PC

**Example — query results sent to a metalink file**

      wget -O myfilename.metalink https://api.daac.asf.alaska.edu/services/search/param?intersectsWith=point%28-119.543+37.925%29\&platform=ALOS\&output=metalink

**Visualize Example - Mac/Linux**

      wget -O myfilename.kml https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550\&output=KML

**Download Example - Windows**

      wget -c -O myfilename.metalink https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550\&output=METALINK

Additional Wget options are available in the [GNU Wget Manual](https://www.gnu.org/software/wget/manual/wget.html).

Refer to the complete documentation on [configuration files for Wget](https://www.gnu.org/software/wget/manual/html_node/Startup-File.html#Startup-File).

### Examples using cURL

**cURL - Mac/Linux Example**

      curl https://api.daac.asf.alaska.edu/services/search/param?platform=R1\&absoluteOrbit=25234\&output=CSV

**cURL - Windows Example**

Note: Copy/pasting quotation marks sometimes causes errors. Delete and re-type the quotes after pasting.

      curl "https://api.daac.asf.alaska.edu/services/search/param?platform=R1&absoluteOrbit=25234&output=CSV" > myfilename.csv

You can also send results to a file on your PC

**Mac/Linux Example — query results sent to a metalink file**

      curl https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP021910740,ALPSRP085800750 >myfilename.metalink

**Windows Example — query results sent to a metalink file**

      curl "https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP021910740,ALPSRP085800750" > myfilename.metalink

**Search Example - Mac/Linux**

      curl https://api.daac.asf.alaska.edu/services/search/param?platform=r1\&asfframe=300\&output=CSV > myfilename.csv

**Search Example - Windows**

      curl  "https://api.daac.asf.alaska.edu/services/search/param?platform=r1&asfframe=300&output=CSV" > myfilename.csv

**Visualize Example - Windows**

      curl "https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550&output=KML" >myfilename.kml

**Download Example - Windows**

      curl -L "https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550&output=METALINK" >myfilename.metalink

## POST Requests
Some keywords and endpoints will accept a POST request. The POST examples below are using cURL.

**POST Example - WKT output from file**

      curl -X POST -F 'files=@/path/to/file.geojson' 'https://api.daac.asf.alaska.edu/services/utils/files_to_wkt'

**POST Examples - intersectsWith Keyword**

      curl -X POST -F 'intersectsWith=LINESTRING(-97.1191 26.4312,-95.5371 29.1522,-83.7598 29.993,-81.5625 25.4036)' 'https://api.daac.asf.alaska.edu/services/search/param'

You can add additional parameters to your POST request with the -F argument for each desired parameter.

      curl -X POST -F 'platform=S1' -F 'output=geojson' -F 'maxresults=10' -F 'intersectsWith=POINT(-102.4805 38.7541)' 'https://api.daac.asf.alaska.edu/services/search/param'

For further reading, see [POST requests](https://en.wikipedia.org/wiki/POST_(HTTP))

## Web Browser

You may run the Search API queries directly in a web browser of your choice. Simply copy and paste the query into a web browser. Any errors will be returned in JSON format.

You will need to use URL encoding for spaces and parentheses. Please refer to the Character Encoding section or see [URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp) for more details.

