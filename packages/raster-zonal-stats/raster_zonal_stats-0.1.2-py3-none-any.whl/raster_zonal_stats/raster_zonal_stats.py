import os
import geopandas as gpd
from rasterstats import zonal_stats

class RasterZonalStats:
    def __new__(cls, shp_path, tiff_path, aggr=None):
        try:
            if ".shp" != os.path.splitext(shp_path)[1]:
                raise ValueError('Incorrect shape file path.')
            
            if os.path.splitext(tiff_path)[1] not in [".tiff", ".tif"]:
                raise ValueError('Incorrect tiff file path.')
            
            if aggr and aggr not in ['mean', 'min', 'max', 'sum', 'median']:
                raise ValueError("Invalid aggregation.")
            
            # Load the Kenya shapefile
            raster_data = gpd.read_file(shp_path)

            if not aggr:
                aggr = 'mean'

            # Perform zonal statistics
            stats = zonal_stats(shp_path, tiff_path, stats=aggr, nodata=-999, all_touched=True)

            # Extract raster values
            raster_values = [stat[aggr] if stat else None for stat in stats]

            # Add temperature values to the Kenya shapefile
            raster_data['_value'] = raster_values

            return raster_data

        except Exception as error:
            raise error

