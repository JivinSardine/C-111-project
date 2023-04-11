import os
import shutil


## this is directory of my mac laptop
from_dir = "/Users/michaes/Downloads"
to_dir = "/Users/michaes/Downloads/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    if ext == ".pdf":
        source_path = os.path.join(from_dir, file_name)
        destination_path = os.path.join(to_dir, file_name)
        shutil.move(source_path, destination_path)
