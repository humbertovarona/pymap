import geopandas as gpd
import matplotlib.pyplot as plt
import os
import numpy as np

cultural_data_dir = '/home/sciuser/data/110m_cultural/'

shapefile_path = os.path.join(cultural_data_dir, 'ne_110m_admin_0_countries.shp')
world = gpd.read_file(shapefile_path)

south_america = world[world['CONTINENT'] == 'South America'].copy()

south_america['Group_A'] = [20, 15, 25, 35, 40, 30, 50, 45, 60, 70, 55, 65, 75]
south_america['Group_B'] = [20, 15, 5, 15, 10, 30, 20, 35, 30, 30, 25, 15, 25]
south_america['Group_C'] = [10, 25, 15, 20, 30, 25, 40, 35, 50, 40, 35, 45, 55]

south_america = south_america.to_crs(epsg=3857)

south_america['centroid_x'] = south_america.geometry.centroid.x
south_america['centroid_y'] = south_america.geometry.centroid.y

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')

south_america.boundary.plot(ax=ax, linewidth=1, edgecolor='black')

def draw_bars(ax, values, x, y, width=450000, height_scale=5000):
    bars = np.array(values)
    n_bars = len(bars)
    bar_width = width / n_bars
    for i, bar in enumerate(bars):
        ax.bar(x + (i - n_bars / 2) * bar_width + bar_width / 2, bar * height_scale, width=bar_width, bottom=y, align='center', color=['blue', 'orange', 'green'][i])

for idx, row in south_america.iterrows():
    values = [row['Group_A'], row['Group_B'], row['Group_C']]
    draw_bars(ax, values, row['centroid_x'], row['centroid_y'])

ax.set_xlim(south_america.total_bounds[[0, 2]])
ax.set_ylim(south_america.total_bounds[[1, 3]])

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

plt.title("Map of South America with Bar Charts - Groups A, B, and C", fontsize=16)

ax.legend(['Group A', 'Group B', 'Group C'], loc='lower left')

output_dir = '/home/sciuser/OUTPUT'
output_file = f"{output_dir}/south_america_barcharts.png"
plt.savefig(output_file, bbox_inches='tight')

print(f"Map saved to {output_file}")

plt.show()