import json
import sys
from datetime import date

with open("text.txt", "r") as fr:
    days = json.load(fr)

help_menu = """
progress_tracker 1.0
usage: track_progress.py [options] [selection] [input]
date_format: year-month-day
-h  show help menu
-s  show start date of the 100 days of code
-a  add note per input 
    add a note to the current day
    + number: add the number of notes you specified
    + date (format year-month-day): to add a note to a specific day
    + date + number: add a number of notes to a specific day
-l  add link to web or file/directory in cmd
    + date + link + ... : add as much links to a day as you wish
-g  get one day 
    + date: get the day you specified

examples:
    track_progress_py -a 2021-02-05 4
    -> add 4 notes to the 5 of February
    track_progress.py -l 2021-01-31 /home/kali/ransom/walz https://github.com/tobi187
    -> add links to 31 of January
"""

# add 1 note to current day
if len(sys.argv) == 2:
    if sys.argv[1] == "-a":
        for i in days:
            if i["date"] == str(date.today()):
                if "notes" not in i:
                    i["notes"] = []
                note = input("note: ")
                i["notes"].append(note)
    elif sys.argv[1] == "-s":
        print(days[0]["date"])
    # print help menu
    elif sys.argv[1] == "-h":
        print(help_menu)


# add notes to other days or more than one to current day
if len(sys.argv) == 3:
    if sys.argv[1] == "-a":
        for i in days:
            if i["date"] == sys.argv[2]:
                if "notes" not in i:
                    i["notes"] = []
                note = input("note: ")
                i["notes"].append(note)
            try:
                if int(sys.argv[2]) < 20:
                    if i["date"] == str(date.today()):
                        if "notes" not in i:
                            i["note"] = []
                        for j in range(int(sys.argv[2])):
                            note = input("note: ")
                            i["note"].append(note)
            except ValueError:
                continue
    # print one day
    elif sys.argv[1] == "-g":
        for i in days:
            if i["date"] == sys.argv[2]:
                print(i)

# add more than one notes to other day
if len(sys.argv) == 4:
    if sys.argv[1] == "-a":
        for i in days:
            if i["date"] == sys.argv[2]:
                if "notes" not in i:
                    i["notes"] = []
                for j in range(int(sys.argv[3])):
                    note = input("note: ")
                    i["notes"].append(note)

# add links to days
if len(sys.argv) > 3:
    if sys.argv[1] == "-l":
        for i in days:
            if i["date"] == sys.argv[2]:
                if "link" not in i:
                    i["link"] = []
                for j in range(3, len(sys.argv)):
                    i["link"].append(sys.argv[j])


# add new item
if len(sys.argv) == 1:
    new_item = {
        "key": days[-1]["key"] + 1,
        "date": str(date.today())
    }


    def is_unique(item, item_list):
        for i in item_list:
            if item["date"] == i["date"]:
                return False

        return True


    if not is_unique(new_item, days):
        print("No 2nd chances")
        exit()

    time_coded = int(input("How long did you code today(in h)? "))
    time_videos = int(input("How long have you watched (coding)videos today(in h)? "))

    new_item["time_coded"] = time_coded
    new_item["time_videos"] = time_videos

    days.append(new_item)

with open("progress.txt", "w") as fw:
    json.dump(days, fw, indent=4)
