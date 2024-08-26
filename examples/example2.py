import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import os

physical_data_dir = '/home/sciuser/data/50m_physical/'
cultural_data_dir = '/home/sciuser/data/110m_cultural/'

fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.set_extent([-82, -34, -56, 13], crs=ccrs.PlateCarree())

land_geom = shpreader.Reader(os.path.join(physical_data_dir, 'ne_50m_land.shp')).geometries()
ocean_geom = shpreader.Reader(os.path.join(physical_data_dir, 'ne_50m_ocean.shp')).geometries()
coastline_geom = shpreader.Reader(os.path.join(physical_data_dir, 'ne_50m_coastline.shp')).geometries()
borders_geom = shpreader.Reader(os.path.join(cultural_data_dir, 'ne_110m_admin_0_countries.shp')).geometries()

land_feature = cfeature.ShapelyFeature(land_geom, ccrs.PlateCarree(), edgecolor='black', facecolor='lightgreen')
ocean_feature = cfeature.ShapelyFeature(ocean_geom, ccrs.PlateCarree(), edgecolor='none', facecolor='lightblue')
borders_feature = cfeature.ShapelyFeature(borders_geom, ccrs.PlateCarree(), edgecolor='black')
coastline_feature = cfeature.ShapelyFeature(coastline_geom, ccrs.PlateCarree(), edgecolor='black')

ax.add_feature(land_feature)
ax.add_feature(ocean_feature)
ax.add_feature(coastline_feature)
ax.add_feature(borders_feature)

ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')

plt.title("Map of South America using Cartopy with Local Data")

output_dir = '/home/sciuser/OUTPUT'
output_file = f"{output_dir}/south_america_map_cartopy.png"
plt.savefig(output_file, bbox_inches='tight')

print(f"Map saved to {output_file}")

plt.show()