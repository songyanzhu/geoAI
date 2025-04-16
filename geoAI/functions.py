import numpy as np
import geopandas as gpd
from matplotlib import pyplot as plt
from shapely.ops import nearest_points
from shapely.geometry import LineString, Point


def show_city_boundary(shp, country, buffer = 0.1, fc = '#ff7f0e'):
    shp.plot()
    ax = plt.gca()
    country.plot(ax = ax, fc = '#1f77b4', alpha = 0.2)
    ax.set_xlim(shp.bounds.minx.item() - buffer, shp.bounds.maxx.item() + buffer)
    ax.set_ylim(shp.bounds.miny.item() - buffer, shp.bounds.maxy.item() + buffer)
    return ax
    

def midpoint_and_perpendicular(line):
    # 1. Get midpoint
    midpoint = line.interpolate(0.5, normalized=True)

    # 2. Get direction vector (dx, dy)
    x0, y0 = line.coords[0]
    x1, y1 = line.coords[-1]
    dx, dy = x1 - x0, y1 - y0

    # 3. Get perpendicular vector (-dy, dx) and normalize
    perp_dx, perp_dy = -dy, dx
    length = np.hypot(perp_dx, perp_dy)
    unit_dx, unit_dy = perp_dx / length, perp_dy / length

    # 4. Define length of perpendicular line (adjust as needed)
    perp_length = line.length / 2  # units (meters, degrees, etc. depending on CRS)

    # 5. Create endpoints of perpendicular line centered at midpoint
    x_mid, y_mid = midpoint.x, midpoint.y
    point1 = Point(x_mid + unit_dx * perp_length / 2, y_mid + unit_dy * perp_length / 2)
    point2 = Point(x_mid - unit_dx * perp_length / 2, y_mid - unit_dy * perp_length / 2)

    perp_line = LineString([point1, point2])

    # 6. Wrap in GeoDataFrames for plotting
    line_gdf = gpd.GeoDataFrame(geometry=[line])
    perp_gdf = gpd.GeoDataFrame(geometry=[perp_line])
    midpoint_gdf = gpd.GeoDataFrame(geometry=[midpoint])

    # # 7. Plot
    # ax = line_gdf.plot(color='blue', linewidth=2)
    # perp_gdf.plot(ax=ax, color='red', linewidth=2, linestyle='--')
    # midpoint_gdf.plot(ax=ax, color='black', markersize=50)

    return midpoint_gdf, perp_gdf 
