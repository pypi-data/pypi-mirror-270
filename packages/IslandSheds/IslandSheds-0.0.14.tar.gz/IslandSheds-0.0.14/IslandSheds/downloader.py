# islandsheds/downloader.py

import geopandas as gpd
import os
import requests
import json

def download_country(country, output_dir=".//Watershed//", target_crs=None):
    # URL of the GeoPackage hosted on GitHub
    geopackage_url = "https://github.com/kgdthomas/IslandSheds/blob/main/CARIBBEAN_WATERSHEDS.gpkg"
    
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
        
        

def show_available_datasets(base_url):
    response = requests.get(f"{base_url}/index.json")  # Assuming there's an index.json that lists all datasets
    if response.status_code == 200:
        datasets = response.json()
        for country, details in datasets.items():
            print(f"Country: {country}, Number of Watersheds: {len(details['watersheds'])}")
    else:
        print("Failed to retrieve dataset information.")

def download_watershed(base_url, country, watershed=None, download_dir="//Watershed//"):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    if watershed:
        url = f"{base_url}/{country}/{watershed}.geojson"
    else:
        url = f"{base_url}/{country}/all_watersheds.geojson"
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(download_dir, f"{watershed or 'all_watersheds'}.geojson"), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {watershed or 'all watersheds'} for {country} successfully.")
    else:
        print("Failed to download the data.")

def main():
    base_url = "https://github.com/JXN/WTSD/raw/main/data"
    print("Welcome to the Watershed Downloader!")
    show_available_datasets(base_url)
    country = input("Enter the country name: ")
    watershed = input("Enter the watershed name (or press enter for all watersheds): ")
    download_dir = input("Enter download directory (default is //Watershed//): ")
    download_dir = download_dir if download_dir else "//Watershed//"
    download_watershed(base_url, country, watershed, download_dir)

if __name__ == "__main__":
    main()