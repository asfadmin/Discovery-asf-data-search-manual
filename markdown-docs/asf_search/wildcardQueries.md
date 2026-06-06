# Wildcard Queries

asf-search and SearchAPI support querying scene names via wildcards (* and ?) with the `granule_list` keyword and is also available on `dataset` search type in Vertex. This enables searching metadata embedded in scene names. Below are examples of useful queries with certain datasets.

## NISAR

NISAR data product names contain a few pieces of metadata that aren't directly searchable by additional attributes in CMR or aren't searchable params in asf-search

For a breakdown of NISAR data product naming conventions see: https://nisar-docs.asf.alaska.edu/naming-conventions/


### CRID Version Number
`CRID` version is available in CMR but isn't a searchable field in asf-search.

match all Level 2 NISAR products with CRID version X05010
`NISAR_L2_*X05010*`

match all NISAR science products with CRID version X05010 and above
`NISAR_L?_*X0501?*`

match all NISAR products with CRID version P05012 and above
`NISAR_*P05012*`

### Freq A & B Polarizations
While asf-search provides searching on these `mainBandPolarization` and `sideBandPolarization` fields you can't search strictly exclusively on single band data without getting possibly getting both bands in results. Data products denote when a band isn't used with `NA`.

Data products that strictly contain frequency A HH data 

`
NISAR_L?_\*_SHNA\*
`

### Stack ids

Stack IDs are useful for building timeseries 
`stack_id`: `RelativeOrbit_OrbitDirection_FrameNumber`
```python
import asf_search as asf

# Two adjacent stacks
stack_ids = ['165_D_100', '165_D_101']

multi_stack_results = asf.search(dataset=asf.DATASET.NISAR, granule_list=[f'NISAR_*{stack_id}*' for stack_id in stack_ids])
```

## OPERA-S1

OPERA S1 has a few useful fields not directly covered in places like Vertex but are possible in SearchAPI and asf-search.

Search for Level 2 OPERA products that use S1C as source acquisitions
`OPERA_L2_*S1C_*`

# TODO: grab more useful examples (what are DISP-NISAR file names going to look like?)
OPERA Project:
- https://www.jpl.nasa.gov/go/opera/products/

RTC:
- https://www.jpl.nasa.gov/go/opera/products/rtc-product/ 