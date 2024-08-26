import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import os
import numpy as np

physical_data_dir = '/home/sciuser/WORKDIR/data/10m_physical/'
cultural_data_dir = '/home/sciuser/WORKDIR/data/50m_cultural/'

nc_file = '/home/sciuser/WORKDIR/sst.oisst.mon.ltm.1991-2020.nc'

ds = nc.Dataset(nc_file)

sst = ds.variables['sst'][4, :, :]
lat = ds.variables['lat'][:]
lon = ds.variables['lon'][:]

sst = np.ma.masked_where(sst == ds.variables['sst'].missing_value, sst)

fig = plt.figure(figsize=(12, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.set_extent([lon.min(), lon.max(), lat.min(), lat.max()], crs=ccrs.PlateCarree())

land_geom = shpreader.Reader(os.path.join(physical_data_dir, 'ne_10m_land.shp')).geometries()
borders_geom = shpreader.Reader(os.path.join(cultural_data_dir, 'ne_50m_admin_0_countries.shp')).geometries()

land_feature = cfeature.ShapelyFeature(land_geom, ccrs.PlateCarree(), edgecolor='black', facecolor='lightgreen')
borders_feature = cfeature.ShapelyFeature(borders_geom, ccrs.PlateCarree(), edgecolor='black')

ax.add_feature(land_feature)
ax.add_feature(borders_feature)

c = ax.pcolormesh(lon, lat, sst, cmap='coolwarm', transform=ccrs.PlateCarree(), vmin=0, vmax=30)

cbar = plt.colorbar(c, ax=ax, orientation='vertical', fraction=0.02, pad=0.02)
cbar.set_label('Sea Surface Temperature (°C)')

contour = ax.contour(lon, lat, sst, levels=[28], colors='black', linewidths=1.25, linestyles='--', transform=ccrs.PlateCarree())
ax.clabel(contour, inline=True, fontsize=10, fmt="28°C", colors='black')

plt.title('Sea Surface Temperature (SST) - July (1991-2020 Mean)', fontsize=16)

output_file = '/home/sciuser/OUTPUT/sst_map_july_with_pcolormesh.png'
plt.savefig(output_file, bbox_inches='tight')
print(f"SST map with pcolormesh saved to {output_file}")

plt.show()

ds.close()