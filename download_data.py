# download_data.py
# author: Lillian Milroy
# date: 2024-03-10

import click
import os
import requests
import zipfile
import pandas as pd

@click.command()
@click.option('--url', type = str)
@click.option('--output_path', type = str)

def main(url, output_path):
    """
    Downloads and extracts data in a zipped file from the internet, and stores it locally.

    Parameters:
    ----------
    url: str
        The URL of the zip file to be read
    output_path: str
        The directory in which the zip file's contents will be extracted and stored

    Returns:
    ----------
    None
    """
    
    # Create target directory
    target_directory_for_data = os.path.join(os.path.dirname(os.getcwd()), 'data')
    raw_folder = os.path.join(target_directory_for_data, 'Raw')

    if not os.path.exists(raw_folder):
        os.makedirs(raw_folder)

    if os.path.isdir(output_path):
        _, filename = os.path.split(url)
        output_path = os.path.join(output_path, filename)

    # Extract file name 
    output_directory, filename = os.path.split(output_path)

    # Add zip to data folder via path
    zip_file = os.path.join(raw_folder, output_path)

    # Now we add the contents to the folder
    response = requests.get(url)

    with open(zip_file, 'wb') as f:
        f.write(response.content)

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(raw_folder)

    click.echo(f"Data successfully downloaded and saved to {zip_file}")
    
if __name__ == '__main__':
        main()