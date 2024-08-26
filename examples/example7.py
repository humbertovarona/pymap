import geopandas as gpd
import matplotlib.pyplot as plt
import os
from matplotlib.patches import Patch

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

def draw_pie(ax, sizes, x, y, size_scale=30000):
    pie_size = size_scale * 3
    wedges, _ = ax.pie(sizes, radius=pie_size, startangle=90)
    for wedge in wedges:
        wedge.set_center([x, y])
    ax.add_patch(plt.Circle((x, y), pie_size, color='white', fill=False, lw=0.5))

for idx, row in south_america.iterrows():
    sizes = [row['Group_A'], row['Group_B'], row['Group_C']]
    draw_pie(ax, sizes, row['centroid_x'], row['centroid_y'], size_scale=30000)

ax.set_xlim(south_america.total_bounds[[0, 2]])
ax.set_ylim(south_america.total_bounds[[1, 3]])

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

plt.title("Map of South America with Pie Charts - Groups A, B, and C", fontsize=16)

legend_elements = [Patch(facecolor='blue', edgecolor='blue', label='Group A'),
                   Patch(facecolor='orange', edgecolor='orange', label='Group B'),
                   Patch(facecolor='green', edgecolor='green', label='Group C')]
ax.legend(handles=legend_elements, loc='lower left')

output_dir = '/home/sciuser/OUTPUT'
output_file = f"{output_dir}/south_america_piecharts.png"
plt.savefig(output_file, bbox_inches='tight')

print(f"Map saved to {output_file}")

plt.show()