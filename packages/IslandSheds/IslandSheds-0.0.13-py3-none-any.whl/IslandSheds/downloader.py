# islandsheds/downloader.py

import geopandas as gpd
import os
import requests

def download_country(country, output_dir=".//Watershed//", target_crs=None):
    # URL of the GeoPackage hosted on GitHub
    geopackage_url = "https://raw.githubusercontent.com/JXN/WTSD/master/your_geopackage.gpkg"
    
    # Download the GeoPackage
    response = requests.get(geopackage_url)
    
    if response.status_code == 200:
        # Load the GeoPackage from the response content
        gdf = gpd.read_file(response.content, layer='watersheds')
        
        # Filter data for the specified country
        country_gdf = gdf[gdf['country'] == country]
        
        # Check and inform user about CRS
        crs = gdf.crs
        print(f"The CRS of the data is {crs}")
        
        # Ask user if they want to change the CRS
        if target_crs:
            # Change CRS if target_crs is specified
            country_gdf = country_gdf.to_crs(target_crs)
            print(f"Data CRS changed to {target_crs}")
        else:
            print("Data will be downloaded with the original CRS.")
        
        # Create output directory if it doesn't exist
        if output_dir:
            create_directory(output_dir)
        
        # Save the filtered data to a new GeoPackage file
        output_file_path = os.path.join(output_dir, f"{country}_watersheds.gpkg")
        country_gdf.to_file(output_file_path, driver='GPKG')
        
        print(f"Data for {country} downloaded successfully.")
    else:
        print(f"Failed to download GeoPackage. Status code: {response.status_code}")

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)