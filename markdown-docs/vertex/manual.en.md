# Vertex Getting Started User Guide

- If you do not already have one, create a free **[Earthdata Login account](https://urs.earthdata.nasa.gov/users/new)**.
- Go to **[Vertex](https://search.asf.alaska.edu)**
	- Log in by clicking the **Sign in** icon in the top right of the window. Use your Earthdata Login username and password.
	![type:video](https://www.youtube.com/embed/j_Db_ipKLos)
- Search Type allows you to choose between all available search types.

## Language Options

In the top right menu, next to the **Sign In** icon, there are language control options. Vertex currently offers English and Spanish. If your browser is set to one of the available languages, Vertex will default to that language. You may click the button and select your desired language from the drop down list. You may also set a default language in your **Preferences**. 

## *Geographic* Search Options

![type:video](https://www.youtube.com/embed/JovQ-rG9ZJE)

- In the top left corner of the map, there are buttons that allow you to change your **map projection**, **zoom**, and **map view**.
	- By default, the map is in equatorial projection. You may click **Map View** and select **Arctic map view** or **Antarctic map view** to change your map projection. Click **Equatorial map view** to switch back to the equatorial projection.
	- You may click the **Zoom In** or **Zoom Out** icons to adjust your zoom.
	- The default map layer is satellite. You may click the **Layers** button and select **Satellite View** or **Street View** to switch your map layer.
		- You may click **Overview Map** to add an overview map in the top right corner of the map. Click it again to turn off the overview map.
		- You may click **Gridlines** to add a graticule overlay to the map. Click it again to turn off the overlay. *Note*: This is currently only available in the equatorial map view.
	- You may click **Opacity** and adjust the slider as desired to change the opacity of browse images displayed on the map.
- Navigate to your area of interest by dragging the map while holding down the left mouse button.
- By default, the map-drawing tool is a bounding box. Click on the map once to specify the starting corner, move the mouse, then click again to finish the box. Additional drawing tool options are available in the toolbar at the top of the screen, including *point*, *linestring*, and *polygon* options.
	- **Point** allows you to define an area of interest by clicking on the map to place a point.
	- **Line** allows you to define an area of interest over a series of line segments by clicking on the map multiple times. Double-click to stop adding segments.
	- **Polygon** allows you to define an area of interest over an arbitrary polygon. You will receive an error message at the bottom of the window if there was a problem with the polygon (self-intersecting, reversed polygon winding order, etc.).
	- **Box** allows you to define an area of interest over a lat/long-aligned bounding box by clicking once to set one corner, and again to set the opposite corner.
	- Once a shape has been drawn, select the **Edit current area of interest** icon on the toolbar to move, add, and delete points. Select the **Draw new area of interest** icon to create a new AOI.
	- Clicking **Upload Goespatial File** brings up the Area of Interest dialog window. You may enter a WKT string, upload a geospatial file, or enter a location.
- **Dataset** enables you to choose the dataset of interest.
	- If you need more information about a particular dataset, click on the appropriate question mark icon in the Dataset selector.
- **Filters...** enables you to further refine your search

### Area of Interest Options

- **Area of Interest** gives you the option of entering a set of geographic coordinates, importing an area of interest as a geospatial file, or searching for a location. Click on the down arrow next to **Area of Interest** in the top menu.
	- An area of interest may be defined by a set of coordinates entered in the **Area of Interest WKT** window.
		- Coordinates should be entered as decimal degrees in *well-known text* (WKT) format. Coordinates entered as a comma-separated long/lat string (e.g. -97.38,36.46,-53.44,36.46...) will be automatically converted by Vertex to WKT format.
	- To upload a geospatial file, click **Select Files** and navigate to a folder on your computer, or drag and drop files into the box. *GeoJSON*, *shapefiles*, and *KML* files are supported provided they are in a latitude/longitude-based coordinate system, such as WGS84.
		- When importing a *GeoJSON* file, all geometries in the file will be included. If multiple geometries are found, a convex hull will be used to represent them in the search.
		- *Shapefiles* can be either a single *.shp* file, multiple shapefile components (*.shp, .shx, .dbf*), or a *zip* file containing one or more shapefile components. At a minimum, the *.shp* component must be included in all cases.
	- To enter a location, click the **Search for a Location** field, and start typing the name of the location. Select your desired location from the drop down list. 
		- Once you have selected a location, it will be geocoded into WKT format coordinates.
	- You can save the coordinates of a search so they can be used to exactly recreate an area of interest in later searches.
		- Once the **Area of Interest** has been set, a *Copy to clipboard* icon will appear. Click on the icon and paste the coordinates into a new search or to a text file for later use.
		- Note: See the section **Other Vertex Options** for additional ways of saving searches.
	- At any time you can clear your search area by clicking on the **Clear** button.

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

### Date Filters

- **Date Filters** Search dates are optional, so they default to empty.  If you are searching for specific dates, you can define the date range further in the **Start Date** and **End Date** fields. The date picker will automatically constrain your selection to a valid range for the selected dataset.
	- *Note*: this information may also be found by clicking on the question mark icon for a dataset.
	- **Seasonal Search** allows constraining the search to certain annual periods within an overall range of dates.  Click the Seasonal Search toggle and additional options will appear, allowing you to enter an overall date range (*Start Date/End Date*) and the seasonal range (*Season Start Day/Season End Day*).

### Additional Filters

![type:video](https://www.youtube.com/embed/Vd9eDL9KVK4)

- **Additional Filters** allow for additional parameters to be applied to narrow your search and reduce the number of results. Not all filters will be available for all datasets.
	- **File Type** – Limit the search to specific types of files. Multiple selections allowed.
	- **Beam Mode** – Limit the search to specific beam modes. Multiple selections allowed.
	- **Polarization** – Limit the search to specific polarizations. Multiple selections allowed.
	- **Direction** – Limit the search to a specific orbit direction.
	- **Subtype** – Limit the search to a specific mission spacecraft.

### Path and Frame Filters

- **Path and Frame Filters** are available for select datasets. You may enter a single path or frame, or a range. Due to inconsistent Sentinel-1 framing, we recommend searching for a frame of interest by ±1-2 frames.
- The maximum number of results is displayed below the **SEARCH** button. Click the **down arrow** to choose your preferred maximum results.
	- You may click **API URL...** in order to generate the API URL matching your current search parameters. This will open a new window.
		- **Amount** allows you to set the maximum results.
		- **Format** allows you to choose your preferred output format.
		- The **Copy** icon next to the URL will copy the URL. It can be pasted into a browser search bar to perform the API search, or pasted into a document and saved.
		- **API Docs** will send you to the [API Documentation](https://asf.alaska.edu/api/).
		- **Download Results** will download the results in the specified output format.
- Once all parameters have been chosen, click **SEARCH**. Search results will appear in the footer area of the Vertex window, and on the map.
	- *Note*: The number of files that are predicted to match the current search parameters is displayed under the SEARCH button. If there are no predicted matches, the search button will be greyed out and display NO RESULTS.

## *List* Search Options

![type:video](https://www.youtube.com/embed/oetqxZkqVZM)

- Selecting **List Search** opens the *List Search* window and allows you to enter a list of scenes or file names.
	- **Scene** allows searching for specific scene names (granule names), and the results will include any files that are part of those scenes.
	- **File** allows searching for specific file names (product names), and the results will only include exactly those files.
- **Edit List** opens the *List Search* window so you can make changes to your list
- Once all parameters have been chosen, click **SEARCH**. Search results will appear in the footer area of your browser window, and on the map.
	- *Note*: The number of files that are predicted to match the current search parameters is displayed under the SEARCH button. If there are no predicted matches, the search button will be greyed out and will display NO RESULTS.

### List Search File Import
You may **drag and drop files** into the box provided on the **Scene** or **File** tabs. Each tab lists the file types accepted at the bottom. Vertex will parse the scene or file names from your uploaded file.

- *Note*: Each file type requires a specific format. Files exported from Vertex will have the correct format.

- **CSV** requires a column labeled "Granule Name" for a scene list search. It requires an additonal "Processing Level" column for a file list search.
- **GeoJSON** requires a field labeled "granuleName" for scene list search. It requires a field labeled "fileID" for file list search.
- **Metalink** requires a structure formatted as
```
<metalink>
    <files>
        <file name="[Scene-Name.zip]"></file>
        <file name ="...
        ...</file>
    </files>
</metalink>
```

- **KML** requires a structure formatted as
```
<kml>
    <Document>
        <Placemark>
            <name>[Scene Name]</name>
        </Placemark>
    </Document>
</kml>
```

## *Baseline* Search Options

![type:video](https://www.youtube.com/embed/Xp5bgvi2pEM)

- Selecting **Baseline Search** provides a space to enter the name of a Reference Scene, and will then search for all secondary scenes that match the coverage area of the Reference.
	- *Note*: If there are no matching scenes, the RESULTS button will be greyed out and will display NO RESULTS.
- Once a Reference Scene has been entered, click **SEARCH**. Search results will appear under the map. Clicking on the *Zoom to results* icon at the top of the left results column will display the location of the stack of scenes on the map.
- The graph displays the Temporal and Perpendicular (spatial) relationship of the secondary scenes to the Reference.
- Clicking on **Baseline Criteria...** above the graph will open the *Baseline Search* window. Using the sliders, the Temporal and Perpendicular extents can be adjusted to limit the number of secondary scenes displayed in the results.
- For further information on **Baseline**, please see the [Baseline documentation](/vertex/baseline).

## *SBAS* Search Options

![type:video](https://www.youtube.com/embed/bQPdtuobdcg)

- Selecting **SBAS Search** provides a space to enter the name of a Reference Scene, and will search for all secondary scenes that match the coverage area of the Reference. It is an alternate method used for Interferometric SAR (InSAR) processing, similar to Baseline.
	- *Note*: If there are no matching scenes, the RESULTS button will be greyed out and will display NO RESULTS.
- Once a Reference Scene has been entered, click **SEARCH**. Search results will appear under the map. Clicking on the *Zoom to results* icon at the top of the left results column will display the location of the stack of scenes on the map.
- The chart displays the Temporal and Perpendicular (spatial) relationship of the secondary scenes to the Reference.
	- **Zoom In** and **Zoom Out** buttons are available above the chart.
	- The **Zoom to Fit** button ensures that all pairs are visible on the chart.
	- The **Custom Pair** buttons allow you to add or delete a custom pair.
	- The **SBAS Criteria...** button allows you to specify additional criteria to refine your results, such as start and end dates, seasonal date settings, and latitudinal overlap threshold settings.
- For further information on **SBAS**, please see the [SBAS documentation](/vertex/sbas).

## *Event* Search Options

- Selecting **Event** allows you to view and search the products created for hazard monitoring.
- **Event Search** allows you to enter an event name. You may enter the full name or a partial string.
- **Event Types** allows you to filter which types of events you wish to see. Currently, there are earthquake and volcano events.
- **Start Date** and **End Date** allow you to specify a date range for events.
- Additional options may be found under **Filters**.
	- You may toggle the **Active Events Only** switch to display only active events. The default is to display all events, including inactive events.
	- You may adjust the **Magnitude** slider to filter earthquakes by your desired magnitude range. *Note:* This filter applies only to earthquake events. If your search includes volcanoes, these will continue to be displayed in your search results.
- For further information on **Event** search, please see the [Event Search documentation](/vertex/events).

## *On Demand Products* Search Options

- Selecting **On Demand Products** allows you to view your submitted On Demand jobs. *Note*: You must be signed in to access this. If you are not signed in, this search option will be greyed out and you will not be able to select it.
- **Project Name** allows you to limit your search to a specific project name. As you start typing, auto-complete options will become available with the project names you have previously used.
- **Date Filters** Search dates are optional, so they default to empty.  If you are searching for specific dates, you can define the date range further in the **Start Date** and **End Date** fields. *Note*: These dates filter by the scene date, not the date it was processed.
- **Product/Source Scene** allows you to enter the product name or source scene name to limit your search. This field will also accept a partial string from either the product or source scene in lieu of the full name.
- **Job Status** allows you to limit your search to specific statuses. Multiple selections allowed.
- *Note*: Jobs expire 14 days after you submit them. Expired products still appear in search results, however, you may no longer download or add them to your cart. You can easily identify your expired products by the **Expired** tag next to the product name.
- For further information on **On Demand Products**, please see the [documentation](https://hyp3-docs.asf.alaska.edu/).

## *Derived Datasets* Search Options

- Selecting **Derived Datasets** allows you to view and download products from ASF's catalog of datasets.
- Each dataset listed includes a short description.
- Click **More Info** to view more information about the dataset.
- Click **Download** to view and download available products for your chosen dataset. *Note*: The download link will open in a new browser window.
- For further information on **Derived Datasets**, please see the [Derived Datasets documentation](/vertex/derived_datasets/).

## Search Results

![type:video](https://www.youtube.com/embed/wp8Xt_Y4T84)

- In Vertex, a **scene** is considered to be a package containing all **files**, or products, that are related to a specific location and time.
	- *For example*, the column on the left of the Results panel displays the scenes returned from a search. The column on the right displays the file contents of each scene.
- The maximum number of files that a search will return is displayed under the SEARCH button.
	- This number can be adjusted by clicking on the down arrow.
	- The total number of files that match the search parameters is also displayed.
- The Results header bar.
	- The **Zoom** button will zoom-in to the location of all scenes on the map.
	- The **Queue** button will add all scenes to the download queue.
	- The **On Demand** button will allow you to choose which eligible scenes to add to the On Demand Queue for further processing.
	- The **Raw** button will show or hide raw files. *Note*: This button is applicable for Sentinel-1 scenes only.
	- The **Export** button will allow you to export data or metadata for all scenes in the results.
	- The **Expired** button will show or hide expired On Demand files. *Note*: This button is only available in the **On Demand Products** search type.
	- *Note*: Not all buttons are available on all search types.
- The **Scenes** column (left).
	- Click on the cart icon next to a scene name to add all the scene’s files to the download queue. The cart changes appearance when this is done.
	- Click on the zoom icon next to a scene name to zoom-in to the scene’s location on the map.
- To view more information about a scene, click on the scene in the left column and the **Scene Detail** and **Files** columns will populate.
	- The **Scene Detail** column (center) provides a more detailed description of the scene, including *Start Date/Time*, *Beam Mode*, *Path*, *Frame*, *Flight Direction*, *Polarization*, *Absolute Orbit*, and a browse image (if available). Not all scenes will have all the extra information.
		- The **Baseline Tool** button opens the ASF Baseline Tool, which is used for creating InSAR stacks.
		- The **SBAS Tool** button opens the ASF SBAS Tool, which is another method of creating InSAR stacks.
		- The **More Like This** button creates a search based on the selected scene’s path and frame.
		![type:video](https://www.youtube.com/embed/h7vmrcpMd60)
		- The **Citation** button opens a new window with citation guidance for published works using data, imagery, or tools accessed through ASF.
		- **Download this Image** downloads the browse image.
		- The eye icon labeled **Open in Image Viewer** opens a larger browse viewer window.
			- In the browse viewer, **zoom** using the **+** or **-** buttons. You may also zoom and pan using the mouse.
			- Click or scroll through the thumbnails at the bottom to see other browse images for scenes returned by your search.
			- By default, the **Only display scenes with a browse image** box is checked. You may uncheck this to see all scenes returned by your search. Scenes without a browse image will show a thumbnail listing *No Browse Available*.
			- The scene metadata is listed on the right side of the browse viewer window.
	- The **Files** column (right) displays a list of files available for the currently selected scene. You may download files immediately or add them to your download queue by clicking on the appropriate icon.
		- Clicking on the right arrow in front a file (product) name will expand the file to show the ancillary files included. These files may be downloaded individually or added to the download queue.
			- You must be signed in to Vertex for this feature to work.
			- This feature is not available for all datasets.

## On Demand Queue

![type:video](https://www.youtube.com/embed/AxhYMBzycuY)

- Clicking on the **three boxes** icon in the header, labeled **On Demand**, will display a drop down list of options.
- **On Demand Queue** will open the On Demand queue.
	- The different jobs types in your queue are separated by tabs along the top of the queue. The job types currently available are **RTC GAMMA**, **InSAR GAMMA**, and **autoRIFT**. You may click on a tab to select it. The selected tab is highlighted.
	- For **RTC GAMMA** and **InSAR GAMMA** jobs, there are additional processing options available.  The options you select will apply to all files of that job type in your queue.
		- You may hover over each option to display a tool tip with details on the option.
	- Choose your desired sorting with the **Sort Criteria** and **Sort Order** drop down boxes.
		- Under **Sort Criteria**, you may choose to sort files by *Start Date* of the file, or by *Date Added* to the queue.
		- Under **Sort Order**, you may choose to sort files by *Latest* or most recent, or by *Oldest*.
	- The list of files you have added to your queue is listed below the options. The X allows you to remove any files you wish from the queue.
	-  **Clear** will list some options for clearing files from your queue. You can choose to clear an individual tab, or you can choose **Clear All Processing Types** to clear all files from the queue. If you choose to clear all files, the option *Restore* will be displayed to allow you to undo this action.
	- The number of jobs remaining is displayed at the bottom of the queue. There are 1,000 jobs allotted to each user per month. If you have too many jobs in your queue, a message stating the number of extra jobs will be displayed at the top of the queue. The **Sumbit** button will be greyed out.
	- When you are satisfied with your selections, click **Submit Jobs** at the bottom. This will display the Review Submission window.
		- The **Project Name** field allows you to create a name for the files you want to submit for processing. The character limit is 20. This field is optional.
		- You may select or deselect the checkboxes to submit only the job types you wish.
		- Select **Cancel** to return to the queue without submitting any files for processing.
		- Click **Submit** to submit your jobs. *Note:* The Submit button will list the number of jobs you are submitting.
		- If there are any errors, such as missing DEM coverage, an error message will display.
- **Submitted Products** will switch to On Demand Products search type and will display your submitted products.
- **On Demand (HyP3) Docs** will send you to the [On Demand documentation](https://hyp3-docs.asf.alaska.edu/)
- *Note*: You must be signed in to see your Submitted Products and to submit jobs from the On Demand Queue.

## Downloads Queue

![type:video](https://www.youtube.com/embed/cRjqbLNv4Aw)

Enhanced download queue functionality is now available on Google Chrome browser. See [below](/vertex/manual/#google-chrome-browser) for more information.

- Clicking on the **cart icon** in the header, labeled **Downloads**, will display the contents of your current download queue.
	- Within the download queue, the list of files you have selected to download is displayed with some basic information on each file, such as file type and size.
		- File IDs (names) can be copied with the **copy** icon.
		- Files can be individually downloaded with the **cloud** icon. You may also right click to save or copy the download URL.
		- Items can be removed from the queue with the **X**.
	- **Clear** will clear all files from the queue. The option *Restore* will be displayed to allow you to undo this action.
	- **Copy File IDs** will copy the file names of all files in the queue for use elsewhere. For example, this list could then be pasted into the *List Search* window.
	- **Copy URLs** will copy the download URLs of all files in the queue.
	- **Data Download** is used to download multiple products, with either the *Download Python Script (.py)* option or *Metalink (metalink)* file option.
	- **Metadata Download** is used to export the contents of the download queue to a *CSV*, *KML*, or *GeoJSON* file. The *KML* and *GeoJSON* files provided by this feature are compatible with the *Geographic Search Import* feature.

### Google Chrome Browser

Enhanced download queue functionality is available on Google Chrome browser. Please note, this improved functionality is not supported while using incognito mode.

- Click on the **cart icon** in the header, labeled **Downloads** to open your download queue.
	- Next to each file, you may click the **cloud** icon to begin the download.
		- As the download begins, a progress indicator lists the percentage downloaded. Once the dowload has completed, the icon appears as a **check mark** to indicate the file has been downloaded.
		- While the file is downloading, you may click the progress indicator to stop the download.
	- Under **Data Download**, you may select **Download All**. This will download 3 files at a time until all products in your cart have been downloaded. The same progress indicators and checkmarks will be displayed to let you know the status of each download in your queue.
		- When you click **Download All**, a dialog box will appear:
			1. Navigate to the folder where you wish to save the files and click *Select*.
			2. Click *View Files* to allow the download to continue. 
			3. Click *Save Changes* to save your download folder preferences. This will persist as long as the Vertex browser window remains open.
	- If you **Clear** the products in your queue, the download progress and completion indicators will reset. You may add the products to your queue again if desired.
	- *Note*: You must be signed in to download files. If you are not signed in, when you click to begin a download, you will be redirected to the sign in page first.

## Other Vertex Options

- In the top left corner of the map, there are buttons that allow you to change your **map projection**, **zoom**, and **map view**. *Note:* Available map controls vary by search type.
![type:video](https://www.youtube.com/embed/qrUnsbZTVnA)
	- By default, the map is in equatorial projection. You may click **Map View** and select **Arctic map view** or **Antarctic map view** to change your map projection. Click **Equatorial map view** to switch back to the equatorial projection.
	- You may click the **Zoom In** or **Zoom Out** icons to adjust your zoom.
	- The default map layer is satellite. You may click the **Layers** button and select **Satellite View** or **Street View** to switch your map layer.
		- You may click **Overview Map** to add an overview map in the top right corner of the map. Click it again to turn off the overview map.
		- You may click **Gridlines** to add a graticule overlay to the map. Click it again to turn off the overlay. *Note*: This is currently only available in the equatorial map view.
	- You may click **Opacity** and adjust the slider as desired to change the opacity of browse images displayed on the map.
- Click on the **down arrow** on the **Search**
	- **Clear Search** will clear all search parameters that have been set except for Search Type and Dataset.
	- **Saved Searches** opens a submenu.
	![type:video](https://www.youtube.com/embed/io4OQumWrJA)
		- **Save Search** allows you to name and save your current search.
		- **View Searches...** opens a list of searches that you have named and saved. Click on the magnifying glass icon to load the search settings.
		- **Search History...** opens a list of your 10 last searches that were not named and saved. Click on the magnifying glass icon to load the search settings.
	- **Saved Filters** opens a submenu.
		- **Save Filters** allows you to save your current filter set.
		- **View Filters...** allows you to view your saved filter sets. Click Apply Filters to apply them to your current search.
	- **Share Search** opens a submenu.
		- **Copy Search Link** will copy all the search parameters that have been set in the current search as a URL. The URL can then be pasted into a browser search bar to recreate the search exactly, or pasted into a document and saved to recreate the search later.
		- **Share With Email** will open a new email with the URL of the search to send to others.
	- **Help & Tutorials** provides both illustrated and video demonstrations on the basic steps for setting up a search and viewing the results.
		- *Note*: You must be signed in to Vertex for these options to be available.
	- **Export** opens a submenu.
		- **Export Python** will provide a Python code snippet to recreate the current search using the Python search module asf_search. It also provides a link to the asf_search documentation. 
		- **Export API** will provide the API URL to recreate the current search using the SearchAPI. It also provides a link to the SearchAPI documentation. 
- Click **Help** for additional help options.
	- **Watch Our Tutorials** provides both illustrated and video demonstrations on how to use Vertex.
	- **Read Our User Guide** opens the Vertex documentation in a new tab.
	- **Read Our On Demand Guide** opens the On Demand documentation in a new tab.
	- **Find SAR Data Using ASF API** opens the SearchAPI documentation in a new tab.
	- **Learn More About ASF & SAR** opens the ASF website in a new tab.
	- **Statistics and GitHub Repository** provides links to our GitHub Vertex repository.
- Click on the **Sign in** icon once you are signed in to display the user options.
	- **Saved Searches** opens a list of searches that you have named and saved. Click on the magnifying glass icon to load the search settings.
	- **Search History** opens a list of your 10 last searches that were not named and saved. Click on the magnifying glass icon to load the search settings.
	- **Saved Filters** opens a list of filters that you have saved. Click *Apply Filters* to apply the selected filter set to your search.
	- **Preferences** opens a window that allows you to set search preferences for language, theme, dataset, max results, map layer, and default filter presets. These preferences will be saved and applied to future searches.
- *Note*: **Saved Searches**, **Saved Filters**, and **Search History** are available through both the Sign in menu and the Search button down arrow menu.
- Click into the **Search all ASF** field on the grey header bar to perform a search. Inputs into this field will search across all ASF websites.
	- You may also click the **microphone** icon if you prefer to use voice search.
	- As you type or speak, the results of your search will be displayed in a list below the field. Clicking a result from the list will open a new browser tab.
	- You may click the **magnifying glass** icon to expand the search results. This will open in the same browser window. To close and return to Vertex, click the **X** near the top right of your screen.