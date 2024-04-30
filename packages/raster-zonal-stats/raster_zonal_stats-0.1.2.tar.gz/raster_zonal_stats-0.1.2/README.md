# Raster Zonal Stats

'Raster Zonal Stats' is a Python library designed to retrieve raster values for each pixel of a shapefile.

## Installation

Install using below pip command

```bash
pip install raster-zonal-stats

```

# Usage

from raster_zonal_stats import RasterZonalStats

RasterZonalStats('/path/to/shapefile.shp', '/path/to/raster.tif', aggr='mean')

# Parameters

shp_path (str): Path to the shapefile.

tiff_path (str): Path to the TIFF file.

aggr (str, optional): Aggregation method for zonal statistics. Defaults to 'mean'.

