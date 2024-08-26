from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))

m = Basemap(
    projection='merc',
    llcrnrlat=-35, urcrnrlat=40,
    llcrnrlon=-20, urcrnrlon=60,
    lat_ts=0,
    resolution='i'
)

m.drawcountries(linewidth=1.0, color='black')

m.drawcoastlines(linewidth=0.8)

m.drawmapboundary(fill_color='lightblue')

m.drawmeridians(range(-180, 180, 20), labels=[0, 0, 0, 1], color='gray')
m.drawparallels(range(-90, 90, 10), labels=[1, 0, 0, 0], color='gray')

m.fillcontinents(color='lightgreen', lake_color='lightblue')

plt.title("Map of Africa using Basemap (Mercator Projection)")

output_dir = '/home/sciuser/OUTPUT'
output_file = f"{output_dir}/africa_map_basemap.png"
plt.savefig(output_file, bbox_inches='tight')

print(f"Map saved to {output_file}")

plt.show()
