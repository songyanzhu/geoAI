'''
GeoPackage download link: https://www.data.gov.uk/dataset/4c1fe120-a920-4f6d-bc41-8fd4586bd662/os-open-greenspace1
'''

# !pip install fiona
# !pip install geopandas

import fiona
import geopandas as gpd

fiona.listlayers("opgrsp_gb.gpkg")
parks = gpd.read_file('opgrsp_gb.gpkg', layer = 'greenspace_site')

# only take greenspace with area > 10 ha
parks = parks[parks.area > 1e5]

parks.to_crs(epsg=4326).to_file('UK_greenspace_10ha.geojson', driver="GeoJSON")