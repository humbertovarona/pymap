import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import os

cultural_data_dir = '/home/sciuser/data/110m_cultural/'

shapefile_path = os.path.join(cultural_data_dir, 'ne_110m_admin_0_countries.shp')
world = gpd.read_file(shapefile_path)

south_america = world[world['CONTINENT'] == 'South America'].copy()

south_america['Population'] = [40, 10, 30, 50, 20, 60, 70, 90, 80, 100, 55, 65, 75]

south_america = south_america.to_crs(epsg=3857)

south_america['centroid_x'] = south_america.geometry.centroid.x
south_america['centroid_y'] = south_america.geometry.centroid.y

plt.figure(figsize=(10, 10))
ax = plt.gca()

south_america.boundary.plot(ax=ax, linewidth=1, edgecolor='black')

sns.scatterplot(
    data=south_america,
    x='centroid_x',
    y='centroid_y',
    size='Population',
    hue='Population',
    palette='coolwarm',
    sizes=(20, 200),
    legend=False,
    ax=ax
)

plt.title("Distribution of Simulated Population in South America using Seaborn")

output_dir = '/home/sciuser/OUTPUT'
output_file = f"{output_dir}/south_america_population_scatter.png"
plt.savefig(output_file, bbox_inches='tight')

print(f"Map saved to {output_file}")

plt.show()