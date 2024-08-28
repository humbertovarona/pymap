
# Mapping and Geospatial Data Analysis (pymap).

## Overview

This Dockerfile is designed to create a Docker image that provides a comprehensive environment for generating maps, particularly focusing on NetCDF data. The image includes all necessary dependencies and tools to process and visualize geospatial data, including support for various data formats like NetCDF, shapefiles, and others. The environment is also equipped with tools to generate, manipulate, and visualize data using Python libraries such as Cartopy, Matplotlib, and GDAL.


## Version

1.0

## Release date

2024-08-04

## DOI

[https://doi.org/10.5281/zenodo.13372558](https://doi.org/10.5281/zenodo.13372558)

## Cite as

Humberto L. Varona, Silena Herold-Garcia. (2024). Mapping and Geospatial Data Analysis (pymap). (1.0). Zenodo. https://doi.org/10.5281/zenodo.13372558


## Base Image

The Dockerfile begins by pulling the `python:3.12.5-slim-bookworm` image, a minimalistic Debian-based image that includes Python 3.12.5. This choice ensures that the environment is lightweight while still offering the necessary capabilities for Python-based geospatial data processing.


## System Dependencies

A series of essential system packages are installed to enable the processing and visualization of geospatial data. These packages include libraries for handling database connections, geospatial data formats, and graphical rendering.

### Installed Packages:

- **curl**: Command-line tool for transferring data with URLs.
- **unzip**: Utility to unpack `.zip` files.
- **libmariadb-dev**: Development files for MariaDB/MySQL database.
- **libpq-dev**: PostgreSQL C client library and headers.
- **libsqlite3-dev**: SQLite3 development files.
- **gdal-bin**: Command-line tools for Geospatial Data Abstraction Library (GDAL).
- **libgdal-dev**: GDAL development libraries.
- **libhdf5-dev**: HDF5 development libraries.
- **libnetcdf-dev**: NetCDF development libraries.
- **libxml2-dev**: XML processing libraries.
- **libxslt1-dev**: XSLT processing libraries.
- **libopenjp2-7**: JPEG 2000 image codec library.
- **libzbar0**: Barcode scanner library.
- **libfreetype6-dev**: FreeType 2 font engine development files.
- **libreoffice-calc**: LibreOffice Calc for spreadsheet processing.


## User and Directory Setup

A new user, `sciuser`, is created to run the container's processes. This user is assigned a home directory at `/home/sciuser`.


```plaintext
/home/sciuser/
│
├── WORKDIR/
│   ├── Python scripts
│   ├── NetCDF data files
│   ├── Other data files 
│   └── ...
├── data/
│   ├── 10m_physical/
│   │   ├── ne_10m_bathymetry_all/
│   │   └── ne_10m_graticules_all/
│   ├── 10m_cultural/
│   ├── 50m_physical/
│   │   └── ne_50m_graticules_all/
│   ├── 50m_cultural/
│   ├── 110m_physical/
│   │   └── ne_110m_graticules_all/
│   ├── 110m_cultural/
│   ├── housekeeping/
│   │   └── src/
│   └── tools/
│   │   └── ...
└── OUTPUT/
    ├── Generated maps will be saved here
    ├── Other generated files
    └── ...
```

## Python Virtual Environment

A Python virtual environment is created to isolate Python dependencies and avoid conflicts with system-wide packages. The environment is stored in `/home/sciuser/venv`, and ownership is assigned to `sciuser`.

Switching to the `sciuser` ensures that all following operations, including package installations, are performed with the correct permissions.

## Detailed Overview of Python Packages for Map Creation

This README provides a comprehensive description of each Python package included in the Docker image for map creation. Each package's applications, relationships with other packages, and other important information are discussed to give a clear understanding of their roles in geospatial data processing and visualization.

### Packages Overview

#### 1. Matplotlib

**Description**: Matplotlib is a widely used plotting library in Python for generating static, animated, and interactive visualizations. It provides a comprehensive set of tools for creating various types of plots, including line graphs, scatter plots, bar charts, and more. When combined with other geospatial libraries, Matplotlib can be used to create maps.

**Applications**:

- Creating 2D plots and visualizations in a variety of formats.
- Generating maps when used in conjunction with Basemap or Cartopy.

#### 2. Basemap

**Description**: Basemap is a toolkit for Matplotlib, developed to create static maps in Python. It offers tools for projecting geographical data, drawing coastlines, and plotting data on maps. Despite being deprecated in favor of Cartopy, Basemap is still in use for legacy projects and specific use cases that require its unique features.

**Applications**:

- Generating maps with different map projections.
- Adding geographical features such as coastlines, borders, and rivers.

#### 3. Seaborn

**Description**: Seaborn is a Python data visualization library based on Matplotlib, providing a high-level interface for creating attractive and informative statistical graphics. Seaborn simplifies the process of generating complex plots and is often used for visualizing statistical relationships between data points.

**Applications**:

- Enhancing data visualization by adding complex statistical plots.
- Creating visually appealing plots with less code compared to Matplotlib.

#### 4. GeoPandas

**Description**: GeoPandas extends the capabilities of Pandas to allow spatial operations on geometric types. It simplifies working with geospatial data in Python by providing the tools to read, write, and manipulate spatial data within a Pandas DataFrame structure. GeoPandas integrates with libraries like Shapely for geometric operations and Matplotlib for plotting.

**Applications**:

- Reading and writing geospatial data from various file formats (e.g., shapefiles, GeoJSON).
- Performing spatial operations, such as buffering, merging, and spatial joins.

#### 5. Shapely

**Description**: Shapely is a library for the creation, manipulation, and analysis of planar geometric objects. It is used extensively in geospatial applications to handle the geometry of objects such as points, lines, and polygons, which are essential in spatial analysis.

**Applications**:

- Creating and manipulating geometric shapes.
- Performing geometric operations such as intersection, union, and difference.

#### 6. Pyproj

**Description**: Pyproj is a Python interface to the PROJ library, which handles cartographic projections and transformations. It is essential for converting geographic coordinates between different projections, making it a critical tool for geospatial analysis.

**Applications**:

- Performing cartographic transformations.
- Converting coordinate systems to and from different projections.

#### 7. Folium

**Description**: Folium is a powerful Python library for generating interactive maps using the Leaflet.js library. It enables users to visualize data on maps that can be embedded in web applications. Folium is particularly useful for creating interactive web-based maps that can display data in various formats.

**Applications**:

- Generating interactive maps for web applications.
- Visualizing geospatial data in an interactive format.

#### 8. Plotly

**Description**: Plotly is an open-source library for creating interactive visualizations. It supports a wide range of plot types, including 3D plots, maps, and dashboards. Plotly is often used in web applications due to its interactivity and ability to generate high-quality visualizations.

**Applications**:

- Creating interactive and responsive visualizations.
- Building dashboards that incorporate maps and other visual data elements.

#### 9. Contextily

**Description**: Contextily is a library that allows users to add basemaps to their GeoPandas visualizations. It fetches tile maps from online sources, like OpenStreetMap, and integrates them into static visualizations created with Matplotlib or GeoPandas.

**Applications**:

- Adding basemaps to geospatial plots created with GeoPandas and Matplotlib.
- Enhancing spatial data visualizations by providing contextual geographic backgrounds.

#### 10. Cartopy

**Description**: Cartopy is a Python package for cartographic projections and geospatial data visualization. It is designed to be used with Matplotlib and provides tools to create maps with various projections, handle geospatial data, and visualize complex datasets on maps.

**Applications**:

- Creating maps with different projections.
- Visualizing geospatial data in a static format.

#### 11. Osmnx

**Description**: Osmnx is a Python package for downloading, modeling, analyzing, and visualizing street networks from OpenStreetMap. It is particularly useful in urban planning and transportation studies, enabling the creation of detailed street maps and network analyses.

**Applications**:

- Downloading and analyzing street networks from OpenStreetMap.
- Conducting urban studies and transportation analyses.


#### 12. Fiona

**Description**: Fiona is a library for reading and writing vector data formats, using the GDAL library's capabilities in a Pythonic way. It serves as the input/output engine behind GeoPandas and allows users to work with various geospatial file formats such as shapefiles, GeoJSON, and more.

**Applications**:

- Reading and writing geospatial data in vector formats.
- Handling file I/O operations in GeoPandas.

#### 13. Rasterio

**Description**: Rasterio is a library for reading and writing geospatial raster data. It leverages GDAL's capabilities and provides Pythonic interfaces to handle large raster datasets, which are common in remote sensing and environmental modeling.

**Applications**:

- Reading, writing, and processing raster data.
- Performing geospatial operations on raster datasets, such as reprojection and clipping.

#### 14. Mapclassify

**Description**: Mapclassify is a library used to classify geographical data into different categories or classes. It is commonly used with GeoPandas for creating thematic maps, such as choropleth maps, where data is visualized in different shades or colors based on classification.

**Applications**:

- Classifying geospatial data for thematic mapping.
- Supporting spatial analysis by categorizing data into classes.

#### 15. Descartes

**Description**: Descartes is a Python library that allows geometric shapes created with Shapely to be used as Matplotlib patches. This integration enables the visualization of geometric data on maps, providing a bridge between geometric operations and data visualization.

**Applications**:

- Visualizing geometric data on plots.
- Enhancing geospatial visualizations by incorporating complex shapes.

#### 16. MySQLclient

**Description**: MySQLclient is a Python interface for connecting to MySQL databases, allowing users to execute SQL queries and interact with MySQL databases from within Python applications. It is commonly used in applications that require database connectivity for data storage and retrieval.

**Applications**:

- Connecting to and querying MySQL databases.
- Integrating MySQL data with Python applications for analysis.

#### 17. Psycopg2-binary

**Description**: Psycopg2 is the most popular PostgreSQL adapter for Python, providing tools to interact with PostgreSQL databases. It supports advanced PostgreSQL features and is widely used for database-driven applications.

**Applications**:

- Executing SQL queries and managing PostgreSQL databases.
- Integrating PostgreSQL with Python applications for geospatial data storage and analysis.

#### 18. SQLAlchemy

**Description**: SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides tools for interacting with relational databases in a Pythonic way, abstracting database operations and enabling complex queries without direct SQL.

**Applications**:

- Database management and query abstraction.
- Integrating databases with Python applications using ORM.

#### 19. GeoAlchemy2

**Description**: GeoAlchemy2 is an extension of SQLAlchemy that provides support for spatial databases such as PostGIS. It allows users to perform spatial queries and manage geospatial data within a relational database using SQLAlchemy's ORM capabilities.

**Applications**:

- Managing and querying spatial data in PostgreSQL/PostGIS.
- Extending SQLAlchemy's ORM to support geospatial operations.

#### 20. SQLite

**Description**: SQLite is a self-contained, serverless, and lightweight database engine. It is often used in applications that require a simple, embedded database for data storage. SQLite's simplicity and portability make it a popular choice for small to medium-sized applications.

**Applications**:

- Embedding databases within Python applications.
- Storing and managing geospatial data in a lightweight format.

#### 21. NetCDF4

**Description**: NetCDF4 is a Python library for interacting with NetCDF files, which are widely used in scientific computing to store multi-dimensional data such as climate data, oceanography, and meteorology. NetCDF4 enables reading, writing, and processing these datasets in Python.

**Applications**:

- Handling large scientific datasets in NetCDF format.
- Processing and analyzing climate and environmental data.

#### 22. Pandas

**Description**: Pandas is a powerful data manipulation and analysis library in Python. It provides data structures like DataFrames for managing and analyzing structured data. Pandas is commonly used for data cleaning, preparation, and analysis in a wide range of applications.

**Applications**:

- Manipulating and analyzing structured data.
- Integrating with other libraries for comprehensive data analysis.

#### 23. Openpyxl

**Description**: Openpyxl is a Python library for reading and writing Excel files. It supports both reading and writing of Excel 2010 xlsx/xlsm/xltx/xltm files. Openpyxl is commonly used in data analysis workflows to handle spreadsheet data.

**Applications**:

- Reading and writing Excel files in Python.
- Manipulating Excel files for data analysis.

#### 24. Xlrd

**Description**: Xlrd is a Python library for reading data from older Excel file formats (.xls). It is used in data analysis workflows to extract information from Excel files, especially those created with older versions of Microsoft Excel.

**Applications**:

- Extracting data from Excel files (.xls format).
- Integrating Excel data with Python applications.

#### 25. Odfpy

**Description**: Odfpy is a Python library for reading and writing OpenDocument Format (ODF) files, such as those used by LibreOffice. It provides tools for working with ODF text documents, spreadsheets, and presentations in Python.

**Applications**:

- Handling OpenDocument files (e.g., .odt, .ods) in Python.
- Automating document processing for LibreOffice-compatible files.

## Geospatial Data

The Dockerfile includes commands to download and unzip geospatial data from the Natural Earth dataset. The data is stored in `/home/sciuser/data`, making it accessible for processing within the container.

```sh
curl -o /home/sciuser/data/natural_earth_vector.zip https://naciscdn.org/naturalearth/packages/natural_earth_vector.zip
unzip /home/sciuser/data/natural_earth_vector.zip -d /home/sciuser/data
rm /home/sciuser/data/natural_earth_vector.zip
```

## Volume Management

The `VOLUME` instruction in the Dockerfile designates `/home/sciuser/OUTPUT` as a mount point for external storage. This allows persistent storage of generated output files, even after the container is stopped.

```Dockerfile
VOLUME /home/sciuser/OUTPUT
```

## Environment Variables

Two environment variables are set:

- **DATA_PATH**: Points to the location of the geospatial data.
- **PATH**: Extends the system path to include the virtual environment and data directories.

```sh
export DATA_PATH=/home/sciuser/data
export PATH="/home/sciuser/venv/bin:$DATA_PATH:$PATH"
```

These variables ensure that the data and Python environment are easily accessible within the container.

## Command Execution

The `CMD` instruction sets up the default command for the container. It ensures that the virtual environment is activated and any provided command is executed in that context.

```Dockerfile
CMD ["/bin/bash", "-c", "source /home/sciuser/.bashrc && exec "$@"", "--"]
```

This setup allows the container to execute any Python script or command provided at runtime while ensuring that the necessary environment is active.

## Building the Docker Image

To build the Docker image using this Dockerfile, navigate to the directory containing the Dockerfile and run the following command:

```bash
docker build -t pymap .
```

This command will create a Docker image named `pymap` with all the dependencies and configurations specified in the Dockerfile.

## How to install

```bash
docker pull humbertovarona/pymap:v1-full
```

or 

```bash
docker pull humbertovarona/pymap:v1-lite
```

or 

```bash
docker pull humbertovarona/pymap:latest
```

The `humbertovarona/pymap:latest` version is the same as the `humbertovarona/pymap:v1-lite` version. The difference between the `humbertovarona/pymap:v1-lite` version and the `humbertovarona/pymap:v1-full` version is that the latter contains the [Natural Earth](https://naciscdn.org/naturalearth/packages/Natural_Earth_quick_start.zip) datasets stored in **/home/sciuser/data/**

### Output Management

A local `OUTPUT` directory must be manually created before instantiating the docker image to store the results generated by the python scripts. Permissions are set to allow read, write, and execute access.

```plaintext
mkdir OUTPUT
chmod -R 777 OUTPUT
```

### Add the "Natural Earth" datasets in the `humbertovarona/pymap:v1-lite` version

```bash
#!/bin/bash
mkdir -p ./data
curl -o ./data/natural_earth_vector.zip https://naciscdn.org/naturalearth/packages/natural_earth_vector.zip
unzip ./data/natural_earth_vector.zip -d ./data
rm ./data/natural_earth_vector.zip
exit 0
```

Save the above bash script as **download_external_data.sh** and run it locally (in the same directory that contains the `OUTPUT` directory), the [Natural Earth](https://naciscdn.org/naturalearth/packages/Natural_Earth_quick_start.zip) datasets will be downloaded and stored in **/home/sciuser/WORKDIR/data/**

```bash
./download_external_data.sh
```

**`VERY IMPORTANT:` NOTE THAT IN THE `humbertovarona/pymap:v1-lite` VERSION THE DATASETS ARE IN A DIFFERENT PATH THAN IN THE `humbertovarona/pymap:v1-full` VERSION**

## Running the Docker

To run the Docker container and execute a Python script within it, use the following command:

```sh
docker run -it --rm -v "$PWD":/home/sciuser/WORKDIR -v "$PWD/OUTPUT:/home/sciuser/OUTPUT" humbertovarona/pymap:v1-full python your_script.py
```

Or


```sh
docker run -it --rm -v "$PWD":/home/sciuser/WORKDIR -v "$PWD/OUTPUT:/home/sciuser/OUTPUT" humbertovarona/pymap:v1-lite python your_script.py
```

### Explanation:

- **-it**: Runs the container in interactive mode with a terminal.
- **--rm**: Automatically removes the container after execution.
- **-v "$PWD":/home/sciuser/WORKDIR**: Mounts the current directory to the container's working directory.
- **-v "$PWD/OUTPUT:/home/sciuser/OUTPUT"**: Mounts the output directory for persistent storage.
- **pymap**: The name of the Docker image built earlier.
- **python your_script.py**: The command to execute inside the container.

# Map Visualization Scripts in Python

This repository contains various Python scripts for creating geographical maps using different libraries such as `Basemap` and `Cartopy`. Each script serves a different purpose and showcases various features of map visualization.

## Scripts Overview

### example1.py

This Python script generates a map of Africa using the Basemap library, which is part of the mpl_toolkits package. The map is created with the Mercator projection, a cylindrical map projection commonly used for navigation because it preserves angles and directions. The script first sets the geographical boundaries of the map to include Africa, ranging from 35 degrees south to 40 degrees north in latitude, and from 20 degrees west to 60 degrees east in longitude. The resolution of the map is set to 'intermediate' ('i'), which balances detail and performance.

The script then draws the borders of the countries and the coastlines, using black and gray colors, respectively. Meridians (lines of longitude) and parallels (lines of latitude) are also drawn on the map, labeled appropriately at the edges. The continents are filled with a light green color, and the oceans and lakes are filled with a light blue color. A title is added to the map for context. Finally, the map is saved as a PNG file in a specified directory, and a message is printed to confirm the save location. The map is also displayed on the screen using plt.show().

This code is suitable for generating high-quality visualizations of geographical regions, particularly for educational or professional presentations. The use of Basemap allows for customizable and precise map rendering, making it a valuable tool for anyone working with geographical data.

**Code**:

```python
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

```

### example2.py

This Python script utilizes the Cartopy library to generate a detailed map of South America, with specific geographic and cultural features. The script begins by importing necessary modules, including Cartopy for geographical plotting and Matplotlib for rendering the final output. The map projection used here is PlateCarree, which is a simple cylindrical projection suitable for representing regions of the Earth without excessive distortion. The script sets the geographical extent to focus on South America, ranging from 82 degrees west to 34 degrees west in longitude, and from 56 degrees south to 13 degrees north in latitude.

The script then reads shapefiles containing physical and cultural data from specified directories on the local filesystem. These shapefiles include geometrical data for landmasses, oceans, coastlines, and country borders. Each dataset is converted into a Cartopy feature using the ShapelyFeature function, which allows for the customization of the visual appearance of these features on the map. The land areas are colored light green, the oceans light blue, and the borders and coastlines are outlined in black.

Finally, the script adds gridlines to the map for reference, labels them, and sets the map's title. The map is then saved to the specified output directory as a PNG file, and a confirmation message is printed. The map is also displayed using Matplotlib’s plt.show() function, allowing for immediate visualization. This script is particularly useful for creating customized geographical maps with high precision, using locally stored shapefiles.

**Code**:

```python
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

```

### example3.py

This Python script uses the GeoPandas library to create a geographical map of South America, augmented with bar charts representing data for three distinct groups: Group A, Group B, and Group C. The script starts by loading a shapefile containing country boundaries and filtering it to retain only the countries within the South American continent. It then introduces three new data columns (Group_A, Group_B, Group_C) representing some numerical data associated with each country.

The script then transforms the coordinate reference system (CRS) of the GeoDataFrame to EPSG:3857, which is a projected CRS suitable for mapping and ensures consistent visual representation. It calculates the centroid coordinates (x and y) for each country to serve as the locations where the bar charts will be plotted. The draw_bars function is defined to create the bar charts, scaling them according to the provided values and placing them at the calculated centroid positions.

Finally, the map's boundary and the bar charts are drawn using Matplotlib. The map is set with appropriate longitude and latitude limits, labels, and a title. The resulting map is saved as a PNG file in a specified output directory, and a message confirming the save location is printed. The map is displayed on the screen using plt.show(). This code is particularly useful for visualizing geographical data in combination with categorical data, offering a clear and informative representation of the information.

**Code**:

```python
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
```

### example4.py

This Python script generates a map of South America using GeoPandas, Matplotlib, and Contextily, incorporating key geographical features and annotating important cities. The script begins by loading a shapefile that contains the country boundaries of South America and filtering it to only include countries from this continent. Additionally, a dictionary of major South American cities with their respective coordinates is created, and these coordinates are converted into geometric points using the Shapely library. These points are then stored in a GeoDataFrame.

The coordinate reference systems (CRS) of both the country boundaries and the city points are converted to EPSG:3857, which is a commonly used web mapping projection, ensuring consistent spatial representation. The map is plotted with the country boundaries displayed in a light green color and the city points highlighted in red. Labels for the cities are placed next to the corresponding points on the map, and each country is annotated with its name at a representative point within its borders.

Contextily is then used to add a basemap from OpenStreetMap, which provides additional geographical context to the map. The basemap enhances the visualization by displaying underlying map tiles that include features like roads and terrain. The map is given appropriate limits for longitude and latitude, and a title is added to the plot. Finally, the map is saved as a PNG file to a specified output directory, and a confirmation message is printed to indicate that the map has been saved. This script is ideal for visualizing geographical data with added context and is particularly useful for creating maps that highlight specific points of interest.

**Code**:

```python
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
```

### example5.py

This Python script is designed to generate a geographical map of Africa using the GeoPandas library, and then save the map as a PNG file. The script begins by defining the path to the shapefile, which contains the boundaries of all countries in the world. This path is constructed using an environment variable (DATA_PATH) to allow for flexibility in data storage location. If the environment variable is not set, it defaults to a predefined directory. The shapefile is read into a GeoDataFrame, and the data is filtered to retain only the countries located on the African continent.

The filtered GeoDataFrame, containing only African countries, is then plotted using Matplotlib. The map is displayed with a light green color for the landmasses and black edges outlining the country borders. The figure is created with a square aspect ratio to ensure that the continent is represented proportionally, and a title is added to the map for context.

Finally, the script sets up the output directory where the map will be saved. This directory is also determined by an environment variable (OUTPUT), with a default path provided if the variable is not set. The script ensures that the output directory exists, creating it if necessary. The map is then saved as a PNG file in the specified directory, and a confirmation message is printed to indicate the save location. This script is well-suited for quickly generating and saving maps of specific continents or regions, offering flexibility in file paths through environment variables.

**Code**:

```python
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
```

### example6.py

This Python script utilizes the Folium library to create an interactive map centered on South America, specifically on Brasília, Brazil. The map is initialized with a zoom level of 4, which provides a broad view of the region. The map's center is set to the coordinates of Brasília, the capital of Brazil. The Folium library is well-suited for creating interactive maps that can be easily embedded in web pages or viewed in browsers.

A marker is added to the map at the location of Brasília, with a popup label that appears when the marker is clicked. This is achieved using the folium.Marker class, which allows for the placement of a pin on the map. Additionally, a circular marker is added at the coordinates of Rio de Janeiro. This marker is styled as a circle with a crimson color and a radius of 50 units, which visually highlights the city. The CircleMarker is filled with the same crimson color, and it includes a popup label that identifies the location as Rio de Janeiro.

Finally, the map is saved as an HTML file in the specified output directory. The path to the output file is /home/sciuser/OUTPUT/south_america_map_folium.html. A confirmation message is printed to the console, indicating the save location. This script is particularly useful for creating interactive, web-based maps with specific points of interest marked, making it a powerful tool for geographical data visualization and presentation.

**Code**:

```python
import folium

mapa = folium.Map(location=[-15.793889, -47.882778], zoom_start=4)

folium.Marker([-15.793889, -47.882778], popup="Brasilia, Brazil").add_to(mapa)

folium.CircleMarker(
    location=[-22.9068, -43.1729],
    radius=50,
    popup="Rio de Janeiro",
    color="crimson",
    fill=True,
    fill_color="crimson"
).add_to(mapa)

mapa.save("/home/sciuser/OUTPUT/south_america_map_folium.html")

print("Folium map saved to /home/sciuser/OUTPUT/south_america_map_folium.html")
```

### example7.py

This Python script generates a map of South America using the GeoPandas library, with overlaid pie charts that represent data for three distinct groups: Group A, Group B, and Group C. The script begins by reading a shapefile containing country boundaries and filtering it to include only the countries in South America. It then assigns numerical data to three new columns, representing the groups for each country.

The script transforms the coordinate reference system (CRS) of the GeoDataFrame to EPSG:3857, which is a projection commonly used in web mapping. For each country, the centroid coordinates (x and y) are calculated, which serve as the locations where the pie charts will be plotted. The draw_pie function is defined to create and position pie charts at these centroids, scaling the pie sizes by a factor of three for better visibility on the map.

Finally, the map's boundary is drawn with black edges, and the pie charts are plotted accordingly. The script sets the map's limits to focus on South America and labels the longitude and latitude axes. A title is added to the map, and a legend is created using Patch elements to represent the three groups. The map is saved as a PNG file in a specified output directory, and a confirmation message is printed to indicate where the map has been saved. This script is useful for visualizing categorical data geographically, with pie charts providing a clear comparison of group distributions across countries.

**Code**:

```python
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
```

### example8.py

This Python script generates a map of South America using GeoPandas and Seaborn, overlaid with a kernel density estimate (KDE) plot to represent a simulated population distribution. The script starts by loading a shapefile that contains the boundaries of all countries and filters the data to include only countries within South America. A fictitious population dataset is assigned to each country to illustrate the KDE visualization.

The script then transforms the coordinate reference system (CRS) of the GeoDataFrame to EPSG:3857, which is suitable for accurate map rendering. Using Matplotlib and Seaborn, a KDE plot is generated, showing the density of the population based on the centroid coordinates of each country. The density plot is colored using the "Blues" color map, providing a gradient effect that highlights areas of higher population density. The contour levels of the KDE plot are set to 10, and the thresh parameter is used to adjust the level below which density estimates are not plotted.

Finally, the country boundaries are overlaid on the KDE plot to provide geographical context, with black lines outlining each country. The map is titled appropriately, indicating that the population data is simulated. The completed map is saved as a PNG file in the specified output directory, and a confirmation message is printed to indicate the save location. This script is particularly useful for visualizing spatial distributions of data, such as population densities, in a geographical context, making it a powerful tool for data analysis and presentation.

**Code**:

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import os

cultural_data_dir = '/home/sciuser/data/110m_cultural/'

shapefile_path = os.path.join(cultural_data_dir, 'ne_110m_admin_0_countries.shp')
world = gpd.read_file(shapefile_path)

south_america = world[world['CONTINENT'] == 'South America'].copy()

south_america.loc[:, 'Population'] = [40, 10, 30, 50, 20, 60, 70, 90, 80, 100, 55, 65, 75]

south_america = south_america.to_crs(epsg=3857)

plt.figure(figsize=(10, 10))
ax = plt.gca()

sns.set(style="whitegrid")
sns.kdeplot(
    data=south_america,
    x=south_america.geometry.centroid.x,
    y=south_america.geometry.centroid.y,
    fill=True,
    cmap="Blues",
    levels=10,
    ax=ax,
    thresh=0.05,
)

south_america.boundary.plot(ax=ax, linewidth=1, edgecolor='black')

plt.title("Map of South America with Simulated Population using Seaborn")

output_dir = '/home/sciuser/OUTPUT'
output_file = f"{output_dir}/south_america_map_seaborn.png"
plt.savefig(output_file, bbox_inches='tight')

print(f"Map saved to {output_file}")

plt.show()
```

### example9.py

This Python script generates a geographical map of South America using GeoPandas and Seaborn, overlaid with a scatter plot representing a simulated population distribution. The script starts by loading a shapefile that contains country boundaries and filtering the data to include only South American countries. A fictitious population dataset is assigned to each country, allowing the visualization of population distribution through scatter points on the map.

The coordinate reference system (CRS) of the GeoDataFrame is transformed to EPSG:3857, ensuring accurate map rendering. The script calculates the centroids (geometric centers) of each country's polygon, which serve as the locations for the scatter points. These centroids' x and y coordinates are extracted for use in plotting.

Using Matplotlib and Seaborn, a scatter plot is created where each point represents a country. The size and color of each point are proportional to the population data, with a gradient color scheme (coolwarm palette) used to differentiate between lower and higher populations. The scatter points are plotted on top of the country boundaries, which are outlined in black for clarity.

Finally, the map is given an appropriate title, saved as a PNG file in a specified output directory, and a confirmation message is printed to indicate the save location. This script is useful for visualizing data distributions geographically, providing a clear and aesthetically pleasing representation of the simulated population data across South America.

**Code**:

```python
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
```

### example10.py

This Python script generates a map of sea surface temperature (SST) for the month of July, averaged over the period from 1991 to 2020, using data from a NetCDF file. The script begins by loading the NetCDF dataset, which contains variables such as SST, latitude, and longitude. It then selects the SST data for the fifth month (July) and masks any missing values, ensuring they are not plotted.

The script creates a map using Cartopy, with a Plate Carrée projection, which is commonly used for global maps. The map's extent is set to the full range of the latitude and longitude data. The script adds geographical features such as land and country borders using shapefiles, which are read and plotted with the appropriate styling.

The SST data is visualized using the pcolormesh function, which creates a colored grid on the map. The colors represent different temperature values, with a color scale ranging from 0°C to 30°C. A color bar is added to the map to provide context for the temperature values. Additionally, a contour line is drawn at the 28°C level, with labels indicating the temperature, providing a clear reference for areas with particularly warm sea surface temperatures. The final map is saved as a PNG file, and a confirmation message is printed to indicate the save location. The NetCDF dataset is closed at the end of the script to free up resources.

**Code**:

```python
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
```

### example11.py

This Python script creates a detailed visualization of Sea Surface Temperature (SST) data for July, using data from a NetCDF file and overlaying it on a map with an inset zoom on the Brazilian coast. The script starts by loading the SST data for July from a NetCDF dataset, masking any missing values to avoid displaying them on the map. It uses the Cartopy library to generate a map with a Plate Carrée projection, which is well-suited for global data visualization.

The main map displays the SST data using a pcolormesh, which renders the data as a colored grid, with the coolwarm colormap ranging from 0°C to 35°C. Geographical features such as landmasses and country borders are added to provide context. A color bar is included to indicate the temperature scale, and a contour line is drawn at 28°C to highlight regions with this specific temperature.

In addition to the main map, the script creates an inset map that zooms in on the coastal region of Brazil, showing the SST in more detail with a different colormap (nipy_spectral) to highlight temperature variations between 25°C and 30°C. This inset includes gridlines with labeled coordinates and is positioned within the main map for easy reference. The entire map is saved as a PNG file, and a confirmation message is printed. The NetCDF dataset is closed at the end of the script to free up resources. This script is ideal for visualizing large-scale environmental data with both broad and detailed perspectives.

**Code**:

```python
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

sst = ds.variables['sst'][9, :, :]
lat = ds.variables['lat'][:]
lon = ds.variables['lon'][:]

sst = np.ma.masked_where(sst == ds.variables['sst'].missing_value, sst)

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})

ax.set_extent([lon.min(), lon.max(), lat.min(), lat.max()], crs=ccrs.PlateCarree())

land_geom = shpreader.Reader(os.path.join(physical_data_dir, 'ne_10m_land.shp')).geometries()
borders_geom = shpreader.Reader(os.path.join(cultural_data_dir, 'ne_50m_admin_0_countries.shp')).geometries()

land_feature = cfeature.ShapelyFeature(land_geom, ccrs.PlateCarree(), edgecolor='black', facecolor='lightgreen')
borders_feature = cfeature.ShapelyFeature(borders_geom, ccrs.PlateCarree(), edgecolor='black')

ax.add_feature(land_feature)
ax.add_feature(borders_feature)

c = ax.pcolormesh(lon, lat, sst, cmap='coolwarm', transform=ccrs.PlateCarree(), vmin=0, vmax=35)

cbar = plt.colorbar(c, ax=ax, orientation='vertical', fraction=0.02, pad=0.04)
cbar.set_label('Sea Surface Temperature (°C)')

contour = ax.contour(lon, lat, sst, levels=[28], colors='black', linewidths=1.25, linestyles='--', transform=ccrs.PlateCarree())
ax.clabel(contour, inline=True, fontsize=10, fmt="28°C", colors='black')

axins = ax.inset_axes([0.5, 0.1, 0.60, 0.70], projection=ccrs.PlateCarree())

axins.set_extent([-46, -33, -10, 8], crs=ccrs.PlateCarree())

axins.add_feature(land_feature)
axins.add_feature(borders_feature)

c_zoom = axins.pcolormesh(lon, lat, sst, cmap='nipy_spectral', transform=ccrs.PlateCarree(), vmin=25, vmax=30)

contour_zoom = axins.contour(lon, lat, sst, levels=[28], colors='black', linewidths=1.25, linestyles='--', transform=ccrs.PlateCarree())
axins.clabel(contour_zoom, inline=True, fontsize=8, fmt="28°C", colors='black')

gridlines = axins.gridlines(draw_labels=True, linestyle='--', linewidth=1, color='gray', alpha=0.7)
gridlines.top_labels = False
gridlines.right_labels = False

cbar_zoom = plt.colorbar(c_zoom, ax=ax, orientation='vertical', fraction=0.02, pad=0.05)

plt.title('Sea Surface Temperature (SST) - July (1991-2020 Mean) with 2x Brazil Coastal Zoom', fontsize=16)

output_file = '/home/sciuser/OUTPUT/sst_map_july_with_brazil_zoom_2x.png'
plt.savefig(output_file, bbox_inches='tight')
print(f"SST map with 2x zoom on the Brazilian coast saved to {output_file}")

plt.show()

ds.close()
```

## License

This project is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.

### IMPORTANT NOTE

This Docker was developed by specialists at the Centro de **Estudos e Ensaios em Risco e Modelagem Ambiental (CEERMA)** as part of the project identified under **Process No.: APQ-0235-1.08/23**, funded by **FACEPE/APAC**. This Docker was designed to support the **Núcleo de Oceanografia Operacional do Estado de Pernambuco (NOPE) project**.

It is available for free use by any individual or institution in scientific research, such as scientific articles, technical reports, books, and other scientific documents. It is important to note that proper citation of this Docker is required in the references of any scientific research in which it is used. Additionally, acknowledgments in such scientific articles, technical reports, books, and other scientific documents must explicitly include an acknowledgment to **CEERMA** as an institution.

For any commercial use of this Docker, it is necessary to contact the coordinator and/or vice-coordinator of the **NOPE** project and **CEERMA** beforehand to establish the corresponding terms and conditions of use.

---
