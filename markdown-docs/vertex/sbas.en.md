# SBAS Search Type

## What is SBAS?
SBAS is an acronym for **short baseline subsets**. It is a technique used in interferometry. The Vertex SBAS tool provides perpendicular and temporal baseline data, as well as scene pairs, for a chosen reference scene.

## What are some uses for SBAS?
SBAS is widely used in the geosciences community. It works best for natural environments over a large scale and can be used to look at gradual change over time. SBAS requires input of a series of interferograms and the final output is a time series showing motion.

One advantage of SBAS is that you are not restricted to a single interferogram. You can see gradual changes over time. It can also be useful for older datasets which sometimes have irregular acquisitions. The temporal and spatial filtering can help increase the accuracy for measuring deformation.

You must choose which interferograms to use, which can require some experimentation. The Vertex SBAS tool simplifies this by providing good visualization and making it easier for you to quickly determine which scenes to use.

There are other preferred approaches for urban environments, or higher resolution needs. However, regardless of your analysis needs, the SBAS tool is a useful overview tool and can also be used as a 2-D baseline plot. It gives a comprehensive, but rapid visualization of scenes.

Further reading on baseline, including descriptions of multiple approaches, can be found [here](https://www.sciencedirect.com/science/article/pii/S0924271615002415). A case study comparison of PS and SBAS can be found [here](https://ieeexplore.ieee.org/document/5692806).

## How to use Vertex SBAS Tool
Visit **[ASF's Vertex](https://search.asf.alaska.edu)** to begin using the SBAS tool.
![type:video](https://www.youtube.com/embed/bQPdtuobdcg)

### **Beginning your SBAS Search**

- If you do not have a particular reference scene chosen, you can search for scenes using the geographic or list search. The center column will have a button under the metadata titled ***SBAS Tool*** for any scenes that are eligible. You may click this button to be directed to an SBAS search. The SBAS search will use the chosen scene as the reference scene.

- If you do have a particular reference scene chosen, you can select ***SBAS*** from the Search Type dropdown list. You may enter your reference scene and hit ***Search***.

### **Interacting with SBAS Search Results**
While in SBAS Search type, you will notice many familiar controls in the results panel. The pairs are shown in the left column. The center column lists the metadata for the two endpoints of the selected pair. The SBAS Chart is shown in the right column.

**Result Panel Controls**

- At the top left of the results panel, you will see the number of pairs listed.
- **Zoom** will *Zoom to results* magnifying the map area of the Earth where the scenes are located.
- **Queue** will *Add all to Downloads* allowing you to add all scenes to the download queue.
- **On Demand** will allow you to *Add all to On Demand queue* to perform custom processing on the scenes. You may also choose to *Create Subscription*.
	- You may choose from **RTC GAMMA**, **InSAR GAMMA**, or **autoRIFT**, depending on your needs. RTC GAMMA processing is performed on the individual scenes in your result set. InSAR GAMMA and autoRIFT processing are performed on the pairs in your result set.
	- **Note:** Currently, only scenes with beam mode IW are eligible for On Demand processing.
- **Pairs** will *Download Pair CSV* which lists the scenes in each pair and the download URL for each. It also includes the baseline values.
- In the left column, highlight the desired pair and click the **On Demand** icon to *Add pair to On Demand queue*. You may choose *InSAR GAMMA* or *autoRIFT* processing for each pair you wish to add.

**Chart Controls**

- The dots on the chart represent individual scenes. Hovering over them will list their temporal and perpendicular information. The lines represent the pairs.
- You may use the mouse to navigate the chart. There are **Zoom In** and **Zoom Out** buttons located above the chart. The **Zoom to Fit** button will fit all of the pairs into the visible chart.
- You may click on any pair line in the chart. When you do, the selected pair is highlighted in red and the metadata for that pair is shown in the center column.
- You may adjust the temporal and perpendicular baseline using the sliders on the chart.
- You may also create your own pair if desired:
	1. Under **Custom Pair**, click the **Plus symbol** to *Start adding custom pair*.
	7. Click the dot on the chart representing the first scene.
	2. Click the dot on the chart representing the second scene.
	3. The new pair is created, and the pair detail is added to the bottom of the result list. Manually added pairs will be displayed with a dotted line on the chart.
	4. **Note:** You may also add custom pairs to the On Demand queue.
- If you wish to stop adding a pair after you have begun, you may click the **Square symbol** to *Stop adding custom pair*.
- If you wish to delete an added pair, you may click on the dotted pair line and click the **Minus symbol** to *Remove custom pair*. Note that only manually added pairs may be deleted.

#### Gaps Detected Warning Message

If there are gaps detected in your SBAS pairs, a warning message will be displayed. It is recommended to avoid disconnected InSAR pair networks. Disconnected pair networks make it difficult to create unbiased estimates of InSAR velocities within a time-series analysis. 

If you wish to eliminate the gaps, you may modify your search filters, such as increasing the temporal baseline until all scenes are connected. You may also add manual pairs for the missing connections. Once all scenes have at least one connection, the warning message will disappear. 

#### SBAS Criteria

- Click **SBAS Criteria...** for additional filtering options.
	- You may enter a **Start** or **End** date, or select dates on the calendar.
	- **Seasonal Search** allows constraining the results to certain annual periods within an overall range of dates.  Click the Seasonal Search toggle and additional options will appear, allowing you to adjust the sliders to specify a seasonal range (*Season Start Day/Season End Day*).
	- **Latitudinal Overlap** allows you to set the overlap threshold for pairs. Filtering out non-overlapping pairs can reduce errors in On Demand InSAR processing.
		- **No Overlap Threshold** is the default. All pair results are returned, including any non-overlapping pairs.
		- **Any Overlap Threshold** will ensure that all pairs have some overlap. Any non-overlapping pairs will be filtered out of the results.
		- **50% Overlap Threshold** ensures that all pairs have approximately 50% overlap. Any pairs with less overlap will be filtered out of the results.

## Next Steps
The next step is creating interferograms. You may do this through On Demand processing in Vertex. First, you would add some or all of the pairs to the On Demand queue as InSAR jobs. In the queue, there are limited options available for customizing your InSAR processing. You may also specify a project name. Submit the queue when you have selected all desired options. When the interferograms are completed, you can view and download them by using the On Demand Products search type in Vertex.

For areas with glacial ice, autoRIFT is another processing option. Similar to InSAR, you would add some or all pairs to the On Demand queue as autoRIFT jobs. There are no additional customization options available for autoRIFT processing, however you can still specify a project name. When autoRIFT processing is completed, you can view and download the products by using the On Demand Products search type in Vertex.

More detail can be found in the [Vertex User Guide](/vertex/manual). Help documentation, including videos, is also available in Vertex [here](https://search.asf.alaska.edu/#/?maxResults=250&topic=onDemand).

To learn more, you may also see the [On Demand documentation](https://hyp3-docs.asf.alaska.edu/).
