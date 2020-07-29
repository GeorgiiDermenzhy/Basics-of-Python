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
    digit = 1
    dozen = 0
    hundred = 0

    os.chdir(dir_path)

    for file in os.listdir(dir_path):
        file_path = Path(file)
        files_number = file_path.stem[4:7]
        expected_numbers = str(hundred) + str(dozen) + str(digit)

        if files_number != expected_numbers:
            os.rename(file_path, "spam" + expected_numbers + ".txt")
            digit += 1

            if digit > 9:
                digit = 0
                dozen += 1

            if dozen > 9:
                dozen = 0
                hundred += 1
        else:
            digit += 1


filling_in_the_gaps()
