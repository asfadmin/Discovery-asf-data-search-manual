# Search API Tools

This section will provide some example commands & details on some of the programs you can use to write & run Search API queries.

**Program Details**

- [aria2](https://wiki.archlinux.org/title/aria2)
- [Wget](https://www.gnu.org/software/wget/)
- [cURL](https://curl.se/docs/manpage.html)

## Examples using aria2

aria2c can be used to download results from the Search API with a single command. You will need to include your Earthdata username and password, all desired keywords & values, and ensure that output=metalink.

**Aria2 — Linux/Mac Example - Download Known Scene**

      aria2c –http-auth-challenge=true –http-user=CHANGE_ME –http-passwd=’CHANGE_ME’ “https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink”

**Aria2 — Windows Example - Download Known Scene**

      aria2c --check-certificate=false --http-auth-challenge=true --http-user=CHANGE_ME --http-passwd="CHANGE_ME" "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

**Aria2 — Download Based on Platform and Time-Range Search**

      aria2c –http-auth-challenge=true –http-user=CHANGE_ME –http-passwd=’CHANGE_ME’ “https://api.daac.asf.alaska.edu/services/search/param?platform=Sentinel-1A&intersectsWith=point(-122.425 37.77)&start=2016-07-01T00:00:00&output=metalink”

You can store your login credentials in a config file, instead of including them in every download command.

**aria2 - Linux/Mac Example — Create and use a configuration file**

      echo 'http-user=CHANGE_ME' >> aria2.conf
      echo 'http-passwd=CHANGE_ME' >> aria2.conf
      chmod 600 aria2.conf

      aria2c --conf-path=aria2.conf --http-auth-challenge=true "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

Additional aria2 options available at the [aria2 manual](http://aria2.sourceforge.net/manual/en/html/aria2c.html).

Refer to the complete documentation on [configuration files for aria2](https://aria2.github.io/manual/en/html/aria2c.html#aria2-conf).

## Examples using Wget

Once you have the download URL, you can download files individually using Wget. You can find the download URL using outputs csv, json, metalink, geojson, or jsonlite.

**Wget - Linux/Mac Example — Download a file**

      wget -c --http-user=CHANGE_ME --http-password='CHANGE_ME' "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

**Wget - Windows Example — Download a file**

      wget --check-certificate=off -c --http-user=CHANGE_ME --http-password="CHANGE_ME" "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

      wget -c –http-user=CHANGE_ME –http-password=’CHANGE_ME’ “https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip”

You can store your login credentials in a config file, instead of including them in every download command.

**Wget - Linux/Mac Example — Create and use a configuration file**

      echo 'http_user=CHANGE_ME' >> wget.conf
      echo 'http_password=CHANGE_ME' >> wget.conf
      chmod 600 wget.conf

      export WGETRC="wget.conf" wget -c "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

You can also send results to a file on your PC

**Example — query results sent to a metalink file**

      wget -O myfilename.metalink https://api.daac.asf.alaska.edu/services/search/param?intersectsWith=point%28-119.543+37.925%29\&platform=ALOS\&output=metalink

**Visualize Example - Mac/Linux**

      wget -O myfilename.kml https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550\&output=KML

**Download Example - Windows**

      wget -c -O myfilename.metalink https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550\&output=METALINK

Additional Wget options at the [GNU Wget Manual](https://www.gnu.org/software/wget/manual/wget.html).

Refer to the complete documentation on [configuration files for Wget](https://www.gnu.org/software/wget/manual/html_node/Startup-File.html#Startup-File).

## Examples using cURL

**cURL - Mac/Linux Example**

      curl https://api.daac.asf.alaska.edu/services/search/param?platform=R1\&absoluteOrbit=25234\&output=CSV

**cURL - Windows Example**

Note: Copy/pasting quotation marks sometimes causes errors on Windows. Delete and re-type the quotes after pasting.

      curl “https://api.daac.asf.alaska.edu/services/search/param?platform=R1&absoluteOrbit=25234&output=CSV” > myfilename.csv

You can also send results to a file on your PC

**Mac/Linux Example — query results sent to a metalink file**

      curl https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP021910740,ALPSRP085800750 >myfilename.metalink

**Windows Example — query results sent to a metalink file**

      curl “https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP021910740,ALPSRP085800750” > myfilename.metalink

**Search Example - Mac/Linux**

      curl https://api.daac.asf.alaska.edu/services/search/param?platform=r1\&asfframe=300\&output=CSV > myfilename.csv

**Search Example - Windows**

      curl  “https://api.daac.asf.alaska.edu/services/search/param?platform=r1&asfframe=300&output=CSV” > myfilename.csv

**Visualize Example - Windows**

      curl “https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550&output=KML” >myfilename.kml

**Download Example - Windows**

      curl -L “https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550&output=METALINK” >myfilename.metalink
