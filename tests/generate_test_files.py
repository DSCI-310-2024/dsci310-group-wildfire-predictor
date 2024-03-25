import os
import zipfile
import shutil

# Create a test directory
os.makedirs('test_subdir', exist_ok=True)

# Create test file 1
with open('test1.txt', 'w') as file:
    file.write('test file 1')

# Create test file 2
with open('test2.csv', 'w') as file:
    file.write('test file 2')

# Create test file 3 inside the directory
with open('test_subdir/test3.txt', 'w') as file:
    file.write('test file 3')

# Create a zip file containing 'test1.txt' and 'test2.csv'
with zipfile.ZipFile('test_files_txt_csv.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('test1.txt')
    zipf.write('test2.csv')

# Create a zip file containing all test files
with zipfile.ZipFile('test_files_all.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('test1.txt')
    zipf.write('test2.csv')
    zipf.write('test_subdir/test3.txt')

# Create an empty zip file
with zipfile.ZipFile('empty.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    pass

# Clean up the files and directories created
test_files = ['test1.txt', 'test2.csv']
for file in test_files:
    if os.path.exists(file):
        os.remove(file)
if os.path.exists("test_subdir"):
    shutil.rmtree("test_subdir")