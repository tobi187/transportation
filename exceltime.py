from openpyxl import load_workbook
import datetime
import subprocess
import holidays

# file stuff -> copy file, open copy and open with openpyxl
get_file_name = input("Name des Excelsheets eingeben (ohne .xlsx). Falls der Name 'Leistungsbericht' ist gib einfach y ein> ")
limit = int(input("Gib das tägliche Arbeitszeitlimit an (nur ganze zahl z.B. 8)> "))

if str(get_file_name).lower() == "y":
    file_name = "Leistungsbericht"
else:
    file_name = str(get_file_name)

# subprocess.run(["cp", file_name+".xlsx", file_name+"_fertig.xlsx"], check=True)
wb = load_workbook(filename=file_name+".xlsx", data_only=True)

# declare variables we need
threshold_time = datetime.timedelta(hours=limit, minutes=0, seconds=0)
german_holidays = holidays.Germany(prov="BW", years=[2020, 2021, 2022])


def check_time_limit_multiple_days(curr_time, new_day):
    if curr_time + new_day >= threshold_time:
        possible_time = threshold_time - curr_time
        return possible_time, False

    else:
        return new_day, True


def multiple_days(start_index, active_sheet, start_date):

    for row in range(4 + start_index, 10000):
        if active_sheet.cell(row=i, column=1) == start_date:


def calculate_one_month(active_sheet):
    max_row = active_sheet.max_row
    time_multiple_days = datetime.timedelta(hours=0, minutes=0, seconds=0)
    total_time_month = datetime.timedelta(hours=0, minutes=0, seconds=0)
    real_time_month = datetime.timedelta(hours=0, minutes=0, seconds=0)
    can_still_work = True
    rows_to_delete = []

    for row in range(4, max_row + 1):
        curr_cell_time = active_sheet.cell(row=row, column=6).value
        curr_cell_date = active_sheet.cell(row=row, column=1).value
        next_day = active_sheet.cell(row=row + 1, column=1).value

        if curr_cell_time is not None and curr_cell_date is not None:
            time_worked_day = curr_cell_time
            real_time_month += time_worked_day

            # check if sunday or holiday
            if curr_cell_date.weekday() == 6 or curr_cell_date in german_holidays:
                active_sheet.cell(row=row, column=6).value = datetime.timedelta(hours=0, minutes=0, seconds=0)
                continue

            if next_day is not None:
                # check if multiple days and limit(8hours) is reached
                if next_day == curr_cell_date and not can_still_work:
                    rows_to_delete.insert(0, row)
                    continue
                else:
                    can_still_work = True

                # check multiple days
                if next_day == curr_cell_date:
                    time_worked_day, can_still_work = check_time_limit_multiple_days(time_multiple_days, time_worked_day)
                    time_multiple_days += time_worked_day
                else:
                    time_multiple_days = datetime.timedelta(hours=0, minutes=0, seconds=0)

            # check if limit is reached
            if curr_cell_time > datetime.timedelta(hours=8, minutes=0, seconds=0):
                time_worked_day = datetime.timedelta(hours=8, minutes=0, seconds=0)

            active_sheet.cell(row=row, column=6).value = time_worked_day
            total_time_month += time_worked_day

    active_sheet.cell(row=5, column=7).value = total_time_month
    active_sheet.cell(row=6, column=7).value = real_time_month

    for row in rows_to_delete:
        active_sheet.delete_rows(row)


for index, sheet in enumerate(wb.worksheets):
    calculate_one_month(sheet)
    print(f"{index + 1} von {len(wb.worksheets)}: Done")

wb.save(filename=file_name+"_fertig.xlsx")
print("_" * 30 + "\n")
print(f"Success\n{file_name}_fertig.xlsx ist fertig")
