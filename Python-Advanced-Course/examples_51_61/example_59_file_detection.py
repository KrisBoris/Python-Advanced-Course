# Example 59 - File detection

import os

file_path = "test_dir/test.txt"
folder_path = "test_dir"

if os.path.exists(file_path):
    print("This path exists")

    if os.path.isfile(file_path):
        print("This is file")
    elif os.path.isdir(file_path):
        print("This is folder")

else:
    print("This path doesn't exist")