"""Task 6 of Module 4."""
from tkinter.filedialog import askopenfilename
from pathlib import Path
import os
import PyPDF2


def brute_force_pdf():
    """Brute force encrypted PDF file with provided list of words."""
    pdf_file = askopenfilename(title='Select encrypted PDF file')
    pwd_file_path = Path(pdf_file)
    os.chdir(pwd_file_path.parent)

    dict_file = askopenfilename(title='Select encrypted Dictionary file')
    dict_file_path = Path(dict_file)

    with open(dict_file_path, "r") as dict_file_content, open(pwd_file_path.name, 'rb') as pdf_content:
        pdf_reader = PyPDF2.PdfFileReader(pdf_content)
        for word in dict_file_content:
            if pdf_reader.decrypt(word):
                print(word)
                break
            else:
                pdf_reader.decrypt(word.lower())
                print(word)
                break


brute_force_pdf()
