import numpy as np
from osgeo import gdal

def get_latlong(geotiff_img_path: str) -> tuple:
    """Returns limits of geotiff (in CRS) as a four-object tuple
     
        Parameters
        ----------
        geotiff_img_path : str, required
            Complete path to GeoTIFF
            
        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
    """
        
    if not isinstance(geotiff_img_path, str):
        raise TypeError("Input must be of type: str")
    
    ds = gdal.Open(geotiff_img_path)
    width = ds.RasterXSize
    height = ds.RasterYSize
    gt = ds.GetGeoTransform()
    minx = gt[0]
    miny = gt[3] + width*gt[4] + height*gt[5] 
    maxx = gt[0] + width*gt[1] + height*gt[2]
    maxy = gt[3]
    
    return (minx, miny, maxx, maxy)


def tif_to_array(tif_path: str) -> np.array:
    ds = gdal.Open(tif_path)
    return np.array(ds.GetRasterBand(1).ReadAsArray())