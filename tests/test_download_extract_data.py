import pytest
import os
import shutil
import responses
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.download_extract_data import download_extract_data

# Test files setup

# setup empty directory for data files to be downloaded to
if not os.path.exists('tests/test_zip_data1'):
    os.makedirs('tests/test_zip_data1')

# setup directory that contains a file for data files to be downloaded to
if not os.path.exists('tests/test_zip_data2'):
    os.makedirs('tests/test_zip_data2')
with open('tests/test_zip_data2/test4.txt', 'w') as file:
    pass  # creates an empty file

test_files_txt_csv = ['test1.txt', 'test2.csv']
test_files_subdir = ['test1.txt', 'test2.csv', 'subdir/test3.txt']
test_files_2txt_csv = ['test1.txt', 'test2.csv', 'test4.txt']

# URL for Case 1 
url_txt_csv_zip = 'https://raw.githubusercontent.com/FionaC124/dsci310-group-wildfire-predictor/abstract-download-data-script-to-fxns/tests/test_files_txt_csv.zip'

# URL for Case 2 ('test1.txt', test2.csv and 'subdir/test2.txt')
url_txt_subdir_zip = 'https://raw.githubusercontent.com/FionaC124/dsci310-group-wildfire-predictor/abstract-download-data-script-to-fxns/tests/test_files_all.zip'

# URL for Case 3 (empty zip file)
url_empty_zip = 'https://raw.githubusercontent.com/FionaC124/dsci310-group-wildfire-predictor/abstract-download-data-script-to-fxns/tests/empty.zip'

# mock non-existing URL
@pytest.fixture
def mock_response():
    # Mock a response with a non-200 status code
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'https://example.com', status=404)
        yield


# TESTS

# Case 1
# Test download_extract_data function can download and extract a zip file that 
# contains files with different formats

def test_download_extract_data_txt_csv():
    download_extract_data(url_txt_csv_zip, 'tests/test_zip_data1')
    # List of files you expect to find in the directory
    for file in test_files_txt_csv:
        file_path = os.path.join('tests/test_zip_data1', file)
        assert os.path.isfile(file_path)
    # clean up unzipped files
    for file in test_files_txt_csv:
        if os.path.exists(file):
            os.remove(file)


# Case 2
# Test download_extract_data function can download and extract a zip file that 
# contains multiple files, including a file within a nested subdirectory

def test_download_extract_data_subdir():
    download_extract_data(url_txt_subdir_zip, 'tests/test_zip_data1')
    # List of files you expect to find in the directory
    for file in test_files_subdir:
        file_path = os.path.join('tests/test_zip_data1', file)
        print("Check file path:", file_path) # Print statement
        assert os.path.isfile(file_path)
    # clean up unzipped files
    for file in test_files_subdir:
        if os.path.exists(file):
            os.remove(file)
    if os.path.exists('tests/test_zip_data1/subdir'):
        shutil.rmtree('tests/test_zip_data1/subdir')


# Case 3
# Test download_extract_data function can download and extract a zip file that 
# contains two files into a directory that already contains a file

def test_download_extract_data_nested_subdir():
    download_extract_data(url_txt_csv_zip, 'tests/test_zip_data2')
    # List of files you expect to find in the directory
    for file in test_files_2txt_csv:
        file_path = os.path.join('tests/test_zip_data2', file)
        assert os.path.isfile(file_path)
    # clean up unzipped files
    for file in test_files_txt_csv:
        if os.path.exists(file):
            os.remove(file)


# Case 4 
# Test download_extract_data function raises an error if the zip file at the 
# input URL is empty

def test_download_extract_data_empty_zip():
    with pytest.raises(ValueError, match="Data extraction failed: the given zip file is empty."):
        download_extract_data(url_empty_zip, 'tests/test_zip_data1')


# Case 5
# Test download_extract_data function raises an error if the input URL is invalid 

def test_download_extract_data_error_on_invalid_url(mock_response):
    with pytest.raises(ValueError, match="File download failed: the given URL does not exist."):
        download_extract_data('https://example.com', 'tests/test_zip_data1')


# Case 6
# Test download_extract_data function throws an error if the URL is not a zip file

def test_download_extract_data_error_on_nonzip_url():
    with pytest.raises(ValueError, match="File download failed: the given URL does not point to a zip file."):
        download_extract_data('https://github.com/', 'tests/test_zip_data1')


# Case 7
# Test download_extract_data function throws an error if the directory path 
# provided does not exist

#def test_download_extract_data_error_on_missing_dir():
#    with pytest.raises(ValueError, match='The directory provided does not exist.'):
#        download_extract_data(url_txt_csv_zip, 'tests/test_zip_data3')