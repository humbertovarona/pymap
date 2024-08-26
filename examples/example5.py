import geopandas as gpd
import matplotlib.pyplot as plt
import os

data_path = os.getenv('DATA_PATH', '/home/sciuser/data/')
shapefile_path = os.path.join(data_path, '50m_cultural', 'ne_50m_admin_0_countries.shp')

world = gpd.read_file(shapefile_path)

africa = world[world['CONTINENT'] == 'Africa']

fig, ax = plt.subplots(figsize=(10, 10))
africa.plot(ax=ax, color='lightgreen', edgecolor='black')

plt.title('Map of Africa')

output_dir = os.getenv('OUTPUT', '/home/sciuser/OUTPUT')
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'africa_map.png')
plt.savefig(output_file)

print(f"Map saved to {output_file}")