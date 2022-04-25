# Event Search Type

## What is Event Search?
Event search harnesses the capabilities of SAR proccessing to monitor natural disasters. Currently supported hazards are volcanic eruptions and earthquakes.  Generated products include fully terrain corrected image time series, as well as interferometric SAR data over areas affected by natural disasters. To facilitate full automation, the processing flow is triggered automatically by existing hazard alert systems such as the USGS Earthquake Notification Service. Event monitoring through Vertex is based on technology developed within SARVIEWS through grant NNX12AQ38G. Visit the [Events (SARVIEWS) documentation](/datasets/events_about) for more information.

## How to use Vertex Event Search
Visit **[ASF's Vertex](https://search.asf.alaska.edu)** to begin using the Event search.

### **Beginning your Event Search**

- When you select **Event** search type, a search will be performed, and all available events will be displayed. As with other search types, there are filters available to limit or refine your search results.
- Click **Event Search** to enter an event name or partial name. You may also select the desired event from the drop down list displayed when you click the field.
- Under **Event Types**, you can choose which event types you wish to be displayed. Currently, there are Earthquake and Volcano events.
- You may select a **Start Date** or **End Date**.
- Click **Filters** for more options
	- You may toggle the **Active Events Only** switch to display only active events. The default is to display all events, including inactive events.
	- You may adjust the **Magnitude** slider to filter earthquakes by your desired magnitude range. *Note:* This filter applies only to earthquake events. If your search includes volcanoes, these will continue to be displayed in your search results.
- Once you have selected your desired Filters, click **Search** to update your search results.

#### **Product Filters**
- **Path and Frame Filters** are available. You may enter a single path or frame, or a range.
	- Click **Clear** to clear the entered path and frame values.
	- Note that **Path and Frame** will filter the displayed products within each event.
- Under **Product Type**, you may select one or more product types. This will filter the displayed products within each event.

### **Interacting with Event Search Results**
While in Event Search type, you will notice many familiar controls in the results panel. The events are shown in the left column. The Volcano and Earthquake icons note what type of event each result is. The center column lists the detail and metadata for the selected event. The Files for the selected event are shown in the right column.

**Result Panel Controls**

- At the top left of the results panel, you will see the number of events returned by your search.
- **Zoom** will *Zoom to results* magnifying the map area of the Earth where the event is located.
- **Queue** will *Add all results to Downloads* allowing you to add all event products to the download queue.
	- You may choose to add **All Event Products** or **Selected Event Products** to the download queue. You may select individual files in the right column.
- **Export** will download the Bulk Download Script. This Python script allows you to download all products from the selected scene.
- **On Demand** will allow you to *Add all results to On Demand queue* to do custom processing on the scenes. Depending on the types of files associated with the chosen event, you may be able to add RTC or InSAR jobs to your queue. To learn more click [here](https://hyp3-docs.asf.alaska.edu/using/vertex/).
- **Copy** allows you to copy either the **Scene IDs** or the download **URLs**.
	- You may choose to copy either **All** Scene IDs or URLs, or only copy **Selected** Scene IDs or URLs. You may select individual files in the right column.
- The Events column (left).
	- Each event has either an earthquake or a volcano icon to the left of it, to help you quickly identify the event type.
	- Click **Zoom to Event** to magnify the map area of the Earth where the event is located.
- The Event Detail column (middle).
	- The event details are listed here. This includes the event processing start and stop time. For earthquakes, the magnitude and depth is also displayed.
	- You may **Copy** the Event ID.
	- Click **SARVIEWS Event** to be directed to the SARVIEWS page for your chosen event.
	- For earthquake events, the **USGS ID** is listed. For volcanoes, the **Smithsonian ID** is listed. Click the link to go to the USGS or Smithsonian event page.
	- Adjust the **Geographic Search Polygon Scale** slider as desired. The Area of Interest polygon will also update on the map.
	- Once you are happy with the **Geographic Search Polygon Scale**, click **Geographic** to launch a Geographic search using the event's Area of Interest & dates.
	- Click **List** to launch a list search including all of the event's product scenes.
	- Click **SARVIEWS** to be directed to the SARVIEWS page for your chosen event.
	- The eye icon labeled **Open in Image Viewer** opens a larger browse viewer window.
		- *Note*: When viewing InSAR images in the image viewer, the wrapped browse image is displayed. The unwrapped browse image is available in the downloaded product.
		- In the browse viewer, **zoom** using the **+** or **-** buttons. You may also zoom and pan using the mouse.
		- Click or scroll through the thumbnails at the bottom to see other browse images for the selected event.
		- The scene metadata is listed on the right side of the browse viewer window.
		- Under **File**, you may click the button labeled **RTC GAMMA** or **INSAR GAMMA** for more options
			- Click **Download File** to download the selected product.
			- Click **Add file to queue** to add it to your Download queue.
			- Click **Reference Scenes** to copy the reference scene names to the clipboard. These may be saved in a file or used in **List** Search.
			- Click **Pin Browse to Map** to pin the browse image to the map. Once pinned, you may click this button again to unpin.
	- Click the **Download this image** icon to download the browse image.
	- Click the **Pin** icon to pin the selected browse image to the map. Once pinned, you may click this button again to unpin.
- The Files column (right).
	- The total number of files for the selected event is listed in this column.
	- You may sort the files using the **Sort By** and **Order** buttons at the top of the column.
		- Under **Sort By**, you may choose **Date**, **Path**, or **Frame**. 
		- Click the **Order Arrow** to switch between ascending and descending order.
	- Click **Product Criteria** to open the Search Filters.
	- Click the **checkboxes** next to each file to select or deselect the file. The selected files will be pinned onto the map. Once your desired files are selected, you may also use the **Download** or **Copy** controls in the top left of the results panel to interact with selected products.
	- Click **On Demand** to add the selected file to your On Demand queue for further processing.
	- Click the **Shopping Cart** icon to add the selected file to your Download queue.
	- Click **Download** to download the selected file.
	- *Note*: You must be logged in to download products.


