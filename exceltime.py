from openpyxl import Workbook, load_workbook
import datetime
import subprocess

file_name = "Leistungsbericht"

# subprocess.run(["cp", file_name, file_name+"_fertig.xlsx"])

wb = load_workbook(filename=file_name+".xlsx", data_only=True)

sheet = wb[wb.sheetnames[0]]

max_row = sheet.max_row

total_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

total_time_single_day = datetime.timedelta(hours=0, minutes=0, seconds=0)

last_date = datetime.datetime(year=2000, month=1, day=1)

threshold_time = datetime.timedelta(hours=8, minutes=0, seconds=0)

can_still_work = True


def check_time_limit_multiple_days(curr_time, new_day):
    if curr_time + new_day > threshold_time:
        possible_time = threshold_time - curr_time
        return possible_time, False

    else:
        return new_day, True


def check_multiple_days(active_sheet, index, date):
    for date_cell in range(index + 4, max_row + 1):
        if date == active_sheet.cell(row=i, )


for i in range(4, max_row + 1):
    curr_cell_time = sheet.cell(row=i, column=6).value
    curr_cell_date = sheet.cell(row=i, column=1).value
    last_date = sheet.cell(row=i-1, column=1).value

    if curr_cell_time is not None:
        total_time = curr_cell_time
        print(curr_cell_time)

        # check if sunday
        if curr_cell_date.weekday() == 6:
            curr_cell_time = datetime.timedelta(hours=0, minutes=0, seconds=0)
            continue

        # check if multiple days and limit(8hours) is reached
        if last_date == curr_cell_date and not can_still_work:
            # zelle löschen bzw ganze zeile
            sheet.delete_rows(i)
            print(total_time, curr_cell_time, curr_cell_date)
            continue
        else:
            can_still_work = True

        # check multiple days
        if last_date == curr_cell_date:
            time_worked, can_still_work = check_time_limit_multiple_days(total_time_single_day, curr_cell_time)
        else:
            total_time_single_day = datetime.timedelta(hours=0, minutes=0, seconds=0)

        # check if limit is reached
        if curr_cell_time > datetime.timedelta(hours=8, minutes=0, seconds=0):
            total_time = datetime.timedelta(hours=8, minutes=0, seconds=0)




