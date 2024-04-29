import geopandas as gpd
import os
import requests

def download_country(country, output_dir=".//Watershed//", target_crs=None):
    """
    Downloads and saves watershed data for a specified country from a GeoPackage.

    Parameters:
    - country (str): The name of the country for which watershed data is to be downloaded.
    - output_dir (str): The directory where the GeoPackage will be saved. Defaults to ".//Watershed//".
    - target_crs (str, optional): The coordinate reference system to which the data should be converted. If None, the original CRS is used.

    Outputs:
    - A new GeoPackage file in the specified directory containing the watershed data for the specified country.
    - Console messages about the status of the download and data processing steps.

    Raises:
    - Prints an error message if the GeoPackage cannot be downloaded (e.g., due to network issues or an incorrect URL).
    """
    # URL of the GeoPackage hosted on GitHub
    geopackage_url = "https://github.com/kgdthomas/IslandSheds/raw/main/CARIBBEAN_WATERSHEDS.gpkg"
    
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
    """
    Creates a directory if it does not already exist.

    Parameters:
    - directory (str): The path of the directory to be created.

    Effects:
    - A new directory is created at the specified path if it does not exist. If the directory already exists, no action is taken.
    """
    # Check if the directory exists and create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)

def show_available_datasets(geopackage_url):
    """
    Loads a GeoPackage and displays all unique countries available in the 'country' column of the dataset.

    Parameters:
    - geopackage_url (str): The URL to the GeoPackage file.

    Outputs:
    - Prints a list of unique countries found in the GeoPackage's 'country' column.
    """
    # Load the GeoPackage directly
    gdf = gpd.read_file(geopackage_url, layer='watersheds')
    unique_countries = gdf['country'].unique()
    print("Available countries in the dataset:")
    for country in unique_countries:
        print(country)

def download_watershed(base_url, country, watershed=None, download_dir="//Watershed//"):
    """
    Downloads watershed data for a specified country and optionally a specific watershed.

    Parameters:
    - base_url (str): The base URL where watershed data files are hosted.
    - country (str): The country for which watershed data is to be downloaded.
    - watershed (str, optional): The specific watershed to download. If None, all watersheds for the country are downloaded.
    - download_dir (str): The directory where the watershed data will be saved. Defaults to "//Watershed//".

    Outputs:
    - Downloads and saves the specified watershed data as a GeoJSON file in the specified directory.
    - Console messages about the status of the download.

    Raises:
    - Prints an error message if the data cannot be downloaded (e.g., due to network issues or an incorrect URL).
    """
    # Check if the directory exists and create it if it doesn't
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    # Construct the URL for the specific watershed or all watersheds
    if watershed:
        url = f"{base_url}/{country}/{watershed}.geojson"
    else:
        url = f"{base_url}/{country}/all_watersheds.geojson"
    # Download the watershed data
    response = requests.get(url)
    if response.status_code == 200:
        # Save the downloaded data to a file
        with open(os.path.join(download_dir, f"{watershed or 'all_watersheds'}.geojson"), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {watershed or 'all watersheds'} for {country} successfully.")
    else:
        print("Failed to download the data.")

def main():
    """
    Main function to run the Watershed Downloader program.

    Interactively prompts the user to enter a country name, an optional watershed name, and a download directory. It then downloads the specified watershed data using the provided details.
    """
    # URL to the GeoPackage
    geopackage_url = "https://github.com/kgdthomas/IslandSheds/raw/main/CARIBBEAN_WATERSHEDS.gpkg"
    print("Welcome to the Watershed Downloader!")
    # Display available datasets
    show_available_datasets(geopackage_url)
    # Get user input for country, watershed, and download directory
    country = input("Enter the country name: ")
    output_dir = input("Enter download directory (default is .//Watershed//): ")
    output_dir = output_dir if output_dir else ".//Watershed//"
    target_crs = input("Enter target CRS (optional): ")
    # Download the country data
    download_country(country, output_dir, target_crs)

if __name__ == "__main__":
    main()