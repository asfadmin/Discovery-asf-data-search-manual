# SBAS Search Type

## What is SBAS?
SBAS is an acronym for **short baseline subsets**. It is a technique used in interferometry.

## What are some uses for SBAS?
SBAS is widely used in the geosciences community. It works best for natural environments over a large scale and can be used to look at gradual change over time. SBAS requires input of a series of interferograms and the final output is a time series showing motion.

One advantage of SBAS is that you are not restricted to a single interferogram. You can see gradual changes over time. It can also be useful for older datasets which sometimes have irregular acquisitions. The temporal and spatial filtering can help increase the accuracy for measuring deformation.

You must choose which interferograms to use, which can require some experimentation. The Vertex SBAS tool simplifies this by providing good visualization and making it easier for you to quickly determine which scenes to use.

There are other preferred approaches for urban environments, or higher resolution needs. However, regardless of your analysis needs, the SBAS tool is a useful overview tool and can also be used as a 2-D baseline plot. It gives a comprehensive, but rapid visualization of scenes.

## How to use Vertex SBAS Tool
Visit **[ASF's Vertex](https://search.asf.alaska.edu)** to begin using the SBAS tool.

#### **Beginning your SBAS Search**

- If you do not have a particular reference scene chosen, you can search for scenes using the geographic or list search. The center column will have a button under the metadata titled ***SBAS Tool*** for any scenes that are eligible. You may click this button to be directed to an SBAS search. The SBAS search will use the chosen scene as the reference scene.

- If you do have a particular reference scene chosen, you can select ***SBAS*** from the Search Type dropdown list. You may enter your reference scene and hit ***Search***.

#### **Interacting with SBAS Search Results**
While in SBAS Search type, you will notice many familiar controls in the results panel. The pairs are shown in the left column. The center column lists the metadata for the two endpoints of the selected pair. The SBAS Chart is shown in the right column.

**Result Panel Controls**

- At the top left of the results panel, you will see the number of pairs listed.
- **Zoom** will *Zoom to results* magnifying the map area of the Earth where the scenes are located.
- **Queue** will *Add all to Downloads* allowing you to add all scenes to the download queue.
- **On Demand** will allow you to *Add all to On Demand queue* to do custom processing on the scenes. To learn more click [here](https://hyp3-docs.asf.alaska.edu/using/vertex/).
- **Pairs** will *Download Pair CSV* which will list the scenes in each pair and the download URL for each.

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
- If you wish to stop adding a pair after you have begun, you may click the **Square symbol** to *Stop adding custom pair*.
- If you wish to delete an added pair, you may click on the dotted pair line and click the **Minus symbol** to *Remove custom pair*. Note that only manually added pairs may be deleted.
