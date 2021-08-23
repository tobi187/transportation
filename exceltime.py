from openpyxl import Workbook, load_workbook
import datetime
import subprocess
import holidays

# file stuff -> copy file, open copy and open with openpyxl
file_name = "Leistungsbericht"
# subprocess.run(["cp", file_name, file_name+"_fertig.xlsx"])
wb = load_workbook(filename=file_name+".xlsx", data_only=True)

# for sheet in wb:
#     active_sheet = wb[sheet]
current_sheet = wb[wb.sheetnames[0]]

# declare variables we need
threshold_time = datetime.timedelta(hours=8, minutes=0, seconds=0)
german_holidays = holidays.Germany(prov="BW", years=[2020, 2021, 2022])


def check_time_limit_multiple_days(curr_time, new_day):
    if curr_time + new_day > threshold_time:
        possible_time = threshold_time - curr_time
        return possible_time, False

    else:
        return new_day, True


def calculate_one_month(active_sheet):
    max_row = active_sheet.max_row
    time_multiple_days = datetime.timedelta(hours=0, minutes=0, seconds=0)
    total_time_month = datetime.timedelta(hours=0, minutes=0, seconds=0)
    last_date = datetime.datetime(year=2000, month=1, day=1)
    can_still_work = True
    rows_to_delete = []

    for row in range(4, max_row + 1):
        curr_cell_time = active_sheet.cell(row=row, column=6).value
        curr_cell_date = active_sheet.cell(row=row, column=1).value
        last_date = active_sheet.cell(row=row - 1, column=1).value
    
        if curr_cell_time is not None:
            time_worked_day = curr_cell_time

            # check if sunday or holiday
            if curr_cell_date.weekday() == 6 or curr_cell_date in german_holidays:
                curr_cell_time = datetime.timedelta(hours=0, minutes=0, seconds=0)
                continue

            # check if multiple days and limit(8hours) is reached
            if last_date == curr_cell_date and not can_still_work:
                rows_to_delete.insert(0, row)
                continue
            else:
                can_still_work = True

            # check multiple days
            if last_date == curr_cell_date:
                time_worked_day, can_still_work = check_time_limit_multiple_days(time_multiple_days, curr_cell_time)
                time_multiple_days += time_worked_day
            else:
                time_multiple_days = datetime.timedelta(hours=0, minutes=0, seconds=0)

            # check if limit is reached
            if curr_cell_time > datetime.timedelta(hours=8, minutes=0, seconds=0):
                time_worked_day = datetime.timedelta(hours=8, minutes=0, seconds=0)

            curr_cell_time = time_worked_day
            total_time_month += time_worked_day

    for row in rows_to_delete:
        active_sheet.delete_rows(row)


