# download_data.py
# author: Lillian Milroy
# date: 2024-03-10

import click
import os
import requests
import zipfile
import pandas as pd
import shutil

@click.command()
@click.option('--url', type=str)
@click.option('--output_path', type=str)
@click.option('--csv_file', type=str)
def main(url, output_path, csv_file):
    """
    Downloads and extracts data in a zipped file from the internet, and stores it locally.

    Parameters:
    ----------
    url: str
        The URL of the zip file to be read
    output_path: str
        The directory in which the zip file's contents will be extracted and stored
    csv_file: str
        The name of the csv file desired

    Returns:
    ----------
    None
    """

    # Create target directory
    if os.path.exists(output_path):
        click.echo(f"Output path '{output_path}' already exists.")
    else:
        os.makedirs(output_path)

    # Extract file name
    _, filename = os.path.split(url)
    output_file_path = os.path.join(output_path, filename)

    # Now we add the contents to the folder
    response = requests.get(url)

    with open(output_file_path, 'wb') as f:
        f.write(response.content)

    # Ensuring that directory and output path do not have conflicting names
    with zipfile.ZipFile(output_file_path, 'r') as zip_ref:
        for item in zip_ref.namelist():
            filename = os.path.basename(item)
            if not filename:
                continue
            source = zip_ref.open(item)
            target = open(os.path.join(output_path, filename), "wb")
            with source, target:
                shutil.copyfileobj(source, target)

    # Remove zip file after data extracted
    os.remove(output_file_path)

    click.echo(f"Data successfully downloaded and saved to {output_path}")

    # Continue to get_csv if csv_file is given
    if csv_file is not None:
        csv_path = get_csv(output_path, csv_file)
        if csv_path:
            pass

def get_csv(directory, csv_file):
    """
    Returns the path of a specific csv file if it exists in the directory containing the data downloaded
    and extracted from the zip file in main, returns None if it does not exist.

    Parameters:
    ----------
    directory: str
        The directory containing the contents of the zip file
    csv_file: str
        The name of the csv file desired

    Returns:
    ----------
    str or None
    The path of the specified csv file if found, else None
    """
    files = [file for file in os.listdir(directory)]
    if csv_file in files:
        csv_path = os.path.join(directory, csv_file)
        click.echo(f"Selected file '{csv_file}' found at path: {csv_path}")
        return csv_path
    else:
        click.echo(f"Selected file '{csv_file}' not found in directory.")
        return None

if __name__ == '__main__':
    main()