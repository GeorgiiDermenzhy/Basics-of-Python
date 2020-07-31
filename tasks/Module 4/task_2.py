"""Task 2 of Module 4."""
from pathlib import Path
import os
from tkinter.filedialog import askdirectory


def filling_in_the_gaps():
    """
    Find all files with a given prefix,
    in a single folder and fill in any gaps in the numbering.
    """
    dir_path = askdirectory(title='Select Folder with spam* files')
    iter = 1

    os.chdir(dir_path)

    for file in sorted(os.listdir(dir_path)):
        file_path = Path(file)

        files_number = file_path.stem[4:7]
        file_prefix = file_path.stem[:4]

        expected_number = str(iter).zfill(3)

        if files_number != expected_number:
            os.rename(file, file_prefix + expected_number + ".txt")
            iter += 1
        else:
            iter += 1


filling_in_the_gaps()
