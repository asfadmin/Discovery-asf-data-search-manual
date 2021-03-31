# Vertex Getting Started User Guide

- If you do not already have one, create a free **[Earthdata Login account](https://urs.earthdata.nasa.gov/users/new)**.
- Go to **[Vertex](https://search.asf.alaska.edu)**
	- Log in by clicking the **Sign in** icon in the top right of the window. Use your Earthdata Login username and password.
- Search Type allows you to choose between *Geographic*, *List*, *Baseline*, *SBAS*, and *On Demand Products* search types.

## *Geographic* Search Options

- In the top left corner of the map, there are buttons that allow you to change your **map projection**, **zoom**, and **map view**.
	- By default, the map is in equatorial projection. You may click **Arctic map view** or **Antarctic map view** to change your map projection. Click **Equatorial map view** to switch back to the equatorial projection.
	- You may click the **Zoom In** or **Zoom Out** icons to adjust your zoom.
	- By default, the map layer is in **Satellite View**. You may click **Street View** to switch your map layer.
- Navigate to your area of interest by dragging the map while holding down the left mouse button.
- By default, the map-drawing tool is a bounding box. Click on the map once to specify the starting corner, move the mouse, then click again to finish the box. Additional drawing tool options are available in the toolbar at the top of the screen, including *point*, *linestring*, and *polygon* options.
	- **Point** allows you to define an area of interest by clicking on the map to place a point.
	- **Line** allows you to define an area of interest over a series of line segments by clicking on the map multiple times. Double-click to stop adding segments.
	- **Polygon** allows you to define an area of interest over an arbitrary polygon. You will receive an error message at the bottom of the window if there was a problem with the polygon (self-intersecting, reversed polygon winding order, etc.).
	- **Box** allows you to define an area of interest over a lat/long-aligned bounding box by clicking once to set one corner, and again to set the opposite corner.
	- Once a shape has been drawn, select the **Edit current area of interest** icon on the toolbar to move, add, and delete points. Select the **Draw new area of interest** icon to create a new AOI.
- **Dataset** enables you to choose the dataset of interest.
	- If you need more information about a particular dataset, click on the appropriate question mark icon in the Dataset selector.
- **Area of Interest** gives you the option of importing an area of interest as a geospatial file or by entering a set of geographic coordinates.
	- Click on the down arrow next to **Area of Interest** in the top menu
	- Click the **Import Area of Interest** button in the Options window
	- Click **Select Files** and navigate to a folder on your computer, or drag and drop files into the box. *GeoJSON*, *shapefiles*, and *KML* files are supported provided they are in a latitude/longitude-based coordinate system, such as WGS84.
		- When importing a *GeoJSON* file, all geometries in the file will be included. If multiple geometries are found, a convex hull will be used to represent them in the search.
		- *Shapefiles* can be either a single *.shp* file, multiple shapefile components (*.shp, .shx, .dbf*), or a *zip* file containing one or more shapefile components. At a minimum, the *.shp* component must be included in all cases.
	- An area of interest may also be defined by a set of coordinates entered in the Options window.
		- Coordinates should be entered as decimal degrees in *well-known text* (WKT) format. Coordinates entered as a comma-separated long/lat string (e.g. -97.38,36.46,-53.44,36.46...) will be automatically converted by Vertex to WKT format.
	- You can save the coordinates of a search so they can be used to exactly recreate an area of interest in later searches.
		- Once the **Area of Interest** has been set, mouse over the coordinates. A *Copy to clipboard* icon will appear. Click on the icon and paste the coordinates into a new search or to a text file for later use.
		- Note: See the section **Other Vertex Options** for additional ways of saving searches.
	- At any time you can clear your search area by clicking on the **Trash can** icon in the top menu bar.
- **Filters...** enables you to further refine your search
	- **Date Filters** Search dates are optional, so they default to empty.  If you are searching for specific dates, you can define the date range further in the **Start Date** and **End Date** fields. The date picker will automatically constrain your selection to a valid range for the selected dataset.
		- *Note*: this information may also be found by clicking on the question mark icon for a dataset.
		- **Seasonal Search** allows constraining the search to certain annual periods within an overall range of dates.  Click the Seasonal Search toggle and additional options will appear, allowing you to enter an overall date range (*Start Date/End Date*) and the seasonal range (*Season Start Day/Season End Day*).
	- **Additional Filters** allow for additional parameters to be applied to narrow your search and reduce the number of results. Not all filters will be available for all datasets.
		- **File Type** – Limit the search to specific types of files. Multiple selections allowed.
		- **Beam Mode** – Limit the search to specific beam modes. Multiple selections allowed.
		- **Polarization** – Limit the search to specific polarizations. Multiple selections allowed.
		- **Direction** – Limit the search to a specific orbit direction.
		- **Subtype** – Limit the search to a specific mission spacecraft.
	- **Path and Frame Filters** are available for select datasets. You may enter a single path or frame, or a range. Due to inconsistent Sentinel-1 framing, we recommend searching for a frame of interest by ±1-2 frames.
- Once all parameters have been chosen, click **SEARCH**. Search results will appear in the footer area of the Vertex window, and on the map.
	- *Note*: The number of files that are predicted to match the current search parameters is displayed under the SEARCH button. If there are no predicted matches, the search button will be greyed out and display NO RESULTS.

## *List* Search Options

- Selecting **List Search** opens the *List Search* window and allows you to enter a list of scenes or file names.
	- **Scene** allows searching for specific scene names (granule names), and the results will include any files that are part of those scenes.
	- **File** allows searching for specific file names (product names), and the results will only include exactly those files.
- **Edit List** opens the *List Search* window so you can make changes to your list
- Once all parameters have been chosen, click **SEARCH**. Search results will appear in the footer area of your browser window, and on the map.
	- *Note*: The number of files that are predicted to match the current search parameters is displayed under the SEARCH button. If there are no predicted matches, the search button will be greyed out and will display NO RESULTS.

## *Baseline* Search Options

- Selecting **Baseline Search** provides a space to enter the name of a Reference Scene, and will then search for all secondary scenes that match the coverage area of the Reference.
	- *Note*: If there are no matching scenes, the RESULTS button will be greyed out and will display NO RESULTS.
- Once a Reference Scene has been entered, click **SEARCH**. Search results will appear under the map. Clicking on the *Zoom to results* icon at the top of the left results column will display the location of the stack of scenes on the map.
- The graph displays the Temporal and Perpendicular (spatial) relationship of the secondary scenes to the Reference.
- Clicking on **Baseline Criteria...** above the graph will open the *Baseline Search* window. Using the sliders, the Temporal and Perpendicular extents can be adjusted to limit the number of secondary scenes displayed in the results.
- For further information on **Baseline**, please see the [Baseline documentation](/vertex/baseline).

## *SBAS* Search Options

- Selecting **SBAS Search** provides a space to enter the name of a Reference Scene, and will search for all secondary scenes that match the coverage area of the Reference. It is an alternate method used for Interferometric SAR (InSAR) processing, similar to Baseline.
	- *Note*: If there are no matching scenes, the RESULTS button will be greyed out and will display NO RESULTS.
- Once a Reference Scene has been entered, click **SEARCH**. Search results will appear under the map. Clicking on the *Zoom to results* icon at the top of the left results column will display the location of the stack of scenes on the map.
- The chart displays the Temporal and Perpendicular (spatial) relationship of the secondary scenes to the Reference.
	- **Zoom In** and **Zoom Out** buttons are available above the chart.
	- The **Zoom to Fit** button ensures that all pairs are visible on the chart.
	- The **Custom Pair** buttons allow you to add or delete a custom pair.
	- The **SBAS Criteria...** button allows you to specify start and end dates to refine your results.
- For further information on **SBAS**, please see the [SBAS documentation](/vertex/sbas).

## *On Demand Products* Search Options

- Selecting **On Demand Products** allows you to view your submitted On Demand jobs. *Note*: You must be signed in to access this. If you are not signed in, this search option will be greyed out and you will not be able to select it.
- **Project Name** allows you to limit your search to a specific project name. As you start typing, auto-complete options will become available with the project names you have previously used.
- **Date Filters** Search dates are optional, so they default to empty.  If you are searching for specific dates, you can define the date range further in the **Start Date** and **End Date** fields. *Note*: These dates filter by the scene date, not the date it was processed.
- **Product/Source Scene** allows you to enter the product name or source scene name to limit your search. This field will also accept a partial string from either the product or source scene in lieu of the full name.
- **Job Status** allows you to limit your search to specific statuses. Multiple selections allowed.
- *Note*: Jobs expire 14 days after you submit them. Expired products still appear in search results, however, you may no longer download or add them to your cart. You can easily identify your expired products by the **Expired** tag next to the product name.
- For further information on **On Demand Products**, please see the [documentation](https://hyp3-docs.asf.alaska.edu/).

## Search Results

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
		- The **Citation** button opens a new window with citation guidance for published works using data, imagery, or tools accessed through ASF.
		- The **More Like This** button creates a search based on the selected scene’s path and frame.
	- The **Files** column (right) displays a list of files available for the currently selected scene. You may download files immediately or add them to your download queue by clicking on the appropriate icon.
		- Clicking on the right arrow in front a file (product) name will expand the file to show the ancillary files included. These files may be downloaded individually or added to the download queue.
			- You must be signed in to Vertex for this feature to work.
			- This feature is not available for all datasets.

## On Demand Queue

- Clicking on the **three boxes** icon in the header, labeled **On Demand**, will display a drop down list of options.
- **On Demand Queue** will open the On Demand queue.
	- The **Project Name** field allows you to create a name for the files you want to submit for processing. The character limit is 20.
	- The **RTC Gamma Options** allow you to change some processing options. The options you select will apply to all files in your queue.
		- The question mark icon next to the options gives you more details on each option.
	- The list of files you have added to your queue is listed below the options. The X allows you to remove any files you wish from the queue.
	-  **Clear** will clear all files from the queue. The option *Restore* will be displayed to allow you to undo this action.
	- The allowed number of jobs left is displayed at the bottom of the queue. There are 200 jobs allotted to each user per month.
	- When you are satisfied with your selections, click **Submit Jobs** at the bottom. This will submit your jobs for processing. *Note*: The button will display the number of jobs you are submitting.
		- If there are any errors, such as missing DEM coverage, an error message will display.
		- Once the jobs are successfully submitted, a popup will display at the bottom of your browser window, listing the number of jobs sent for processing. You may click to dismiss. Or you may click **View On Demand Queue** to be redirected to the On Demand Products search.
- **Submitted Products** will switch to On Demand Products search type & will display your submitted products.
- **Help** will send you to the [On Demand documentation](https://hyp3-docs.asf.alaska.edu/)
- *Note*: You must be signed in to see your Submitted Products, and to process new On Demand products.

## Downloads Queue

- Clicking on the **cart icon** in the header, labeled **Downloads**, will display the contents of your current download queue.
	- Within the download queue, the list of files you have selected to download is displayed with some basic information on each file, such as file type and size.
		- File IDs (names) can be copied with the **copy** icon
		- Files can be individually downloaded with the **cloud** icon
		- Items can be removed from the queue with the **X**
	- **Clear** will clear all files from the queue. The option *Restore* will be displayed to allow you to undo this action.
	- **Copy File IDs** will copy the file names of all files in the queue for use elsewhere. *For example*, this list could then be pasted into the *List Search* window.
	- **Data Download** is used to download multiple products, with either the *Download Python Script (.py)* option or *Metalink (metalink)* file option.
	- **Metadata Download** is used to export the contents of the download queue to a *CSV*, *KML*, or *GeoJSON* file. The *KML* and *GeoJSON* files provided by this feature are compatible with the *Geographic Search Import* feature.

## Other Vertex Options

- In the top left corner of the map, there are buttons that allow you to change your **map projection**, **zoom**, and **map view**. These are visible in all search types.
	- By default, the map is in equatorial projection. You may click **Arctic map view** or **Antarctic map view** to change your map projection. Click **Equatorial map view** to switch back to the equatorial projection.
	- You may click the **Zoom In** or **Zoom Out** icons to adjust your zoom.
	- By default, the map layer is in **Satellite View**. You may click **Street View** to switch your map layer.
- Click on the **three-bars menu icon** next to the **Sign in** icon to display the menu options.
	- **Copy Search Link** will copy all the search parameters that have been set in the current search as a URL. The URL can then be pasted into a browser search bar to recreate the search exactly, or pasted into a document and saved to recreate the search later.
	- **Share With Email** will open a new email with the URL of the search to send to others.
	- **Help & Tutorials** provides both illustrated and video demonstrations on the basic steps for setting up a search and viewing the results.
	- **What’s New** provides updated information on new features and changes that have been added to Vertex for improved performance and functionality.
- Click on the **Sign in** icon once you are signed in to display the user options.
	- **Saved Searches** opens a list of searches that you have named and saved. Click on the magnifying glass icon to load the search settings.
	- **Search History** opens a list of your 10 last searches that were not named and saved. Click on the magnifying glass icon to load the search settings.
	- **Preferences** opens a window that allows you to set search preferences for dataset, max results, and map layer. These preferences will be saved and applied to future searches.
- Click on the **down arrow** on the **Search**
	- **Clear Search** will clear all search parameters that have been set except for Search Type and Dataset.
	- **Save Search^** allows you to name and save all current search parameters in Saved Searches.
	- **Saved Searches^** opens a list of searches that you have named and saved. Click on the magnifying glass icon to load the search settings.
	- **Search History^** opens a list of your 10 last searches that were not named and saved. Click on the magnifying glass icon to load the search settings.
	- **Help & Tutorials** provides both illustrated and video demonstrations on the basic steps for setting up a search and viewing the results.
		- ^*Note*: You must be signed in to Vertex for these options to be available.
- *Note*: **Saved Searches** and **Search History** are available through both the Sign in menu and the Search button down arrow menu.
- Click into the **Search all ASF** field on the grey header bar to perform a search. Inputs into this field will search across all ASF websites.
	- You may also click the **microphone** icon if you prefer to use voice search.
	- As you type or speak, the results of your search will be displayed in a list below the field. Clicking a result from the list will open a new browser tab.
	- You may click the **magnifying glass** icon to expand the search results. This will open in the same browser window. To close and return to Vertex, click the **X** near the top right of your screen.
