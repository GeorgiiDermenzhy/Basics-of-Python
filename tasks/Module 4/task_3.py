"""Task 3 of Module 4."""
from tkinter.filedialog import askdirectory
from pathlib import Path
import os
import shutil


def selective_copy():
    """Find files with .jpg extension and moves it to selected folder."""
    start_path = askdirectory(title='Select Folder to start search for .jpg files')
    os.chdir(start_path)

    save_into_path = askdirectory(title='Select destination folder')

    for dirpath, dirnames, filenames in os.walk(start_path):
        for file in filenames:
            file_path = Path(dirpath) / Path(file)
            if file_path.suffix == ".png":
                shutil.copy(file_path, Path(save_into_path))


selective_copy()
