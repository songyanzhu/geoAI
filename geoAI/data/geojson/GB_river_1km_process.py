import geopandas as gpd

shp = gpd.read_file('Statutory_Main_River_MapLine.shp')
shp = shp[shp['status'] == 'Main River']

shp = shp[shp['length_km'] > 1].to_crs('EPSG:4326')

# shp = gpd.overlay(shp, city, how="intersection")#.plot(color='lightblue', edgecolor='black')

# fig, ax = setup_canvas(1, 1, labelsize=10, fontsize=10)
# shp.plot(ax = ax, color='lightblue', edgecolor='black')
# city.plot(ax = ax, color='salmon', edgecolor='black')

shp.to_file("GB_river_1km.geojson", driver="GeoJSON")