 ## Overview
Radar remote sensing has become a highly important data source in the Geosciences. This is mostly due to the ability of radar to penetrate clouds and operate independently of solar illumination. In addition radar sensors benefit from their ability to easily identify changes, track surface deformation with cm-accuracy, and map large areas regularly and over long time scales. It is not surprising that radar remote sensing is regularly used for studying earthquakes, volcanoes, and glaciers, as well as for the monitoring of anthropogenic activities such as hydrocarbon extraction, and groundwater pumping.

Within the SARVIEWS project, we are working on harnessing the capabilities of SAR by developing a fully automatic processing system that produces value-added products in support of monitoring natural disasters. The SARVIEWS processor is implemented in the Amazon Cloud and utilizes modern processing technology to generate geocoded and fully terrain corrected image time series, as well as interferometric SAR data over areas affected by natural disasters. To facilitate full automation, the SARVIEWS processing flow is triggered automatically by existing hazard alert systems such as the [USGS Earthquake Notification Service](https://earthquake.usgs.gov/ens/). Currently, SARVIEWS is supporting hazards related to volcanic eruptions and earthquakes. The inclusion of flood events is in preparation.

## Hazard Monitoring Criteria

SARVIEWS subscriptions are created in near real-time based upon reports from monitoring organizations such as the USGS and the Smithsonian Institution Global Volcanism Program. Subscriptions are created automatically after checking [Earthquake Notification Service (ENS)](https://earthquake.usgs.gov/ens/) emails and [Volcano Notification Service (VNS)](https://volcanoes.usgs.gov/vns2/) emails, or the Smithsonian Institution Global Volcanism Program's weekly updates for active volcanoes outside the United States.

### Earthquakes

Earthquake subscriptions are created if the earthquake event has potential surface deformation, which is roughly assesed based upon the following logic:

<table>
  <thead>
    <tr>
      <th>Magnitude</th>
      <th>Shallow: 0-35 km</th>
      <th>Medium: 35-100 km</th>
      <th>Deep: 100+ km</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Large: Mag 7.5+</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Medium: Mag 7.0 - 7.5</td>
      <td>If within 75 km of coast</td>
      <td>If within 25 km of coast</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Small: Mag 6.0 - 7.0</td>
      <td>If within 25 km of coast</td>
      <td>If within 0.5 km of coast</td>
      <td>No</td>
    </tr>
  </tbody>
</table>

These criteria provide a quick estimate of the strength of the earthquake in relation to depth and the distance from land in order to limit event subscriptions to only those with the potential for surface deformation. This simple logic is created upon the ENS email, and does not wait for more data to calculate surface deformation with conventional seismologic methods. Once created, earthquake subscriptions process Sentinel data for 6 months from the date of the earthquake.

### Volcanoes

Criteria for volcano subscriptions reply on the VNS Activity Notice emails for domestic volcanoes, and the Smithsonian Institution Global Volcanism Program's RSS feed for international volcanoes. If a volcano is flagged as a WARNING Alert level, or a RED aviation code, a subscription is created for the volcano. Globally, if the volcano's activity is high enough to be triggered and posted by the Global Volcanism Program, SARVIEWS creates a subscription. Volcano subscriptions process data starting 1 year prior to the activity, and continue indefinitely until volcano activity levels return to normal.

## On Demand Processing

The SARVIEWS processor takes full advantage of the extensive SAR archives available at the Alaska Satellite Facility (ASF), NASA Distributed Active Archive Center (DAAC) for Synthetic Aperture Radar data. Through ASF, SARVIEWS has efficient access to the historic and future acquisitions of the Sentinel-1 sensors, a spaceborne SAR system launched and operated by the European Space Agency. Sentinel-1 images all of Earth’s landmasses every 6 - 12 days, providing valuable data for hazard monitoring.

To efficiently access and process the incoming stream of Sentinel-1 SAR data, SARVIEWS leverages ASF HyP3, a cloud-based processing system that generates value-added SAR products on demand. On demand processing via HyP3 is also available from [ASF's Vertex](https://search.asf.alaska.edu/#/?topic=onDemand). Through HyP3, SARVIEWS has full access to the benefits of the cloud, such as elastic scaling of compute resources and efficient cloud-based storage and distribution. For more information, please visit the [HyP3 Documentation](https://hyp3-docs.asf.alaska.edu/).

## FAQ

**Is SARVIEWS free?**

All of the SARVIEWS products available in Vertex are freely available for download and use without restrictions. These are value-added products created from freely available Sentinel-1 data, with no login necessary. Please credit both ESA and SARVIEWS when using our data.

**How do I bulk download products?**

When you choose to copy the URLs for any event products, you will get a list of links to all of the selected SARVIEWS products. You may paste these links into a file, such as a .csv. To download the products, use a program such as wget with the '-i' option. For example:

    ## move to the location you want the products to be downloaded
    cd path/to/destination

    ## download with the -i option to specify the .csv
    wget -i path/to/download_all.csv

You may also download and run the Python Bulk Download script to download your selected event products.

**When will the next product become available?**

SARVIEWS automatically creates and archives products as soon as they become available. If a product is missing for a subscrciption, it means that the subscription is waiting on a new scene to be acquired, or it's still processing. Generally, there are 12 days between most Sentinel overpasses.

**What software is used to process SARVIEWS data?**

SARVIEWS events are processed using [GAMMA Remote Sensing](https://www.gamma-rs.ch/software) software tools through the ASF HyP3 engine. For more information on algoritm specifics, please visit the [ASF HyP3 products page](https://hyp3-docs.asf.alaska.edu/products/).

## Acknowledgements & Contact

The SARVIEWS effort was funded by the [NASA Applied Sciences Disasters Program](https://appliedsciences.nasa.gov/what-we-do/disasters) through grant NNX12AQ38G. Sentinel-1 data is provided by the European Space Agency through their [Copernicus](https://www.esa.int/Applications/Observing_the_Earth/Copernicus) program. Access to Sentinel-1 data is provided by the [NASA Alaska Satellite Facility (ASF) DAAC](https://asf.alaska.edu/). SARVIEWS products contain modified Copernicus Sentinel data. Contributions to SARVIEWS were made by the SARVIEWS project team including FJ Meyer, S Arko, JB Nicoll, K Hogenson, W Gong, DB McAlpin, P Webley and many more. We owe thanks to the ASF Advanced Prototype Development (APD) and ASF HyP3 teams for supporting the robust implementation of SARVIEWS procedures and for their assistance with moving SARVIEWS into the cloud. Ongoing contributions are being made by the many beta-testers of our service.

For more information on SARVIEWS, please contact [Franz Meyer](mailto:fjmeyer@alaska.edu). You may also view the [Twitter](https://twitter.com/SARevangelist?) account.

## Useful Links

- The University of Alaska Fairbanks' (UAF) Microwave Remote Sensing class: [UAF GEOS 657](https://radar.community.uaf.edu/)
- Newcastle University's Generic Atmospheric Correction Online Service for InSAR: [GACOS](http://www.gacos.net/)
- The German Aerospace Center (DLR) for Satellite Based Crisis Information: [DLR ZKI](https://www.dlr.de/eoc/desktopdefault.aspx/tabid-12797#gallery/36755)
- NASA's Jet Propulsion Laboratory's Advanced Rapid Imaging and Analysis (ARIA) Center for Natural Hazards: [JPL ARIA](https://aria.jpl.nasa.gov/)
- ESA's Copernicus Emergency Management Service: [Copernicus EMS](https://emergency.copernicus.eu/)
- The Center for Observation and Modelling of Earthquakes, Volcanoes and Tectonics: [COMET InSAR](https://comet.nerc.ac.uk/earth-observation/insar/)
- ESA's Thematic Exploitation Platforms: [ESA TEPs](https://tep.eo.esa.int/home)

