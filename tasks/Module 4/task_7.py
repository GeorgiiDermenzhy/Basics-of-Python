"""Task 7 of Module 4."""
from tkinter.filedialog import askdirectory
from pathlib import Path
import os
import csv
from openpyxl import load_workbook


def excel_to_csv_converter():
    """Convert excel workbooks/worksheets to csv file/s."""
    start_path = askdirectory(title='Select Folder to start search for excel files')
    os.chdir(start_path)

    save_into_path = askdirectory(title='Select Folder to start search for .jpg files')

    for file in os.listdir(start_path):
        file_path = Path(file)
        if file_path.suffix == ".xlsx":
            excel_file_name = file_path.stem
            wb = load_workbook(file_path)
            for ws in wb.worksheets:
                csv_name = excel_file_name + "_" + ws.title + ".csv"
                destination = Path(save_into_path) / Path(csv_name)
                with open(destination, "w", newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    for row in ws.rows:
                        row_data = [cell.value for cell in row]
                        csv_writer.writerow(row_data)


excel_to_csv_converter()
