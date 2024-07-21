#print directory content by using os module

import os

def list_directory_contents(dir_path='.'):
    try:
        # List all files and directories in the specified directory
        entries = os.listdir(dir_path)
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory {dir_path} does not exist")
    except PermissionError:
        print(f"Permission denied to access the directory {dir_path}")
    except OSError as e:
        print(f"An OS error occurred: {e}")

# Specify the directory path here
directory_path = '/c'
list_directory_contents(directory_path)
