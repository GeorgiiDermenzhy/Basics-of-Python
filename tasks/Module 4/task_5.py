"""Task 3 of Module 5."""
import ezsheets


def finding_mistakes_in_a_spreadsheet():
    """Find values that not fit expected output of the formula."""
    ss = ezsheets.Spreadsheet('1jDZEd'
                              'vSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
    errors_location = []
    sheet = ss[0]
    number_of_rows = sheet.rowCount

    for row in range(2, number_of_rows):
        if sheet.getRow(row)[0] == "":
            print(f"Data are missing, or table contains empty row at line {row}")
            break
        elif int(sheet.getRow(row)[0]) * int(sheet.getRow(row)[1]) != int(sheet.getRow(row)[2]):
            errors_location.append(row)

    print(f"You have some errors in row/s {errors_location}")


finding_mistakes_in_a_spreadsheet()
