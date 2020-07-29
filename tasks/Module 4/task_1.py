"""Task 1 of Module 4."""
from pathlib import Path
import pyinputplus as pyip

WORDS_TO_REPLACE = ["ADJECTIVE", "NOUN", "VERB"]


def mad_libs():
    """
    Create and read in text files
    and lets the user add their own text instead of words in constant.
    """
    input_file_path = Path("file.txt")
    output_file_path = Path("output_file.txt")
    new_text = []

    if not input_file_path.is_file():
        with open(input_file_path, "w") as input_file:
            input_file.write("The ADJECTIVE panda walked to the NOUN and then VERB. "
                             "A nearby NOUN was unaffected by these events.")

    with open(input_file_path, "r") as input_file:
        with open(output_file_path, "w") as output_file:
            for line in input_file:
                for word in line.split():
                    if word in WORDS_TO_REPLACE:
                        input_word = pyip.inputStr(f"Please provide {word}:\n")
                        new_text.append(input_word)
                    elif word[:len(word) - 1] in WORDS_TO_REPLACE:
                        input_word = pyip.inputStr(f"Please provide {word[:len(word) - 1]}:\n")
                        new_text.append(input_word + word[-1])
                    else:
                        new_text.append(word)
            output_file.write(" ".join(new_text))

    with open(output_file_path, "r") as input_file:
        rf_content = input_file.read()
        print(rf_content)


mad_libs()
