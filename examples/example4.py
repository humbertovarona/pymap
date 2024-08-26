import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
from shapely.geometry import Point

gdf = gpd.read_file('/home/sciuser/data/10m_cultural/ne_10m_admin_0_countries.shp')

gdf = gdf[gdf['CONTINENT'] == 'South America']

cities = {
    "Buenos Aires": (-58.3816, -34.6037),
    "São Paulo": (-46.6333, -23.5505),
    "Lima": (-77.0428, -12.0464),
    "Bogotá": (-74.0721, 4.7110),
    "Santiago": (-70.6483, -33.4569),
    "Caracas": (-66.9036, 10.4806)
}

city_geom = [Point(coord) for coord in cities.values()]
city_gdf = gpd.GeoDataFrame(cities.keys(), geometry=city_geom, crs="EPSG:4326")

gdf = gdf.to_crs(epsg=3857)
city_gdf = city_gdf.to_crs(epsg=3857)

fig, ax = plt.subplots(figsize=(12, 12))

gdf.plot(ax=ax, alpha=0.5, edgecolor='k', facecolor='lightgreen')

city_gdf.plot(ax=ax, color='red', markersize=50, label="Major Cities")

for x, y, label in zip(city_gdf.geometry.x, city_gdf.geometry.y, cities.keys()):
    ax.text(x, y, label, fontsize=12, ha='right')

gdf['coords'] = gdf['geometry'].apply(lambda x: x.representative_point().coords[:])
gdf['coords'] = [coords[0] for coords in gdf['coords']]
for idx, row in gdf.iterrows():
    ax.annotate(text=row['NAME'], xy=row['coords'], horizontalalignment='center', fontsize=10, color='darkblue')

ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, zoom=4)

ax.set_xlim(gdf.total_bounds[[0, 2]])
ax.set_ylim(gdf.total_bounds[[1, 3]])

plt.title("Map of South America with Major Cities", fontsize=16)

plt.legend()

output_file = "/home/sciuser/OUTPUT/south_america_map_contextily_with_info.png"
plt.savefig(output_file, bbox_inches='tight')
print(f"Contextily map with additional information saved to {output_file}")