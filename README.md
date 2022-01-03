# polyclean
Clean up geospatial vector data.

This package provides utilities for cleaning up messy polygon data in 
geospatial data sets (e.g. filling holes within polygons or eliminating 
gaps between them.)

## Examples
### Fill Holes
Holes in polygons can be filled in based on area.

![holes_examplepng](https://user-images.githubusercontent.com/8603349/147906975-a8fee143-5809-4997-b622-eff2fc622f90.png)

### Fill Gaps
Gaps between polygons can also be filled in. Any gaps that are found are given a value of -1, so they can be easily distinguished from the original polygons. These gaps can be automatically removed by folding them into the polygon with which they share the longest edge. This mimics the functionality of the the ArcGIS Eliminate tool.

<img width="637" alt="combined" src="https://user-images.githubusercontent.com/8603349/147909181-af731d27-fba2-49aa-bfc6-30e4f311d724.png">

