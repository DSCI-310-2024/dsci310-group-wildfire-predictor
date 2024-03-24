import os
import requests
import zipfile
import shutil

def download_extract_data(url, output_path):
    """
    Downloads a zip file from the URL provided and extracts the data it contains, storing it locally in the specified directory

    Parameters:
    ----------
    url: str
        The URL of the zip file to be read
    output_path: str
        The directory in which the zip file's contents will be extracted and stored

    Returns:
    -------
    str
        A message indicating whether the function execution was successful.
    """
    # Fetch URL and extract file name
    response = requests.get(url)
    _, filename = os.path.split(url)
    output_file_path = os.path.join(output_path, filename)

    # Check if URL exists; if not, raise an error
    if response.status_code != 200:
        raise ValueError("File download failed: the given URL does not exist.")

    # Check if the URL points to a zip file; if not, raise an error
    if not filename.endswith(".zip"):
        raise ValueError("File download failed: the given URL does not point to a zip file.")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    # Write the zip file to the specified output path
    with open(output_file_path, 'wb') as f:
        f.write(response.content)

    # Extract the zip file to the output path
    with zipfile.ZipFile(output_file_path, 'r') as zip_ref:
        all_files = zip_ref.namelist()
        
        # Check if the zip file is empty; if yes, raise an error
        if not all_files:
            raise ValueError("Data extraction failed: the given zip file is empty.")
        
        for item in all_files:
            item_filename = os.path.basename(item)
            if not item_filename:
                continue
            source = zip_ref.open(item)
            target = open(os.path.join(output_path, item_filename), "wb")
            with source, target:
                shutil.copyfileobj(source, target)

    # Remove zip file after data extracted
    os.remove(output_file_path)

    if not os.listdir(output_path):
        raise ValueError("No files were extracted from the given zip file.")

    return f"Data successfully downloaded and saved to {output_path}"