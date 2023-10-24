# Baseline Search Type

## What is Baseline?
Baseline uses information from two synthetic aperture radar (SAR) images of the same target area acquired at different times (temporal baseline) and from slightly different satellite orbit positions (perpendicular baseline). The Vertex baseline tool helps you identify and select scene pairs that are appropriate for Interferometric SAR (InSAR) processing. It provides visualization of perpendicular and temporal baseline data, and allows you to easily change the reference scene used in any stack.

## How to use Vertex Baseline Tool
Visit **[ASF's Vertex](https://search.asf.alaska.edu)** to begin using the Baseline tool.
![type:video](https://www.youtube.com/embed/Xp5bgvi2pEM)

### **Beginning your Baseline Search**

- If you do not have a particular reference scene chosen, you can search for scenes using the geographic or list search. The center column will have a button under the metadata titled ***Baseline Tool*** for any scenes that are eligible. You may click this button to be directed to a Baseline search. The Baseline search will use the chosen scene as the reference scene.

- If you do have a particular reference scene chosen, you can select ***Baseline*** from the Search Type dropdown list. You may enter your reference scene and hit ***Search***.

### **Interacting with Baseline Search Results**
While in Baseline Search type, you will notice many familiar controls in the results panel. The scenes are shown in the left column. The perpendicular and temporal baselines are listed next to each scene. The center column lists the metadata for the selected scene, and includes the **Set as Reference** button, which allows you to set any scene in the stack as the reference scene. The Baseline Chart is shown in the right column.

**Result Panel Controls**

- At the top left of the results panel, you will see the number of scenes listed.
- **Zoom** will *Zoom to results* magnifying the map area of the Earth where the scenes are located.
- **Queue** will *Add all results to Downloads* allowing you to add all scenes to the download queue.
- **On Demand** will allow you to *Add all results to On Demand queue* to do custom processing on the scenes. To learn more click [here](https://hyp3-docs.asf.alaska.edu/using/vertex/). You may also choose to *Create Subscription*. More details about subscriptions can be found [here](https://hyp3-docs.asf.alaska.edu/using/subscriptions/).
- **Export** will allow you to *Download data/metadata* for all scenes in the stack.
- In the left column, **Queue** will *Add scene files to downloads* for the selected scene only.
- Under the metadata in the center column, **Set as Reference** will allow you to set any scene in the stack as the reference scene. When you select this, both the chart and the baseline values will be updated automatically.

**Chart Controls**

- The dots on the chart represent individual scenes. Hovering over them will list their temporal and perpendicular values. You may also click on any point to select that scene. The metadata in the center column will be updated.
- Located above the chart, there are labels and corresponding colors. These indicate how the reference scene, selected scene, and any scenes in your download queue are displayed on the chart. Some datasets include a shaded area which indicates the critical baseline.
- You may zoom and pan the chart.

#### Baseline Criteria

- You may click **Baseline Criteria...** above the chart for additional options.
	- You can adjust the sliders to change the perpendicular and temporal values that you wish to be included in your results.
	- You can enter a start and end date.
	- Changing any criteria will automatically update the list of scenes and the chart.

## Next Steps
Once you are satisfied with your result set, you can use the download queue to manage and download baseline results. More information about the download queue can be found in the [Vertex Getting Started User Guide](/vertex/manual).

If you wish to create interferograms, custom processing is now available through Vertex. Details are available in the On Demand Queue section of the [Vertex Getting Started User Guide](/vertex/manual). You can find more information about creating interferograms with ASF's custom processing through the [HyP3 documentation](https://hyp3.asf.alaska.edu/about).
